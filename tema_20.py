import csv
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
# odata completata tabela, scrieti functii sql (scrieti-le ca functii python) care calculeaza: 


#afisari:
    #afiseaza toate masinile dintr-un judet anume 
    #afiseaza toate masinile dintr-o categorie anume 
    #afiseaza toate masinile care sunt mai multe de 10 


#conversii 
    #converteste fisierul din csv in json 
    #converteste fisierul in fisier text unde fiecare linie este de tipul "Vehicul de tip <CATEGORIE_NATIONALA> din judetul <JUDET> marca <MARCA>: <TOTALVEHICULE> <TOTAL
    #converteste un fisier json primit ca parametru in fisier csv (pe caz general)


#calcule
    #calculeaza numarul total de masini din tara 
    #calculeaza numarul total de masini dintr-un judet primit ca parametru
    #calculeaza numarul total de masini dintr-o anumita categorie nationala 
    #calculeaza numarul total de masini in functie de tipul de combustibil pe care il folosesc


#modificare 
   #modificati valorile a.i. toate intrarile care contin denumirea benzina sa ramana cu valoarea benzina 
   #modificati valorile a.i. in locul judetelor "dolj","olt","gorj","valcea","mehedinti" sa apara oltenia 
   #adaugati o coloana care sa contina valoarea "popular" sau "nepopular" in functie de nr de vehicule din acea categorie (un vehicul e popular daca exista mai mult de 100)