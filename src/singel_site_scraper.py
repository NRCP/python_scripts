#Benötigte Module importerien
import requests
import datetime
import csv
from bs4 import BeautifulSoup

#Headerinformationen für die Webabfrage definieren
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/31.0'
}

#Webseite die abgefragt werden soll wird definiert
page = requests.get('https://example.com/', headers=headers)

#Aktuelles Datum der Abfrage nach dem Schema YYYY-mm-dd
now = datetime.datetime.now().strftime("%Y-%m-%d")

#Website aufrufen
soup = BeautifulSoup(page.text, 'html.parser')

#Seiten Titel bestimmen
site_title = soup.title.string

with open('/path/filename.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Date', 'Site', 'Titel', 'URL', 'Conten']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
   
    writer.writeheader()
    
    for c in soup.find_all('article', class_='et_pb_post'):
        
        writer.writerow({'Date': now, 'Site': site_title, 'Titel': c.h2.string, 'URL': c.a.get('href'), 'Conten': c.div.p.string})
    
    csvfile.close