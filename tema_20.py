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



# scrieti o functie care parcurge acel fisier si insereaza in baza de date fiecare inregistrare din tabela
def transferCsvRowsToDb(csvFile):
    f = open(csvFile, "r", encoding="utf-8-sig")
    reader = csv.DictReader(f, dialect="excel")

    for row in reader:
        c.execute(f"INSERT INTO {carTable} (Judet, Categorie_Nationala, Categorie_Comunitara, Marca, Descriere_Comerciala, Combustibil, Nr_Vehicule) VALUES ({repr(row['JUDET'])}, {repr(row['CATEGORIE_NATIONALA'])}, {repr(row['CATEGORIE_COMUNITARA'])}, {repr(row['MARCA'])}, {repr(row['DESCRIERE_COMERCIALA'])}, {repr(row['VALUE_NAME'])}, {repr(row['TOTAL_VEHICULE'])});")
    
    dbcon.commit()
    f.close()



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
    pass



def csvToTxt(infile, outfile):
    pass



def jsonToCsv(inFile, outfile):
    pass



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