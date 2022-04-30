import requests
import json
from datetime import datetime, date

def print_horario(primera_sortida, darrera_sortida,tipus_dia):
    if tipus_dia == 1 or tipus_dia == 2:
        print(f"Primera sortida: {primera_sortida}")
        print(f"Darrera sortida: {darrera_sortida}")
    elif tipus_dia == 3:
        print("Servicio 24h")
    elif tipus_dia == 4:
        print(f"Darrera sortida: {darrera_sortida}")

nom_linia = "L3"

get_metro = requests.get("https://api.tmb.cat/v1/transit/linies/metro?app_id=896b5b9e&app_key=8ff3a68902a34aa9e2a6e6ff037f0ff1")

if get_metro.status_code != 200:
    print("Error GET Metro")
    exit()

r = get_metro.json()

codigo_linea = 0

for x in r["features"]:
    if x["properties"]["NOM_LINIA"] == nom_linia:
        codigo_linea = x["properties"]["CODI_LINIA"]
        break

if codigo_linea == 0:
    print("No existe la linea")
    exit()

print(f"{codigo_linea}")

"""
nom_estacion = "Maria Cristina"

get_estacion = requests.get(f"https://api.tmb.cat/v1/transit/linies/metro/{codigo_linea}/estacions?app_id=896b5b9e&app_key=8ff3a68902a34aa9e2a6e6ff037f0ff1")

r.get_estacion.json()

"""
feiners = ["Monday","Tuesday","Wednesday","Thursday"]
dia = "Friday"#date.today().strftime("%A")
tipus_dia = 0
if dia in feiners:
    tipus_dia = 1
elif dia == "Friday":
    tipus_dia = 2
elif dia == "Saturday":
    tipus_dia = 3
else:
    tipus_dia = 4

print(dia)

get_hora = requests.get(f"https://api.tmb.cat/v1/transit/linies/metro/{codigo_linea}/horaris?app_id=896b5b9e&app_key=8ff3a68902a34aa9e2a6e6ff037f0ff1")

if get_hora.status_code != 200:
    print("Error GET Horario")
    exit()

r = get_hora.json()

for x in r["features"]:
    if x["properties"]["ID_TIPUS_DIA"] == tipus_dia:
        primera_sortida = x["properties"]["PRIMERA_SORTIDA"]
        darrera_sortida = x["properties"]["ULTIMA_SORTIDA"]

        print_horario(primera_sortida,darrera_sortida,tipus_dia)
        break
