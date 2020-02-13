import urllib.request
import pymysql
import urlopen
import request
import requests
from bs4 import BeautifulSoup
from datetime import date
import datetime
from urllib.request import Request, urlopen

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(
    url='https://www.centroapuesta.com/apuestas/futbol/espana/laliga/', headers=headers)
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
    partido=''
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
                fecha=fecha.text
                hora=hora.text

        if cont == 1:
            partido = td.find("a")
            if partido is not None:
                partido=partido.text.strip()
             

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
        if cuota1>0 and cuota2>0 and cuota3>0:
            percentage = (1/cuota1)+(1/cuota2)+(1/cuota3)
           
            
            arrayFecha=fecha.split(" ")
            mes=0
            dia=0
            ano=0
           
            if arrayFecha[1]=="Feb":
                mes="02"
            dia=int(arrayFecha[0].replace(",",""))
            ano=int(arrayFecha[2])
            fecha=str(ano)+"-"+str(mes)+"-"+str(dia)+" "+str(hora)
            print(casa1)
            print(casa2)
            print(casa3)
            print(fecha)
        cont = cont+1
