#coding: utf-8

# Pour tous les matricules entre 1930 et 1999
for annee in range(30000,100000):
    print(annee)

# Le bogue de l'an 2000! — code pour les premières possibilités de l'an 2000
for annee in range(0, 10):
    print("0000{}" .format(annee))

# Pour tous les matricules après 00000-00009 entre 2000 et 2001
for annee in range(000,1000):
    print("00{}" .format(annee))

# Pour tous les matricules jusqu'à 2009
for annee in range (1000, 10000):
    print("0{}" .format(annee))

# Pour tous les matricules entre 2010 et 2017    
for annee in range (10000, 18000):
    print(annee)