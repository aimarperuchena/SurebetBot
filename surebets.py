import urllib.request
import pymysql
import urlopen
import request
from bs4 import BeautifulSoup
from datetime import date
import datetime 
from urllib.request import Request, urlopen
today = date.today()
tomorrow = today + datetime.timedelta(days = 1) 
d1 = today.strftime("%d-%m-%Y")
d2=tomorrow.strftime("%d-%m-%Y")
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(
    url='http://www.elcomparador.com/futbol/'+str(d2), headers=headers)
html = urlopen(req).read()
soup2 = BeautifulSoup(html)
contSurebets = 0
contPartidos=0


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

    nombre1 = ''
    nombre2 = ''
    cuota1 = 0
    cuota2 = 0
    cuota3 = 0
    casa1=''
    casa2=''
    casa3=''
    codCasa=0
    codCasa1=0
    codCasa2=0
    codCasa3=0
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
                a_link=celda_cuotas.find('a')
                casa=''
                link=a_link['href']
                if "bet365" in link:
                    casa="bet365"
                    codCasa=1
                if "codere" in link:
                    casa="codere"
                    codCasa=2
                if "bwin" in link:
                    casa="bwin"
                    codCasa=3
                if "marathonbet" in link:
                    casa="marathon bet"
                    codCasa=4
                if "luckia" in link:
                    casa="luckia"
                    codCasa=5
                if "sportium" in link:
                    casa="sportium"
                    codCasa=6
                if "betway" in link:
                    casa="betway"
                    codCasa=7
                if "marcaapuestas" in link:
                    casa="marca apuestas"
                    codCasa=8
                if "willhill" in link:
                    casa="william hill"
                    codCasa=9
                if "sport888" in link:
                    casa="888 sport"
                    codCasa=10
                if "betfair" in link:
                    casa="betfair"
                    codCasa=11
                if "interwetten" in link:
                    casa="interwetten"
                    codCasa=12   
                
                if contCuota == 0:
                    cuota1 = float(celda_cuotas.text)
                    casa1=casa
                    codCasa1=codCasa
                if contCuota == 1:
                    cuota2 = float(celda_cuotas.text)
                    casa2=casa
                    codCasa2=codCasa
                if contCuota == 2:
                    cuota3 = float(celda_cuotas.text)
                    casa3=casa
                    codCasa3=codCasa
                contCuota = contCuota+1

                
                
    ''' fila_cuotas = contenedor_cuotas.find("div", {"id": "fila_cuotas"}) '''
    ''' for cuota in fila_cuotas:
        cuota_span = cuota.find("a", {"class": "verde"})
        print(cuota_span.text) '''
    for equipo in franja_equipos:
        if contNombre == 0:
            nombre1 = equipo.text
        if contNombre == 1:
            nombre2 = equipo.text
        contNombre = contNombre+1
        

    if hora_text != '':
        if cuota1 != 0 and cuota2 != 0 and cuota3 != 0:
            contPartidos=contPartidos+1
            surebets = (1/cuota1)+(1/cuota2)+(1/cuota3)
            if surebets < 1:
                
                contSurebets = contSurebets+1
                surebets = surebets*100
                surebets = 100-surebets
                
                print("Partido: "+nombre1+" vs "+nombre2)
                print('Hora: '+hora_text)
                print(casa1+": "+str(cuota1))
                print(casa2+": "+str(cuota2))
                print(casa3+": "+str(cuota3))
                print("Surebet: "+str(surebets))
                print('-------------------')
print("Partidos: "+str(d1)+" "+str(contPartidos))


