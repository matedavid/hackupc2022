from flask import Flask, request 
from flask_cors import CORS

import sqlite3
import json
from typing import Dict, Tuple
import time
import jwt

from fgc import get_times, get_station_code
from buses import get_horarios as bus_horarios 
from metro import get_horarios as metro_horarios

app = Flask(__name__)
CORS(app)

# TODO: Save secret key in env file
secret_key = "secret"

def json_response(status: bool, data: str = "") -> str:
  return json.dumps({ "status": status, "data": data })

def validate_time(time: str) -> str:
  h, m = time.split(":")
  if len(h) != 2:
    h = f"0{h}"
  if len(m) != 2:
    m = f"0{m}"

  return f"{h}:{m}"

def create_user_token(user: Tuple[int, str], creation_time: float, expiration_time: float) -> str:
  payload = {
    "id": user[0],
    "email": user[1],
    "creationTime": int(creation_time),
    "expirationTime": int(expiration_time)
  }

  encoded = jwt.encode(payload, secret_key, algorithm="HS256")
  return encoded

def decode_jwt_token(token: str) -> Dict[str, str]:
  return jwt.decode(token, secret_key, algorithms=["HS256"])

def validate_user_token(token: str) -> bool:
  current_time = time.time()
  try:
    payload = decode_jwt_token(token)

    con = sqlite3.connect("database.db")
    cur = con.cursor()

    cur.execute("""SELECT * from User where id = ?;""", (payload['id'],))
    users = cur.fetchall()

    con.close()
    return current_time < payload["expirationTime"] and len(users) == 1

  except Exception as e:
    print("Exception decoding jwt token:", e)
    return False

@app.route("/api/user/create", methods=["POST"])
def create_user():
  data = json.loads(request.data)

  con = sqlite3.connect("database.db")
  cur = con.cursor()

  cur.execute("SELECT * FROM User WHERE email=?", (data['email'],))
  users = cur.fetchall()

  if len(users) != 0:
    con.close()
    return json_response(False, "User with same email already exists")

  cur.execute("INSERT INTO User (email, password) values (?, ?)", (data['email'], data['password']))
  con.commit()

  con.close()

  return json_response(True)

@app.route("/api/user/login", methods=["POST"])
def login_user():
  data = json.loads(request.data)

  email = data["email"]
  password = data["password"]

  con = sqlite3.connect("database.db")
  cur = con.cursor()

  cur.execute("SELECT id, email from User where email = ? and password = ?", (email, password))
  users = cur.fetchall()

  if len(users) > 1:
    con.close()
    return json_response(False, "Internal error")
  elif len(users) == 0:
    con.close()
    return json_response(False, "The User does not exist")

  user = users[0]
  print(user)

  cur.execute("""SELECT * from UserToken where user = ?;""", (user[0],))
  tokens = cur.fetchall()

  print(tokens)

  if len(tokens) >= 1:
    for token in tokens:
      cur.execute("""DELETE from UserToken where id = ?""", (token[0],))

  current_time = time.time()
  expiration_time = current_time + 60*60  # 1 hour
  user_token = create_user_token(user, current_time, expiration_time)

  cur.execute("""INSERT INTO UserToken (
    token,
    user,
    creationTime,
    expirationTime
  ) VALUES (?, ?, ?, ?);""", (user_token, user[0], current_time, expiration_time))
  con.commit()

  return json_response(True, data=user_token)

@app.route("/api/user/validateToken/<token>", methods=["GET"])
def validate_token(token):
  is_token_valid = validate_user_token(token)
  print(is_token_valid)
  return json_response(is_token_valid)

@app.route("/api/fgc/add", methods=["POST"])
def add_fgc_entry():
  data = json.loads(request.data)

  origin = data["origin"]
  destination = data["destination"]
  time = None if data["time"] is None else validate_time(data["time"])
  user = data["user"]

  origin_code = get_station_code(origin)
  destination_code = get_station_code(destination)

  con = sqlite3.connect("database.db")
  cur = con.cursor()

  # TODO: Any check before inserting?
  # - Check user exists?

  cur.execute("""INSERT INTO FGCTransport (
      user, 
      originStation, 
      originStationCode, 
      destinationStation, 
      destinationStationCode,
      time
    ) VALUES (?, ?, ?, ?, ?, ?)""", (user, origin, origin_code, destination, destination_code, time))

  con.commit()
  con.close()

  return json_response(True)

@app.route("/api/bus/add", methods=["POST"])
def add_bus_entry():
  data = json.loads(request.data)

  user = data["user"]
  line_name = data["lineName"]
  stop_name = data["stopName"]
  time = None if data["time"] == None else validate_time(data["time"])

  # TODO: Any check before inserting?
  # - Check user exists?

  con = sqlite3.connect("database.db")
  cur = con.cursor()

  cur.execute("""INSERT INTO BUSTransport (
    user, 
    lineName,
    stopName,
    time 
  ) VALUES (?, ?, ?, ?)""", (user, line_name, stop_name, time))

  con.commit()
  con.close()

  return json_response(True)

@app.route("/api/metro/add", methods=["POST"])
def add_metro_entry():
  data = json.loads(request.data)

  user = data["user"]
  line_name = data["lineName"]

  con = sqlite3.connect("database.db")
  cur = con.cursor()

  cur.execute("""INSERT INTO METROTransport (
    user,
    lineName
  ) VALUES (?, ?);""", (user, line_name))

  con.commit()
  con.close()

  return json_response(True)

@app.route("/api/overview/<user_session>", methods=["GET"])
def overview(user_session):
  is_token_valid = validate_user_token(user_session)

  if not is_token_valid:
    return json_response(False, "User token has expired")

  payload = decode_jwt_token(user_session)
  user_id = payload["id"]

  con = sqlite3.connect("database.db")
  cur = con.cursor()

  overview = {
    "FGC": [],
    "BUS": [],
    "MET": []
  }

  # FGC 
  cur.execute("""SELECT originStation, destinationStation, time FROM FGCTransport where user = ?;""", (user_id,))
  fgc_results = cur.fetchall()

  for fgc_res in fgc_results:
    times = get_times(fgc_res[0], fgc_res[1], fgc_res[2])
    print(times)
    overview["FGC"].append({"origin": fgc_res[0], "destination": fgc_res[1], "times": times})

  # BUS
  cur.execute("""SELECT lineName, stopName, time FROM BUSTransport where user = ?;""", (user_id,))
  bus_results = cur.fetchall()

  for bus_res in bus_results:
    times = bus_horarios(bus_res[0], bus_res[1], bus_res[2])
    print(times)
    overview["BUS"].append({"lineName": bus_res[0], "stopName": bus_res[1], "times": times})

  # MET
  cur.execute("""SELECT lineName from METROTransport where user = ?;""", (user_id,))
  met_results = cur.fetchall()

  for met_res in met_results:
    times = metro_horarios(met_res[0])
    print(times)
    overview["MET"].append({"lineName": met_res[0], "times": times})  

  return json_response(True, overview)

if __name__ == "__main__":
  app.run(debug=True)
