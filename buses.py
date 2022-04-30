import requests
import json
from datetime import datetime, timedelta, date

feiners = ["Monday","Tuesday","Wednesday","Thursday","Friday"]

dia = "Monday" #date.today().strftime("%A")
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

contador = 0
for x in r["features"]:

    if hora_date >= datetime.strptime("00:00",'%H:%M') and hora_date < datetime.strptime("07:00",'%H:%M'):
        break
    #Si eso, mirar de poner el bus mas cercano

    if x["properties"]["ID_TIPUS_DIA"] == tipus_dia :
        literal = x["properties"]["LITERAL"]

        #print(literal)
        if "-" in literal:
            tmp_horas = literal.split(" - ")

            min_hour = datetime.strptime(tmp_horas[0], "%H:%M")
            max_hour = datetime.strptime(tmp_horas[-1], "%H:%M")
            if max_hour <= hora_date:
                continue
            #print(min_hour, max_hour)

            if hora_date <= min_hour:
                for times in range(5):
                    horas.append(tmp_horas[times])
                #horas = list(map(lambda x: datetime.strptime(x, "%H:%M"), tmp_horas))
                break
            elif hora_date > min_hour and hora_date <= max_hour:
                i = 1
                while hora_date >= min_hour and i < len(tmp_horas):
                    min_hour = datetime.strptime(tmp_horas[i], "%H:%M")
                    i += 1
                for times in range(5):
                    if i-1+times < len(tmp_horas):
                        horas.append(tmp_horas[i-1+times])
                break

        elif "#" in literal:
            info = literal.split(" ")

            start = datetime.strptime(info[1], "%H:%M")
            end = datetime.strptime(info[3][:5], "%H:%M")

            minutes = int(info[5])

            if hora_date >= start and hora_date <= end:
                step = start
                contador = 0
                while step <= end:
                    if step <= hora_date:
                        step += timedelta(minutes=minutes)
                    else:
                        horas.append(step)
                        step += timedelta(minutes=minutes)
                        contador +=1
                        if contador > 4:
                            break

                break
            #horas = list(filter(lambda x: x >= hora_date, horas))
    
if len(horas) == 0:
    print("NO HAY BUSES BOBO")
    exit()
print(horas)
