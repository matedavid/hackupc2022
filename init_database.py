import sqlite3
import os

if "database.db" in os.listdir("."):
  os.remove("database.db")

con = sqlite3.connect("database.db")
cur = con.cursor()

cur.execute("""CREATE TABLE User (
  id integer primary key autoincrement,
  email varchar(40) not null,
  password varchar(40) not null
);""")

cur.execute("""CREATE TABLE UserToken (
  id integer primary key autoincrement,
  token varchar(240) not null,
  user integer references User(id),
  creationTime integer not null,
  expirationTime integer not null
);""")

cur.execute("""CREATE TABLE FGCTransport (
  fgcId integer primary key autoincrement, 
  user int references User,

  originStation varchar(20) not null,
  originStationCode char(2) not null,

  destinationStation varchar(20) not null,
  destinationStationCode char(2) not null,

  time time
);""")

cur.execute("""CREATE TABLE BUSTransport (
  busId integer primary key autoincrement, 
  user int references User,

  lineName char(3) not null,
  stopName varchar(40) not null,

  time time
);""")
con.commit()

con.close()
