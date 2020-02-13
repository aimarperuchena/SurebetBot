import urllib.request
import pymysql
import urlopen
import request
import requests
from bs4 import BeautifulSoup
from datetime import date
import datetime
from urllib.request import Request, urlopen


def enviarPost(match, fecha, team1, team2, odd1, odd2, odd3, bookie1, bookie2, bookie3, percentage, country, sport, league):
    today = date.today()

    url = 'http://192.168.0.12:1234/api/surebet'
    objeto = {'match': match, 'date': fecha, 'team1': team1, 'team2': team2, 'odd1': odd1, 'odd2': odd2,
              'odd3': odd3, 'bookie1': bookie1, 'bookie2': bookie2, 'bookie3': bookie3, 'percentage': percentage, 'country': country, 'sport': sport, 'league': league}
    x = requests.post(url, data=objeto)
    print(x.text)
    if len(x.text) > 0:
        print('----------------------------' +
              bookie1+'------------------------')
        print('----------------------------' +
              bookie2+'------------------------')
        print('----------------------------' +
              str(bookie3)+'------------------------')


'''FUTBOL 3 OPCIONES'''


def leerFutbolLigas():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    req = Request(
        url='https://www.centroapuesta.com/apuestas/futbol/espana/laliga/', headers=headers)
    html = urlopen(req).read()
    soup2 = BeautifulSoup(html)
    content = soup2.find("div", {"id": "content"})
    menu_apuestas_deportes = content.find(
        "div", {"id": "menu-apuestas-deportes"})
    sports_menu = menu_apuestas_deportes.find("nav", {"class": "sports-menu"})
    ul = sports_menu.find("ul")
    '''SPORTS'''
    li = ul.find("li", {"class": "futbol"})
    ul = li.find("ul")
    '''COUNTRIES'''
    lis = ul.findAll("li")
    for li in lis:
        ul = li.find("ul")
        if ul is not None:
            links = ul.findAll('a')
            for link in links:

                cuotasFutbol(link["href"])


def cuotasFutbol(link):

    arrayLink = link.split("/")

    sport = arrayLink[5]
    country = arrayLink[4]
    league = arrayLink[6]

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

    req = Request(
        url=link, headers=headers)
    html = urlopen(req).read()
    soup2 = BeautifulSoup(html)

    content = soup2.find("div", {"id": "content"})
    main_column = content.find("div", {"class": "main-column"})
    article = main_column.find("article")
    matches_table = article.find("table")
    tbody = matches_table.find("tbody")
    trs = tbody.findAll("tr")
    for tr in trs:
        tds = tr.findAll("td")
        cont = 0
        fecha = ''
        hora = ''
        match = ''
        cuota1 = 0
        cuota2 = 0
        cuota3 = 0
        casa1 = ''
        casa2 = ''
        casa3 = ''
        for td in tds:

            if cont == 0:
                fecha = td.find("span", {"class": "date"})
                hora = td.find("span", {"class": "time"})
                if fecha is not None:
                    fecha = fecha.text
                    hora = hora.text

            if cont == 1:
                partido = td.find("a")
                if partido is not None:
                    match = partido.text.strip()

            if cont == 2:
                cuota1 = td.find("span")
                if cuota1 is not None:
                    casa1 = td.find("img")
                    cuota1 = float(cuota1.text)
                    casa1 = casa1["alt"]

            if cont == 3:
                cuota2 = td.find("span")
                if cuota2 is not None:
                    casa2 = td.find("img")
                    cuota2 = float(cuota2.text)
                    casa2 = casa2["alt"]
            if cont == 4:
                cuota3 = td.find("span")
                if cuota3 is not None:
                    casa3 = td.find("img")
                    cuota3 = float(cuota3.text)
                    casa3 = casa3["alt"]
            if cuota1 is not None and cuota2 is not None and cuota3 is not None:
                if cuota1 > 0 and cuota2 > 0 and cuota3 > 0:
                    percentage = (1/cuota1)+(1/cuota2)+(1/cuota3)
                    arrayFecha = fecha.split(" ")
                    mes = 0
                    dia = 0
                    ano = 0

                    if arrayFecha[1] == "Feb":
                        mes = "02"
                    dia = int(arrayFecha[0].replace(",", ""))
                    ano = int(arrayFecha[2])
                    fecha = str(ano)+"-"+str(mes)+"-"+str(dia)+" "+str(hora)
                    equipoarray = match.split(" — ")
                    team1 = equipoarray[0]
                    team2 = equipoarray[1]
                    odd1 = cuota1
                    odd2 = cuota2
                    odd3 = cuota3
                    bookie1 = casa1
                    bookie2 = casa2
                    bookie3 = casa2

                    if bookie1 == "William Hill":
                        bookie1 = "WilliamHill"
                    if bookie2 == "William Hill":
                        bookie2 = "WilliamHill"
                    if bookie3 == "William Hill":
                        bookie3 = "WilliamHill"
                    enviarPost(match, fecha, team1, team2, odd1, odd2, odd3,
                               bookie1, bookie2, bookie3, percentage, sport, country, league)
            cont = cont+1


'''TENIS'''


def leerTenisLigas():

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

    req = Request(
        url='https://www.centroapuesta.com/apuestas/futbol/espana/laliga/', headers=headers)
    html = urlopen(req).read()
    soup2 = BeautifulSoup(html)

    content = soup2.find("div", {"id": "content"})
    menu_apuestas_deportes = content.find(
        "div", {"id": "menu-apuestas-deportes"})
    sports_menu = menu_apuestas_deportes.find("nav", {"class": "sports-menu"})
    ul = sports_menu.find("ul")
    '''SPORTS'''
    li = ul.find("li", {"class": "tenis"})
    ul = li.find("ul")
    '''COUNTRIES'''
    lis = ul.findAll("li")
    for li in lis:
        ul = li.find("ul")
        if ul is not None:

            links = ul.findAll('a')
            for link in links:
                cuotasTenis(link["href"])


def cuotasTenis(link):
    arrayLink = link.split("/")

    sport = arrayLink[5]
    country = arrayLink[4]
    league = arrayLink[6]

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

    req = Request(
        url=link, headers=headers)
    html = urlopen(req).read()
    soup2 = BeautifulSoup(html)

    content = soup2.find("div", {"id": "content"})
    main_column = content.find("div", {"class": "main-column"})
    article = main_column.find("article")
    matches_table = article.find("table")
    tbody = matches_table.find("tbody")
    trs = tbody.findAll("tr")
    for tr in trs:
        tds = tr.findAll("td")
        cont = 0
        fecha = ''
        hora = ''
        match = ''
        cuota1 = 0
        cuota2 = 0
        cuota3 = 0
        casa1 = ''
        casa2 = ''
        casa3 = ''
        for td in tds:

            if cont == 0:
                fecha = td.find("span", {"class": "date"})
                hora = td.find("span", {"class": "time"})
                if fecha is not None:
                    fecha = fecha.text
                    hora = hora.text

            if cont == 1:
                partido = td.find("a")
                if partido is not None:
                    match = partido.text.strip()

            if cont == 2:
                cuota1 = td.find("span")
                if cuota1 is not None:
                    casa1 = td.find("img")
                    cuota1 = float(cuota1.text)
                    casa1 = casa1["alt"]

            if cont == 3:
                cuota2 = td.find("span")
                if cuota2 is not None:
                    casa2 = td.find("img")
                    cuota2 = float(cuota2.text)
                    casa2 = casa2["alt"]

            if cuota1 is not None and cuota2 is not None:
                if cuota1 > 0 and cuota2 > 0:
                    percentage = (1/cuota1)+(1/cuota2)
                    arrayFecha = fecha.split(" ")
                    mes = 0
                    dia = 0
                    ano = 0

                    if arrayFecha[1] == "Feb":
                        mes = "02"
                    dia = int(arrayFecha[0].replace(",", ""))
                    ano = int(arrayFecha[2])
                    fecha = str(ano)+"-"+str(mes)+"-"+str(dia)+" "+str(hora)
                    equipoarray = match.split(" — ")
                    team1 = equipoarray[0]
                    team2 = equipoarray[1]
                    odd1 = cuota1
                    odd2 = cuota2

                    bookie1 = casa1
                    bookie2 = casa2

                    if bookie1 == "William Hill":
                        bookie1 = "WilliamHill"
                    if bookie2 == "William Hill":
                        bookie2 = "WilliamHill"
                    
                    enviarPost(match, fecha, team1, team2, odd1, odd2, None,
                               bookie1, bookie2, None, percentage, sport, country, league)
            cont = cont+1



def leerBaloncestoLigas():
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

    req = Request(
        url='https://www.centroapuesta.com/apuestas/futbol/espana/laliga/', headers=headers)
    html = urlopen(req).read()
    soup2 = BeautifulSoup(html)

    content = soup2.find("div", {"id": "content"})
    menu_apuestas_deportes = content.find(
        "div", {"id": "menu-apuestas-deportes"})
    sports_menu = menu_apuestas_deportes.find("nav", {"class": "sports-menu"})
    ul = sports_menu.find("ul")
    '''SPORTS'''
    li = ul.find("li", {"class": "baloncesto"})
    ul = li.find("ul")
    '''COUNTRIES'''
    lis = ul.findAll("li")
    for li in lis:
        ul = li.find("ul")
        if ul is not None:

            links = ul.findAll('a')
            for link in links:
                cuotasBaloncesto(link["href"])


def cuotasBaloncesto(link):
    arrayLink = link.split("/")

    sport = arrayLink[5]
    country = arrayLink[4]
    league = arrayLink[6]

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

    req = Request(
        url=link, headers=headers)
    html = urlopen(req).read()
    soup2 = BeautifulSoup(html)

    content = soup2.find("div", {"id": "content"})
    main_column = content.find("div", {"class": "main-column"})
    article = main_column.find("article")
    matches_table = article.find("table")
    tbody = matches_table.find("tbody")
    trs = tbody.findAll("tr")
    for tr in trs:
        tds = tr.findAll("td")
        cont = 0
        fecha = ''
        hora = ''
        match = ''
        cuota1 = 0
        cuota2 = 0
        cuota3 = 0
        casa1 = ''
        casa2 = ''
        casa3 = ''
        for td in tds:

            if cont == 0:
                fecha = td.find("span", {"class": "date"})
                hora = td.find("span", {"class": "time"})
                if fecha is not None:
                    fecha = fecha.text
                    hora = hora.text

            if cont == 1:
                partido = td.find("a")
                if partido is not None:
                    match = partido.text.strip()

            if cont == 2:
                cuota1 = td.find("span")
                if cuota1 is not None:
                    casa1 = td.find("img")
                    cuota1 = float(cuota1.text)
                    casa1 = casa1["alt"]

            if cont == 3:
                cuota2 = td.find("span")
                if cuota2 is not None:
                    casa2 = td.find("img")
                    cuota2 = float(cuota2.text)
                    casa2 = casa2["alt"]

            if cuota1 is not None and cuota2 is not None:
                if cuota1 > 0 and cuota2 > 0:
                    percentage = (1/cuota1)+(1/cuota2)
                    arrayFecha = fecha.split(" ")
                    mes = 0
                    dia = 0
                    ano = 0

                    if arrayFecha[1] == "Feb":
                        mes = "02"
                    dia = int(arrayFecha[0].replace(",", ""))
                    ano = int(arrayFecha[2])
                    fecha = str(ano)+"-"+str(mes)+"-"+str(dia)+" "+str(hora)
                    equipoarray = match.split(" — ")
                    team1 = equipoarray[0]
                    team2 = equipoarray[1]
                    odd1 = cuota1
                    odd2 = cuota2

                    bookie1 = casa1
                    bookie2 = casa2

                    if bookie1 == "William Hill":
                        bookie1 = "WilliamHill"
                    if bookie2 == "William Hill":
                        bookie2 = "WilliamHill"
                    
                    enviarPost(match, fecha, team1, team2, odd1, odd2, None,
                               bookie1, bookie2, None, percentage, sport, country, league)
            cont = cont+1


leerFutbolLigas()
leerTenisLigas()
leerBaloncestoLigas()