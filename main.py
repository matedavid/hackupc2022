from bs4 import BeautifulSoup
import requests as req
import json

res = req.request("GET", "https://www.fgc.cat/es/buscador/?from_address=Sarri%C3%A0&from_code=SR&to_address=Pl.+Catalunya&to_code=PC&datetime_option=0&range_option=0&date=29-04-2022&time_from=22%3A29&transport=0")
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