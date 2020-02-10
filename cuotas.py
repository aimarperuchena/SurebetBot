import urllib.request
import pymysql
import urlopen
import request
import requests
from bs4 import BeautifulSoup
from datetime import date
import datetime
from urllib.request import Request, urlopen

'''---------------------------------------------------------------'''


def enviarPost(match, date, team1, team2, odd1, odd2, odd3, bookie1, bookie2, bookie3, percentage,today):
  
    fecha = today.strftime("%Y-%m-%d")
    url = 'https://aimarsurebet.herokuapp.com/api/surebet'
    objeto = {'match': match, 'date': fecha, 'team1': team1, 'team2': team2, 'odd1': odd1, 'odd2': odd2,
              'odd3': odd3, 'bookie1_id': bookie1, 'bookie2_id': bookie2, 'bookie3_id': bookie3, 'percentage': percentage}
    x = requests.post(url, data=objeto)
    print(x.text)


'''---------------------------------------------------------------'''
def leer():
    today = date.today()
    d1 = today.strftime("%d-%m-%Y")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

    req = Request(
        url='http://www.elcomparador.com/futbol/'+str(d1), headers=headers)
    html = urlopen(req).read()
    soup2 = BeautifulSoup(html)
    contSurebets = 0
    contPartidos = 0
    tomorrow = today + datetime.timedelta(days=1)
    print(tomorrow)
    div_contenedor = soup2.find("div", {"id": "contenedor_lista_partidos"})
    div_partido = div_contenedor.findAll("div", {"id": "contenedor_evento"})
    for partido in div_partido:

        fila_evento = partido.find("div", {"id": "fila_evento"})
        celda_evento_fecha = fila_evento.find("div", {"id": "celda_evento_fecha"})
        horas = celda_evento_fecha.findAll("span", {"class": "hora"})
        hora_text = ''
        for hora in horas:
            hora_text = hora.text
        celda_evento_partido = fila_evento.find(
            "div", {"id": "celda_evento_partido"})
        franja_equipos = celda_evento_partido.findAll("span", {"class": "equipo"})
        contNombre = 0

        team1 = ''
        team2 = ''
        odd1 = 0
        odd2 = 0
        odd3 = 0
        bookie1 = ''
        bookie1_id = 0
        bookie2 = ''
        bookie2_id = 0
        bookie3 = ''
        bookie3_id = 0
        bookie = ''
        bookieId = 0
        celda_evento_cuotas = fila_evento.find(
            "div", {"id": "celda_evento_cuotas"})
        contenedor_cuotas = celda_evento_cuotas.findAll(
            "div", {"id": "contenedor_cuotas"})
        for contenedor_cuota in contenedor_cuotas:
            fila_cuotas = contenedor_cuota.findAll("div", {"id": "fila_cuotas"})
            contCuota = 0
            for fila_cuota in fila_cuotas:
                celda_cuotas = fila_cuota.find("div", {"class": "verde"})
                if celda_cuotas is not None:
                    a_link = celda_cuotas.find('a')

                    link = a_link['href']
                    if "bet365" in link:
                        bookie = "bet365"
                        bookieId = 1
                    if "codere" in link:
                        bookie = "codere"
                        bookieId = 2
                    if "bwin" in link:
                        bookie = "bwin"
                        bookieId = 3
                    if "marathonbet" in link:
                        bookie = "marathon bet"
                        bookieId = 4
                    if "luckia" in link:
                        bookie = "luckia"
                        bookieId = 5
                    if "sportium" in link:
                        bookie = "sportium"
                        bookieId = 6
                    if "betway" in link:
                        bookie = "betway"
                        bookieId = 7
                    if "marcaapuestas" in link:
                        bookie = "marca apuestas"
                        bookieId = 8
                    if "willhill" in link:
                        bookie = "william hill"
                        bookieId = 9
                    if "sport888" in link:
                        bookie = "888 sport"
                        bookieId = 10
                    if "betfair" in link:
                        bookie = "betfair"
                        bookieId = 11
                    if "interwetten" in link:
                        bookie = "interwetten"
                        bookieId = 12

                    if contCuota == 0:
                        odd1 = float(celda_cuotas.text)
                        bookie1 = bookie
                        bookie1_id = bookieId
                    if contCuota == 1:
                        odd2 = float(celda_cuotas.text)
                        bookie2 = bookie
                        bookie2_id = bookieId
                    if contCuota == 2:
                        odd3 = float(celda_cuotas.text)
                        bookie3 = bookie
                        bookie3_id = bookieId
                    contCuota = contCuota+1

        for equipo in franja_equipos:
            if contNombre == 0:
                team1 = equipo.text
            if contNombre == 1:
                team2 = equipo.text
            contNombre = contNombre+1

        if hora_text != '':
            if odd1 != 0 and odd2 != 0 and odd3 != 0:
                contPartidos = contPartidos+1
                percentage = (1/odd1)+(1/odd2)+(1/odd3)
                if percentage < 1:
                    contPartidos = contPartidos+1
                    match = team1+" vs "+team2
                    percentage = percentage*100
                    percentage = 100-percentage

                    enviarPost(match, d1, team1, team2, odd1, odd2, odd3,
                           bookie1_id, bookie2_id, bookie3_id, percentage,today)
    print("bucle")

leer()
