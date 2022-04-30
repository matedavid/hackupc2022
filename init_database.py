import sqlite3
import os

if "database.db" in os.listdir("."):
  os.remove("database.db")

con = sqlite3.connect("database.db")
cur = con.cursor()

cur.execute("CREATE TABLE User (id serial primary key, email varchar(40) not null, password varchar(40) not null);")
con.commit()

con.close()
