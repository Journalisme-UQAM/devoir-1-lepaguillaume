#coding: utf-8

# Pour tous les matricules entre 1930 et 1999
annee1 = [format(annee1) for annee1 in range(30000, 100000)]

# Pour tous les matricules entre 2000 et 2017
annee2 = ["{:05d}".format(annee2) for annee2 in range(0, 18000)]

#On imprime les deux chaînes l'une après l'autre
print(annee1, annee2)