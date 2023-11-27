import csv
import json
import mysql.connector as mc

# Settings
dbh = "127.0.0.1"
dbu = "root"
dbpw = "#6eo#6eo"
dbSchema = "Tema_20"
carTable = "Masini"

csvFile = "../curs17/masini.csv"

dbcon = mc.connect(host=dbh, user=dbu, password=dbpw, database=dbSchema)
c = dbcon.cursor()



# creati o tabela SQL care sa aiba aceeasi structura cu fisierul pe care l-am descarcat acum cateva saptamani de pe site-ul ins (cel cu masinile)
"""CREATE SCHEMA IF NOT EXISTS `Tema_20`;"""

"""CREATE TABLE `Tema_20`.`Masini` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `Judet` VARCHAR(20) NULL,
  `Categorie_Nationala` VARCHAR(30) NULL,
  `Categorie_Comunitara` VARCHAR(5) NULL,
  `Marca` VARCHAR(20) NULL,
  `Descriere_Comerciala` VARCHAR(20) NULL,
  `Combustibil` VARCHAR(15) NULL,
  `Nr_Vehicule` INT UNSIGNED NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE);"""


def csvToDictList(infile) -> list:
    f = open(infile, "r", encoding="utf-8-sig")
    reader = csv.DictReader(f, dialect="excel")
    entries = []
    
    for row in reader:
        entries.append(row)

    f.close()
    return entries

# scrieti o functie care parcurge acel fisier si insereaza in baza de date fiecare inregistrare din tabela
def transferCsvRowsToDb(infile):
    data = csvToDictList(infile)
    for d in data:
        c.execute(f"INSERT INTO {carTable} (Judet, Categorie_Nationala, Categorie_Comunitara, Marca, Descriere_Comerciala, Combustibil, Nr_Vehicule) VALUES ({repr(d['JUDET'])}, {repr(d['CATEGORIE_NATIONALA'])}, {repr(d['CATEGORIE_COMUNITARA'])}, {repr(d['MARCA'])}, {repr(d['DESCRIERE_COMERCIALA'])}, {repr(d['VALUE_NAME'])}, {repr(d['TOTAL_VEHICULE'])});")
    
    dbcon.commit()



# odata completata tabela, scrieti functii sql (scrieti-le ca functii python) care calculeaza: 
#afisari:
    #afiseaza toate masinile dintr-un judet anume 
    #afiseaza toate masinile dintr-o categorie anume 
    #afiseaza toate masinile care sunt mai multe de 10 
def getCarsFromCounty(county):
    c.execute(f"SELECT * FROM {carTable} WHERE `Judet` = '{county}'")
    return c.fetchall()



def getCarsFromCategory(category):
    c.execute(f"SELECT * FROM {carTable} WHERE `Categorie_Nationala` = '{category}'")
    return c.fetchall()



def getMoreCarsThan(numero):
    c.execute(f"SELECT * FROM {carTable} WHERE `Nr_vehicule` > {numero}")
    return c.fetchall()



#conversii 
    #converteste fisierul din csv in json 
    #converteste fisierul in fisier text unde fiecare linie este de tipul "Vehicul de tip <CATEGORIE_NATIONALA> din judetul <JUDET> marca <MARCA>: <TOTALVEHICULE> <TOTAL
    #converteste un fisier json primit ca parametru in fisier csv (pe caz general)
def csvToJson(infile, outfile):
    data = csvToDictList(infile)
    jsonObj = json.dumps(data, )

    j = open(outfile, "w")
    j.write(jsonObj)
    j.close()



def csvToTxt(infile, outfile):
    data = csvToDictList(infile)
    tfile = open(outfile, "w")
    redata = {}

    for d in data:
        if d["JUDET"] in redata:
            if d["CATEGORIE_NATIONALA"] in redata[d["JUDET"]]:
                if d["MARCA"] in redata[d["JUDET"]][d["CATEGORIE_NATIONALA"]]:
                    redata[d["JUDET"]][d["CATEGORIE_NATIONALA"]][d["MARCA"]] += int(d["TOTAL_VEHICULE"])
                else:
                    redata[d["JUDET"]][d["CATEGORIE_NATIONALA"]][d["MARCA"]] = int(d["TOTAL_VEHICULE"])
            else:
                redata[d["JUDET"]][d["CATEGORIE_NATIONALA"]] = {}
        else:
            redata[d["JUDET"]] = {}

    for jud in redata:
        for cat in redata[jud]:
            for m in redata[jud][cat]:
                tfile.write(f"Vehicul de tip {cat} din judetul {jud} marca {m}: {redata[jud][cat][m]}\n")
    tfile.close()



def jsonToCsv(inFile, outfile):
    j = open(inFile, "r")
    c = open(outfile, "w")
    indata = json.load(j)
    headers = list(indata[0].keys())
    outdata = csv.DictWriter(c, fieldnames=headers)

    outdata.writeheader()
    outdata.writerows(indata)

    c.close()
    j.close()



#calcule
    #calculeaza numarul total de masini din tara 
    #calculeaza numarul total de masini dintr-un judet primit ca parametru
    #calculeaza numarul total de masini dintr-o anumita categorie nationala 
    #calculeaza numarul total de masini in functie de tipul de combustibil pe care il folosesc
def totalCars() -> int:
    return 0



def totalInCounty(county) -> int:
    return 0 



def totalInCategory(category) -> int:
    return 0



def totalByFuel(fuel) -> int:
    return 0



#modificare 
   #modificati valorile a.i. toate intrarile care contin denumirea benzina sa ramana cu valoarea benzina 
   #modificati valorile a.i. in locul judetelor "dolj","olt","gorj","valcea","mehedinti" sa apara oltenia 
   #adaugati o coloana care sa contina valoarea "popular" sau "nepopular" in functie de nr de vehicule din acea categorie (un vehicul e popular daca exista mai mult de 100)
def setFuelToGas():
    pass


def changeToOltenia():
    pass


def addPopularColumn():
    pass


#cleanup
c.close()
dbcon.close()