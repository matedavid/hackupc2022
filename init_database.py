import sqlite3
import os

if "database.db" in os.listdir("."):
  os.remove("database.db")

con = sqlite3.connect("database.db")
cur = con.cursor()

cur.execute("CREATE TABLE User (id integer primary key autoincrement, email varchar(40) not null, password varchar(40) not null);")

cur.execute("""CREATE TABLE FGCTransport (
  fgcId integer primary key autoincrement, 
  user int references User,

  originStation varchar(20) not null,
  originStationCode char(2) not null,

  destinationStation varchar(20) not null,
  destinationStationCode char(2) not null,

  time time);""")
con.commit()

con.close()
