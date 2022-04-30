from bs4 import BeautifulSoup
import requests as req
import json
import sys
from enum import Enum

class TimeMode(Enum):
  NOW = 0
  DEPARTURE = 1
  ARRIVAL = 2

def get_url(origin_address: str, destination_address: str, timemode: TimeMode, time: str = "") -> str:
  origin_code = ""
  destination_code = ""

  stations_code = json.load(open("codigo-estaciones_fgc.json"))
  for st in stations_code:
    station_name = st['fields']['nom_estacio']

    if station_name == origin_address:
      origin_code = st['fields']['inicials']
    elif station_name == destination_address:
      destination_code = st['fields']['inicials']

  date = "29-04-2022"

  url = f"https://www.fgc.cat/es/buscador/?from_address={origin_address}&from_code={origin_code}&to_address={destination_address}&to_code={destination_code}&datetime_option={timemode.value}&date={date}"
  if timemode != TimeMode.NOW:
    url += f"&time_from={time}"

  return url

def get_trips(url):
  res = req.get(url)
  if res.status_code != 200:
    print("Status code:", res.status_code)
    exit(1)

  soup = BeautifulSoup(res.text, 'html.parser')
  trips_js = soup.find(id="form_cercador_JS-js-after")

  text = trips_js.get_text()
  idx = text.find("{")
  json_content_txt = text[idx:-2]

  json_content = json.loads(json_content_txt)
  trips = json_content["result"]["Trips"]

  for t in trips:
    trip = t['steps'][0]
    route = trip["route"]
    departure = trip["departure"]
    arrival = trip["arrival"]

    print(f"{route}: {departure}-{arrival}")

if __name__ == "__main__":
  args = sys.argv

  origin = args[1]
  destination = args[2]
  timemode = args[3]

  if timemode == "now":
    timemode = TimeMode.NOW
  elif timemode == "departure":
    timemode = TimeMode.DEPARTURE
  elif timemode == "arrival":
    timemode = TimeMode.ARRIVAL

  time = ""
  if timemode != TimeMode.NOW:
    time = args[4]

  url = get_url(origin, destination, timemode, time)
  print(url)
  get_trips(url)
