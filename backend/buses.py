import requests
import json
from datetime import datetime, timedelta, date
from typing import Dict, Tuple, List

def get_horarios(linea: str, parada: str, tiempo: str | None) -> Dict[str,str | List[str]]:
    codigo_linea = get_codigo_linea(linea)
    codigo_parada = get_codigo_parada(codigo_linea, parada)
    horas_proximas = get_horas_proximas(codigo_linea,codigo_parada,tiempo)
    if tiempo != None:
        minutos_restantes = get_minutos_restantes(codigo_parada, linea)
    else:
        minutos_restantes = None
    dic ={
        "horas_proximas": horas_proximas,
        "minutos_restantes": minutos_restantes
    }
    return dic

def get_minutos_restantes(codigo_parada:int, linea:str) -> str:
    
    get_min_res = requests.get(f"https://api.tmb.cat/v1/ibus/stops/{codigo_parada}?app_id=896b5b9e&app_key=8ff3a68902a34aa9e2a6e6ff037f0ff1")
    r = get_min_res.json()

    for x in r["data"]["ibus"]:
        if x["line"] == linea:
            minutos_res = x["t-in-min"]
            return str(minutos_res)

def get_horas_proximas(codigo_linea: int, codigo_parada: int, tiempo: str) -> List[str]:
    feiners = ["Monday","Tuesday","Wednesday","Thursday","Friday"]

    dia = date.today().strftime("%A")
    tipus_dia = 0
    if dia in feiners:
        tipus_dia = 1
    elif dia == "Saturday":
        tipus_dia = 2
    else:
        tipus_dia = 3
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

    horas_proximas = []
    contador = 0

    if tiempo is not None:
        hora_date = datetime.strptime(tiempo,"%H:%M")
    else:
        ttt = datetime.today()
        hora_date = datetime(1900, 1, 1, ttt.hour, ttt.minute, ttt.second)

    for time in horas:
        if hora_date < time:    
            horas_proximas.append(time.strftime("%H:%M"))
            contador += 1
            if contador > 4:
                break
    return horas_proximas

def get_codigo_parada(codigo_linea: int, parada: str) -> int:
    get_parada = requests.get(f"https://api.tmb.cat/v1/transit/linies/bus/{codigo_linea}/parades?app_id=896b5b9e&app_key=8ff3a68902a34aa9e2a6e6ff037f0ff1")

    if get_parada.status_code != 200:
        print("Error GET Parada")
        exit()

    r = get_parada.json()

    codigo_parada = 0

    for x in r["features"]:
        if x["properties"]["NOM_PARADA"] == parada:
            codigo_parada = x["properties"]["CODI_PARADA"]
            break

    if codigo_parada == 0:
        print("No existe la parada")
        return 0

    return codigo_parada

def get_codigo_linea(linea: str) -> int:
    get_bus = requests.get("https://api.tmb.cat/v1/transit/linies/bus?app_id=896b5b9e&app_key=8ff3a68902a34aa9e2a6e6ff037f0ff1")

    if get_bus.status_code != 200:
        print("Error GET Bus")
        exit()

    r = get_bus.json()

    codigo_linea = 0
 
    for x in r["features"]:
        if x["properties"]["NOM_LINIA"] == linea:
            codigo_linea = x["properties"]["CODI_LINIA"]
            break

    if codigo_linea == 0:
        print("No existe la linea ")
        return 0

    return codigo_linea


def print_horas(horas):
    print("Próximas horas: \n")
    for time in horas:
        tiempo = time.strftime("%H:%M")
        print(f"{tiempo}\t")


if __name__ == "__main__":
    print(get_codigo_linea("V21"))
    print(get_codigo_parada(221,"Padilla - Mas Casanovas"))
    print(get_horas_proximas(221,1234,"10:00"))
    print(get_minutos_restantes(1234,"V21"))
    print(get_horarios("V21","Padilla - Mas Casanovas","10:00"))
