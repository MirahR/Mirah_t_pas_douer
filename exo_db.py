import sqlite3

connexion = sqlite3.connect("school.db")
curseur = connexion.cursor()

###Exécution unique
curseur.execute('''CREATE TABLE IF NOT EXISTS 
                classroom(
                    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                    libelle TEXT NOT NULL,
                    taille TEXT)''')

curseur.execute('''CREATE TABLE IF NOT EXISTS 
                students( 
                    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, 
                    pseudo TEXT, 
                    valeur INTEGER, 
                    class_id INTEGER NOT NULL, FOREIGN KEY (class_id) REFERENCES classroom(id))''')

connexion.commit()


### Insertion d'une donnée
donnee = ("toto", 10000, 1)
curseur.execute('''INSERT INTO students (pseudo, valeur, class_id) VALUES (?, ?, ?)''',donnee)
connexion.commit()

### Insertion multiple de données
"""
donnees = (
{"psd" : "toto", "val" : 1000},
{"psd" : "tata", "val" : 750},
{"psd" : "titi", "val" : 500}
)
curseur.executemany("INSERT INTO students (pseudo,valeur, class_id) VALUES (:psd, :val, 1)", donnees)
connexion.commit()
"""

## Lire tout les items de la table
curseur.execute("SELECT * FROM students")
resultats = curseur.fetchall()
for resultat in resultats:
    print(resultat)
    
"""
# Sélectionner un item dans la DB via son pseudo
donnee = ("titi", )
curseur.execute("SELECT valeur FROM students WHERE pseudo = ?",donnee)
result = curseur.fetchone()
print(result)
while result:
    print(result)
    result = curseur.fetchone()
"""

task = ("pomme", 200, 2)
sql = ''' UPDATE students
        SET pseudo = ? ,
        valeur = ?
        WHERE id = ?'''
curseur.execute(sql, task)
connexion.commit()

curseur.execute('''INSERT INTO students (pseudo, valeur, class_id) VALUES (?, ?, ?)''',donnee)


## Supprimer un item dans la BD
def delete_item(id):
    curseur.execute(f'''DELETE FROM
    students WHERE id = {id}''')
    connexion.commit()
    print("Record deleted successfully")

delete_item(63)

connexion.close()