#coding: utf-8

j = 0 ### Je crée un compteur pour voir si ton script produit bien les 88000 numéros attendus

# Pour tous les matricules entre 1930 et 1999
for annee in range(30000,100000):
	j += 1 ### J'augmente mon compteur d'un permis à chacun qui est généré par cette boucle
	print(j, annee) ### J'ajoute mon compteur au numéro de permis affiché

# Le bogue de l'an 2000! — code pour les premières possibilités de l'an 2000
for annee in range(0, 10):
	j += 1 ### J'augmente mon compteur d'un permis à chacun qui est généré par cette boucle
	print(j, "0000{}" .format(annee)) ### J'ajoute mon compteur au numéro de permis affiché

# Pour tous les matricules après 00000-00009 entre 2000 et 2001
for annee in range(000,1000): ### L'erreur est dans cette ligne et la suivante
	j += 1 ### J'augmente mon compteur d'un permis à chacun qui est généré par cette boucle
	print(j, "00{}" .format(annee)) ### J'ajoute mon compteur au numéro de permis affiché

# Pour tous les matricules jusqu'à 2009
for annee in range (1000, 10000):
	j += 1 ### J'augmente mon compteur d'un permis à chacun qui est généré par cette boucle
	print(j, "0{}" .format(annee)) ### J'ajoute mon compteur au numéro de permis affiché

# Pour tous les matricules entre 2010 et 2017    
for annee in range (10000, 18000):
	j += 1 ### J'augmente mon compteur d'un permis à chacun qui est généré par cette boucle
	print(j, annee) ### J'ajoute mon compteur au numéro de permis affiché

### Mes commentaires sont précédés de trois # pour les distinguer des tiens :)

### Solution intéressante. Y aller successivement peut fonctionner.
### Ton script règle en partie le bogue de l'an 2000.
### Il fonctionne entre les numéros 00000 et 00009.
### Après, cependant, il y a un problème. Ton script écrit des numéros de 3 chiffres (000 à 009), puis de quatre (0010 à 0099)
### Au final, il y a 10 numéros de permis de trop.
