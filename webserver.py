from flask import Flask, request 
import sqlite3
import json
from fgc import get_station_code

app = Flask(__name__)

def response(status: bool, data: str = "") -> str:
  return json.dumps({ "status": status, "data": data })

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

# TEMPORAL: Test
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

if __name__ == "__main__":
  app.run(debug=True)
