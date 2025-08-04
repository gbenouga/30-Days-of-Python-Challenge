# Day 13 : Liste Comprehension - Exercices
print("***********************Liste Comprehension******************************")


# 1. Filtre seulement les nombres négatifs et zéro
print("1. Filtre les nombres négatifs et zéro:")
nombres = [-4, -3, -2, -1, 0, 2, 4, 6]
print(f"Voici la liste originale : {nombres}")
# Après filtre
negative_and_zero = [num for num in nombres if num <= 0]
print(f"   Nombres ≤ 0 : {negative_and_zero}")
print("*******************************************************************************************")
# 2. Aplatir une liste de listes de listes
print("2. Aplatir une liste de listes de listes:")
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
print(f"Liste originale : {list_of_lists}")

liste_applatie = [item for sous_liste in list_of_lists for inner_list in sous_liste for item in inner_list]
print(f"Liste aplatie : {liste_applatie}")
print("*******************************************************************************************")
# 3. Créer une liste de tuples avec des puissances
print("3. Créer une liste de tuples avec des puissances:")
print(" Format: (i, 1, i, i², i³, i⁴, i⁵) pour i de 0 à 10")
puissances_tuples = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(" Résultat:")
for tuple_item in puissances_tuples:
    print(f" {tuple_item}")
print("*******************************************************************************************")
# 4. Transformer les pays et capitales
print("4. Transformer la liste de pays en format [PAYS, CODE, CAPITALE]:")
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
print(f"Liste originale : {countries}")
# Extraire le premier tuple de chaque sous-liste et créer le format demandé
transformed_countries = [
    [country.upper(), country[:3].upper(), capital.upper()] 
    for sublist in countries 
    for country, capital in sublist
]
print(f"Liste transformée : {transformed_countries}")
print("*******************************************************************************************")
# 5. Transformer en liste de dictionnaires
print("5. Transformer en liste de dictionnaires:")
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
print(f"Liste originale : {countries}")
countries_dict = [
    {'country': country.upper(), 'city': capital.upper()} 
    for sublist in countries 
    for country, capital in sublist
]
print("Liste de dictionnaires :")
for country_dict in countries_dict:
    print(f"   {country_dict}")
print("*******************************************************************************************")
# 6. Concaténer les noms
print("6. Concaténer les prénoms et noms:")
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
print(f"Liste originale : {names}")
full_names = [
    f"{first_name} {last_name}" 
    for sublist in names 
    for first_name, last_name in sublist
]
print(f"Noms complets : {full_names}")
print("*******************************************************************************************")
# 7. Fonction lambda pour la pente et l'ordonnée à l'origine
print("7. Fonctions lambda pour les équations linéaires:")
calculate_slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x2 != x1 else "Pente infinie"
y_intercept = lambda x, y, slope: y - slope * x
print("Calcul de pente:")
print(f"Pente entre (1, 2) et (4, 8) : {calculate_slope(1, 2, 4, 8)}")
print(f"Pente entre (0, 0) et (3, 6) : {calculate_slope(0, 0, 3, 6)}")

print("Calcul d'ordonnée à l'origine:")
print(f"Ordonnée avec point (2, 5) et pente 2 : {y_intercept(2, 5, 2)}")
print(f"Ordonnée avec point (1, 3) et pente 1 : {y_intercept(1, 3, 1)}")
print("*******************************************************************************************")