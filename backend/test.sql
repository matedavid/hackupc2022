create table User (
  id serial primary key,
  email varchar(40) not null,
  password varchar(40) not null
);

create table UserToken {
  id serial primary key,
  token varchar(120) not null,
  user serial references User,
  creationTime integer not null,
  expirationTime integer not null
}

create table FGCTransport (
  user serial references User,

  fgcId serial primary key, 

  originStation varchar(40) not null,
  originStationCode char(2) not null,

  destinationStation varchar(40) not null,
  destinationStationCode char(2) not null,

  time time
);

create table BusTransport (
  user serial references User,

  busId serial primary key,

  lineName varchar(40) not null,
  stopName varchar(40) not null,

  time time
);

create table MetroTransport (
  user serial references User,
  metroId serial primary key,
  lineName char(5) not null
)