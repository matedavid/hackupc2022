from flask import Flask, request 
import sqlite3
import json
from typing import Dict, Tuple
import time
import jwt

from fgc import get_station_code

app = Flask(__name__)

def response(status: bool, data: str = "") -> str:
  return json.dumps({ "status": status, "data": data })

def create_user_token(user: Tuple[int, str], creation_time: float, expiration_time: float) -> str:
  payload = {
    "id": user[0],
    "email": user[1],
    "creationTime": int(creation_time),
    "expirationTime": int(expiration_time)
  }

  # TODO: Save secret key in env file
  secret_key = "secret"
  encoded = jwt.encode(payload, secret_key, algorithm="HS256")
  return encoded

@app.route("/api/user/create", methods=["POST"])
def create_user():
  data = json.loads(request.data)

  con = sqlite3.connect("database.db")
  cur = con.cursor()

  cur.execute("SELECT * FROM User WHERE email=?", (data['email'],))
  users = cur.fetchall()

  if len(users) != 0:
    con.close()
    return response(False, "User with same email already exists")

  cur.execute("INSERT INTO User (email, password) values (?, ?)", (data['email'], data['password']))
  con.commit()

  con.close()

  return response(True)

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
    return response(False, "Internal error")
  elif len(users) == 0:
    con.close()
    return response(False, "The User does not exist")

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

  return response(True, data=user_token)

# TEMPORAL: Test
@app.route("/api/user/tokens", methods=["GET"])
def get_tokens():
  con = sqlite3.connect("database.db")
  cur = con.cursor()

  cur.execute("SELECT * FROM UserToken")
  tokens = cur.fetchall()

  print(tokens)

  return "Ok"
  

@app.route("/api/user/", methods=["GET"])
def get_users():
  con = sqlite3.connect("database.db")
  cur = con.cursor()

  cur.execute("SELECT * FROM User")
  users = cur.fetchall()

  con.close()

  print(users)
  return "Ok"

@app.route("/api/fgc/", methods=["GET"])
def get_fgc():
  con = sqlite3.connect("database.db")
  cur = con.cursor()

  cur.execute("SELECT * FROM FGCTransport;")
  fgcs = cur.fetchall()

  con.close()
  print(fgcs)

  return "Ok"

@app.route("/api/bus/", methods=["GET"])
def get_bus():
  con = sqlite3.connect("database.db")
  cur = con.cursor()

  cur.execute("SELECT * FROM BUSTransport;")
  buses = cur.fetchall()

  con.close()
  print(buses)

  return "Ok"
### 

@app.route("/api/fgc/add", methods=["POST"])
def add_fgc_entry():
  data = json.loads(request.data)

  origin = data["origin"]
  destination = data["destination"]
  time = data["time"]
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

  return response(True)

@app.route("/api/bus/add", methods=["POST"])
def add_bus_entry():
  data = json.loads(request.data)

  user = data["user"]
  line_name = data["lineName"]
  stop_name = data["stopName"]
  time = data["time"]

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

  return response(True)

if __name__ == "__main__":
  app.run(debug=True)
