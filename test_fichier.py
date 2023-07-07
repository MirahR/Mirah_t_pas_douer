# écrire dans fichier
import json

if __name__=='__main__':
    fichier1 = open("file.txt", "w+")
    if fichier1 :
        print("votre fichier est ouvert")
        fichier1.write("test")
        fichier1.close()
        # lire le contenu d'un fichier
        f = open("file.txt", "r")
        print(f.read())
        print(f.readline())
        f.close()



    with open('my-file.json', 'r') as file:
        data = json.load(file)
        print(data)