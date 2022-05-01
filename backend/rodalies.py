import requests
import json
from datetime import datetime, date
from typing import Dict, List, Tuple, Set


def get_routes_data(file:str) -> Dict[str,str]:
    routes = open(file,"r")
    routes.readline()

    routes_data = []

    for x in routes:
        line = x.split(",")
        routes_data.append({
            "route_id":line[0].strip(),
            "line_name":line[1].strip(),
            "route_from":line[2][:40].strip(),
            "route_to":line[2][40:].strip()[1:],
        })

    routes.close()
    return routes_data


def get_stops_data(file:str) -> Dict[str,str]:
    stops = open(file,"r")
    stops.readline()

    stops_data = []

    for x in stops:
        line = x.split(",")
        stops_data.append({
            "stop_id":line[0].strip(),
            "stop_name":line[1].strip(),
        })

    stops.close()
    return stops_data

def get_times_data(file:str) -> Dict[str,str]:
    times = open(file,"r")
    times.readline()

    times_data = []
    for x in times:
        line = x.split(",")
        times_data.append({
            "trip_id":line[0].strip(),
            "arrival_time":line[1].strip(),
            "departure_time":line[2].strip(),
            "stop_id":line[3].strip(),
            "stop_sequence":line[4].strip()
        })
    times.close()
    return times_data


def get_trips_data(file:str) -> Dict[str,str]:
    trips = open(file,"r")
    trips.readline()

    trips_data = []
    for x in trips:
        line = x.split(",")
        trips_data.append({
            "route_id":line[0].strip(),
            "trip_id":line[2].strip(),
            "service_id":line[1].strip()
        })
    trips.close()
    return trips_data

def get_stop_id(stop:str,stops:Dict[str,str]) -> str:
    for x in stops:
        if x["stop_name"] == stop:
            return x["stop_id"]

def get_route_id(stop_id1:str,stop_id2:str,timetable:Dict[str,str],trips:Dict[str,str]) ->str:
    id1 = False
    id2 = False
    id_trip = ""

    for x in timetable:
        if x["stop_id"] == stop_id1:
            id1 = True
            id_trip = x["trip_id"]
        if x["stop_id"] == stop_id2 and id_trip == x["trip_id"]:
            id2 = True
        if id1 and id2:
            break
    
    for x in trips:
        if x["trip_id"] == id_trip:
            return x["route_id"]


            


def get_trip_id(stop_id1:str,stop_id2:str,time:str,timetable:Dict[str,str]) -> str:
    trip_id = ""
    for x in timetable:
        if datetime.strptime(time, "%H:%M:%S") > datetime.strptime(x["arrival_time"],"%H:%M:%S"):
            print(time)
            print(x["arrival_time"])
            
        else:
            print(x["arrival_time"])
            if x["stop_id"] == stop_id1:
                trip_id = x["trip_id"]
                for y in timetable:
                    if y["stop_id"] == stop_id2 and y["trip_id"] == trip_id:
                        if int(x["stop_sequence"]) < int(y["stop_sequence"]):
                            return trip_id
                        else:
                            break

def get_trips(route_id:str,trips_data:Dict[str,str])->List[str]:
    trips = []
    for x in trips_data:
        if x["route_id"] == route_id:
            trips.append(x["trip_id"])
    return trips

def get_times_route(trips: List[str], times_data:Dict[str,str],time:str) -> Set[str]:
    trip_times = set()
    for x in times_data:
        for y in trips:
            print(x["arrival_time"])
            if x["trip_id"] == y and datetime.strptime(x["arrival_time"],"%H:%M:%S") > datetime.strptime(time,"%H:%M:%S"):
                trip_times.add(x["arrival_time"])

    return trip_times


def get_timetables(origin:str,destination:str,time:str):
    stops_data = get_stops_data("rodalies/stops.txt")
    times_data = get_times_data("rodalies/stop_times.txt")
    trips_data = get_trips_data("rodalies/trips.txt")
    
    origin_id = get_stop_id(origin,stops_data)
    destination_id = get_stop_id(destination,stops_data)
    route_id = get_route_id(origin_id,destination_id,times_data,trips_data)
    trips = get_trips(route_id,trips_data)
    
    arrival_times = get_times_route(trips,times_data,time)
    print(arrival_times)
    count = 0
        



get_timetables("Viladecans","Castelldefels","12:00:00")
