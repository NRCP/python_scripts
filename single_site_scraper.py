#Benötigte Module importerien
import requests
import datetime
import csv
from pathlib import Path
from bs4 import BeautifulSoup

#Headerinformationen für die Webabfrage definieren
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/31.0'
}

url = 'https://example.com/'

#Webseite die abgefragt werden soll wird definiert
page = requests.get(url, headers=headers)

#Aktuelles Datum der Abfrage nach dem Schema YYYY-mm-dd
now = datetime.datetime.now().strftime("%Y-%m-%d")

#Website aufrufen
soup = BeautifulSoup(page.text, 'html.parser')

#Seiten Titel bestimmen
site_title = soup.title.string

#Pfad und Name der CSV Datei
filename = 'filename.csv'   #Dateiname definieren mit dem Prefix .csv
filepath = '/path/to/file/' #Pfad zur Datei

file = filepath + filename

fieldnames = ['Date', 'Site', 'Titel', 'URL', 'ID','Content']

csv_file = Path(file)

# Überprüfen pb die Datei schon existiert. Wenn die Datei noch nicht vorhanden ist wird diese erstellt und der Header geschrieben.
if csv_file.is_file() == False:
    csvfile = open(file, 'w', newline='', encoding='utf-8')
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
     
    writer.writeheader()

    csvfile.close

with open(file, 'a', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
    
    for c in soup.find_all('article', class_='et_pb_post'):
        
        writer.writerow({'Date': now, 'Site': site_title, 'Titel': c.h2.string, 'URL': c.a.get('href'), 'Conten': c.div.p.string})
    
    csvfile.close