import sqlite3

connexion = sqlite3.connect("classe.db")
curseur = connexion.cursor()

###Exécution unique
curseur.execute('''CREATE TABLE IF NOT EXISTS classe (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE
                nom TEXT,
                moyenne INTEGER)''')


curseur.execute('''CREATE TABLE IF NOT EXISTS student (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, FOREIGN KEY (id) REFERENCES classe(id)
                nom TEXT,
                date de naissance TEXT,
                note INTEGER)''')



connexion.commit()



connexion.close()