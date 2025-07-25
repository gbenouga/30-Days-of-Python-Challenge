# «Jour2: 30 Days of Python Programming»


# prenom, = "Laurent"
# nom_de_famille = "Dupont"
# nom_complet = prenom + " " + nom_de_famille
# pays = "Togo"
# municipale = pays
# an = 2025
# is_true = True
# is_light = False


from numpy import divide, multiply, subtract
import keyword

prenom, nom_de_famille, nom_complet, pays, municipale, an, is_true, is_light = "Laurent", "Dupont", "Laurent Dupont", "Togo", "Togo", 2025, True, False

# 1. Vérification des types de données
print(type(prenom))
print(type(nom_de_famille))
print(type(nom_complet))
print(type(pays))
print(type(municipale))
print(type(an))
print(type(is_true))
print(type(is_light))

# 2. Longueur du prénom
print("Longueur du prénom :", len(prenom))

# 3. Comparaison des longueurs
print("Longueur du prénom :", len(prenom))
print("Longueur du nom de famille :", len(nom_de_famille))
if len(prenom) > len(nom_de_famille):
    print("Le prénom est plus long que le nom de famille.")
elif len(prenom) < len(nom_de_famille):
    print("Le nom de famille est plus long que le prénom.")
else:
    print("Le prénom et le nom de famille ont la même longueur.")

# 4. Déclaration des nombres
num_one = 5
num_two = 4

# 5. Addition
somme = sum([num_one, num_two])

# 6. Soustraction
difference = subtract(num_one, num_two)

# 7. Multiplication
produit = multiply(num_one, num_two)

# 8. Division
division = divide(num_one, num_two)
# 9. Modulo
reste = num_one % num_two

# 10. Floor Division
floor_division = num_one // num_two

# Affichage des résultats
print("Somme :", somme)
print("Différence :", difference)
print("Produit :", produit)
print("Division :", division)
print("Reste :", reste)
print("Floor Division :", floor_division)


import math
# ...existing code...

# 12. Calculs sur le cercle
rayon = 30
area_of_circle = 3.14 * rayon ** 2
circum_of_circle = 2 * 3.14 * rayon

print("Aire du cercle :", area_of_circle)
print("Circonférence du cercle :", circum_of_circle)

# iii. Prendre le rayon comme entrée utilisateur et calculer l'aire
rayon_user = float(input("Entrez le rayon du cercle : "))
aire_user = 3.14 * rayon_user ** 2
print("Aire du cercle avec le rayon saisi :", aire_user)

# 13. Entrée utilisateur pour prénom, nom de famille, pays et âge
prenom_user = input("Entrez votre prénom : ")
nom_de_famille_user = input("Entrez votre nom de famille : ")
pays_user = input("Entrez votre pays : ")
age_user = input("Entrez votre âge : ")

print("Informations utilisateur :")
print("Prénom :", prenom_user)
print("Nom de famille :", nom_de_famille_user)
print("Pays :", pays_user)
print("Âge :", age_user)

# 14. Afficher les mots clés réservés Python
print("**********************************************************************************************")
print("Mots clés réservés Python :", keyword.kwlist)

