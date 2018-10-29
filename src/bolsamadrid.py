import whois
import requests
import os
from bs4 import BeautifulSoup

#Whois bolsamadrid.es
#print(whois.whois('bolsamadrid.es'))
wh=str(whois.whois('bolsamadrid.es'))

f=open("whois.txt","w")
f.write(wh)
f.close()

#esta es la pagina a la que vamos a hacer scraping
page=requests.get('http://www.bolsamadrid.es/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000')

#Contenido de la pagina
soup=BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())
rqt=soup.prettify()
f=open("request.html","w")
f.write(rqt)
f.close()

#contenido de la tabla con las acciones 
table = soup.find_all('table', {'id':'ctl00_Contenido_tblAcciones'})

#print(table)
#Iniciamos variables
columnas=0
cabecera=""
cotizacion=""
n=0

for contador in  soup.find_all('table', {'id':'ctl00_Contenido_tblAcciones'}):
    for column in contador.find_all('th'):
                   if(column!=contador.find_all('th')):
                       cabecera=cabecera+column.text+";"
                       columnas=columnas+1;



  
for column2 in contador.find_all('td'):
        cotizacion=cotizacion+column2.text
        n=n+1
            #print(column2.text+","
        if (n==columnas):
            cotizacion=cotizacion+"\n"
            #print (cotizacion)
            n=0
        else:
            cotizacion=cotizacion+";"
cabecera=cabecera.rstrip(';')
print(cabecera)        
print(cotizacion)      



f=open("cotizacionIBEX35.csv","w")
f.write(cabecera+"\n"+cotizacion)
f.close()


     
print("Fin practica")
