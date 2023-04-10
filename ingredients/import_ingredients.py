import mysql.connector
import csv

# se connecter à la base de données
cnx = mysql.connector.connect(user='usename', password='password', host='localhost', database='dbname')
cursor = cnx.cursor()

# créer la table Ingredients
cursor.execute("CREATE TABLE Ingredients ("
                "IdIngredient INT NOT NULL AUTO_INCREMENT, "
               "IngredientNameFR VARCHAR(255), "
               "IngredientSynonymFR VARCHAR(255), "
               "CategoryFR VARCHAR(255), "
               "ContituentIngredientsFR VARCHAR(255), "
               "PRIMARY KEY (IdIngredient))"
               )

# importer les données du fichier CSV Ingredients
with open('IngredientsFR.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=';')
    next(csvreader)  # sauter la première ligne (en-tête)
    for row in csvreader:
        if len(row) == 5: # vérifier le nombre de colonnes
            cursor.execute("INSERT INTO Ingredients ("
                           "IngredientNameFR, IngredientSynonymFR, "
                           "CategoryFR, ContituentIngredientsFR) "
                           "VALUES (%s, %s, %s, %s)",
                           (row[0], row[1], row[2], row[3]))
cnx.commit() # sauvegarder les changements dans la base de données
cursor.close() # fermer le curseur
cnx.close() # fermer la connexion à la base de données