### Exercice 1
# 1. Créer un tuple vide
empty_tuple = ()

# 2. Tuple avec les prénoms des sœurs et frères
soeurs = ("Nina", "Lola")
freres = ("Laurent", "Lionel")

# 3. Joindre les tuples frères et sœurs
print("****************************************************")
siblings = soeurs + freres
print("les tuples frères et sœurs :", siblings)

# 4. Nombre de frères et sœurs
print("****************************************************")
print("Nombre de frères et sœurs :", len(siblings))

# 5. Ajouter le père et la mère
print("****************************************************")
family_members = siblings + ("Goku", "Chichi")
print("Membres de la famille :", family_members)

### Exercice 2
# Déballer siblings et parents
print("****************************************************")
siblings = family_members[:len(siblings)]
parents = family_members[len(siblings):]
print("Siblings :", siblings)
print("les noms des parents :", parents)

# 2. Créer les tuples fruits, légumes et produits animaux
fruits = ("mangue", "papaye", "orange")
vegetables = ("epices", "tomate", "poivron")
animal_products = ("lait", "oeuf", "fromage")

# . Joindre les trois tuples en un seul
print("****************************************************")
food_stuff_tp = fruits + vegetables + animal_products
print("food_stuff_tp :", food_stuff_tp)

# 3. Convertir le tuple en liste
print("****************************************************")
food_stuff_lt = list(food_stuff_tp)
print("food_stuff_lt :", food_stuff_lt)

# 4. Extraire l’élément ou les éléments du milieu
print("****************************************************")
n = len(food_stuff_lt)
if n % 2 == 1:
    print("L'élement se trouvant au milieu :", food_stuff_lt[n // 2])
else:
    print("les Elements se trouvant au milieu :", food_stuff_lt[n // 2 - 1 : n // 2 + 1])

# 5. Extraire les 3 premiers et 3 derniers éléments
print("****************************************************")
print("3 premiers :", food_stuff_lt[:3])
print("3 derniers :", food_stuff_lt[-3:])

# 6. Supprimer complètement le tuple
del food_stuff_tp

# 7. Vérifier si un élément existe dans le tuple nordic_countries
print("****************************************************")
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("'Estonia' est un pays nordique :", 'Estonia' in nordic_countries)
print("'Iceland' est un pays nordique :", 'Iceland' in nordic_countries)