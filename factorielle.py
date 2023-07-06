def facto(nb):
    if nb == 1:
        return 1
    else:
        return nb*facto(nb-1)
    


nb = int(input("Entrer un nombre : "))
print(facto(nb))