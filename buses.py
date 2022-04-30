import requests
import json
from datetime import datetime, timedelta, date


def print_horas(horas):
    print("Próximas horas: \n")
    for time in horas:
        tiempo = time.strftime("%H:%M")
        print(f"{tiempo}\t")



feiners = ["Monday","Tuesday","Wednesday","Thursday","Friday"]

dia = date.today().strftime("%A")
tipus_dia = 0
if dia in feiners:
    tipus_dia = 1
elif dia == "Saturday":
    tipus_dia = 2
else:
    tipus_dia = 3

print(dia)

nom_linia = "V21" #input("Que linea?")

get_bus = requests.get("https://api.tmb.cat/v1/transit/linies/bus?app_id=896b5b9e&app_key=8ff3a68902a34aa9e2a6e6ff037f0ff1")

if get_bus.status_code != 200:
    print("Error GET Bus")
    exit()

r = get_bus.json()

codigo_linea = 0
 
for x in r["features"]:
    if x["properties"]["NOM_LINIA"] == nom_linia:
        codigo_linea = x["properties"]["CODI_LINIA"]
        break

if codigo_linea == 0:
    print("No existe la linea ")
    exit()

print(str(codigo_linea) + "\n")

nom_parada = "Padilla - Mas Casanovas" #input("Que parada? ")

get_parada = requests.get(f"https://api.tmb.cat/v1/transit/linies/bus/{codigo_linea}/parades?app_id=896b5b9e&app_key=8ff3a68902a34aa9e2a6e6ff037f0ff1")

if get_parada.status_code != 200:
    print("Error GET Parada")
    exit()

r = get_parada.json()

codigo_parada = 0

for x in r["features"]:
    if x["properties"]["NOM_PARADA"] == nom_parada:
        codigo_parada = x["properties"]["CODI_PARADA"]
        break

if codigo_parada == 0:
    print("No existe la parada")
    exit()

print(str(codigo_parada) + "\n")

hora = input("Que hora? ")

hora_date = datetime.strptime(hora, '%H:%M')

get_hora = requests.get(f"https://api.tmb.cat/v1/transit/linies/bus/{codigo_linea}/parades/{codigo_parada}/horespas?app_id=896b5b9e&app_key=8ff3a68902a34aa9e2a6e6ff037f0ff1")

if get_hora.status_code != 200:
    print("Error GET Horario")
    exit()

r = get_hora.json()

horas = []

contador = 0
for x in r["features"]:

    if x["properties"]["ID_TIPUS_DIA"] == tipus_dia :
        literal = x["properties"]["LITERAL"]

        #print(literal)
        if "-" in literal:
            tmp_horas = literal.split(" - ")
            for time in tmp_horas:
                horas.append(datetime.strptime(time,"%H:%M"))

        elif "#" in literal:
            info = literal.split(" ")
            start = datetime.strptime(info[1], "%H:%M")
            end = datetime.strptime(info[3][:5], "%H:%M")

            minutes = int(info[5])

            step = start
            while step <= end:
                horas.append(step)
                step += timedelta(minutes=minutes)
            #horas = list(filter(lambda x: x >= hora_date, horas))

#print(horas)

horas_proximas = []
contador = 0

for time in horas:
    if hora_date < time:    
        horas_proximas.append(time)
        contador += 1
        if contador > 4:
            break


if len(horas_proximas) == 0:
    print("NO HAY BUSES BOBO")
    exit()

print_horas(horas_proximas)


get_min_res = requests.get(f"https://api.tmb.cat/v1/ibus/stops/{codigo_parada}?app_id=896b5b9e&app_key=8ff3a68902a34aa9e2a6e6ff037f0ff1")
r = get_min_res.json()

for x in r["data"]["ibus"]:
    if x["line"] == nom_linia:
        minutos_res = x["t-in-min"]
        if minutos_res > 1:
            print(f"Quedan {minutos_res} minutos para el siguiente bus.")
        else:
            print(f"La llegada de {nom_linia} es inminente")
        break

