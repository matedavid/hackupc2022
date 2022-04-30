import requests
import json
from datetime import datetime, timedelta


nom_linia = "V21" #input("Que linea?")

get_bus = requests.get("https://api.tmb.cat/v1/transit/linies/bus?app_id=896b5b9e&app_key=8ff3a68902a34aa9e2a6e6ff037f0ff1")

r = get_bus.json()

codigo_linea = 0

for x in r["features"]:
    if(x["properties"]["NOM_LINIA"] == nom_linia):
        codigo_linea = x["properties"]["CODI_LINIA"]
        break

if codigo_linea == 0:
    print("No existe la linea ")
    exit()

print(str(codigo_linea) + "\n")

nom_parada = "Padilla - Mas Casanovas" #input("Que parada? ")

get_parada = requests.get("https://api.tmb.cat/v1/transit/linies/bus/"+str(codigo_linea)+"/parades?app_id=896b5b9e&app_key=8ff3a68902a34aa9e2a6e6ff037f0ff1")

r = get_parada.json()

codigo_parada = 0

for x in r["features"]:
    if(x["properties"]["NOM_PARADA"] == nom_parada):
        codigo_parada = x["properties"]["CODI_PARADA"]
        break

if codigo_parada == 0:
    print("No existe la parada")
    exit()

print(str(codigo_parada) + "\n")

hora = input("Que hora? ")

hora_date = datetime.strptime(hora, '%H:%M')

get_hora = requests.get("https://api.tmb.cat/v1/transit/linies/bus/"+str(codigo_linea)+"/parades/"+str(codigo_parada)+"/horespas?app_id=896b5b9e&app_key=8ff3a68902a34aa9e2a6e6ff037f0ff1")

r = get_hora.json()

horas = []

for x in r["features"]:
    literal = x["properties"]["LITERAL"]
    if "-" in literal:
        tmp_horas = literal.split(" - ")

        min_hour = datetime.strptime(tmp_horas[0], "%H:%M")
        max_hour = datetime.strptime(tmp_horas[-1], "%H:%M")

        #print(min_hour, max_hour)

        if hora_date >= min_hour and hora_date <= max_hour:
            horas = list(map(lambda x: datetime.strptime(x, "%H:%M"), tmp_horas))
            break

    elif "#" in literal:
        info = literal.split(" ")

        start = datetime.strptime(info[1], "%H:%M")
        end = datetime.strptime(info[3][:5], "%H:%M")

        minutes = int(info[5])

        if hora_date >= start and hora_date <= end:
            step = start
            while step <= end:
                horas.append(step)
                step += timedelta(minutes=minutes)

            break

horas = list(filter(lambda x: x >= hora_date, horas))
if len(horas) == 0:
    print("NO HAY BUSES BOBO")
    exit()
print(horas)

"""
if "-" in v1:
    horas = v1.split(" - ")

if "#" in v2:
    horas = v2.split(" ")
    horas[1], horas[3], horas[5]
"""