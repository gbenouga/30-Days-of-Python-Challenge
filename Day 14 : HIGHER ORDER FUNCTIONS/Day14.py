#### Day 14 : HIGHER ORDER FUNCTIONS

## Exercice 1
from functools import reduce


print("\n**********Exercices: Level 1**********\n")

# 3. Définir des fonctions avant map, filter ou reduce
print("*******************************************************************************")
print("3. Définition de fonctions pour map, filter, reduce:")

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark',
'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def to_upper(country):
    """Convertit un pays en majuscules"""
    return country.upper()

def is_long_name(name):
    """Vérifie si un nom a plus de 6 caractères"""
    return len(name) > 6

def multiply_numbers(x, y):
    """Multiplie deux nombres"""
    return x * y

# Exemples d'utilisation
countries_upper = list(map(to_upper, countries))
print(f"Pays en majuscules: {countries_upper}")

long_names = list(filter(is_long_name, names))
print(f"Noms longs: {long_names}")

product = reduce(multiply_numbers, numbers)
print(f"Produit de tous les nombres: {product}")

# 4. Utiliser for loop pour imprimer chaque pays
print("********************************************************************************")
print("4. Pays (avec for loop):")
for country in countries:
    print(f"   - {country}")

# 5. Utiliser for loop pour imprimer chaque nom
print("*********************************************************************************")
print("5. Noms (avec for loop):")
for name in names:
    print(f" - {name}")

# 6. Utiliser for loop pour imprimer chaque nombre
print("*********************************************************************************")
print("*********************************************************************************")
print("6. Nombres (avec for loop):")
for number in numbers:
    print(f"   - {number}")


print("\n**********Exercices: Level 2**********")

# 1. Utiliser map pour créer une nouvelle liste en mettant chaque pays en majuscules
print("********************************************************************************")
print("1. Pays en majuscules avec map:")
countries_uppercase = list(map(lambda country: country.upper(), countries))
print(f"   {countries_uppercase}")


# 2. utiliser map pour créer une nouvelle liste avec les nombres au carré
print("********************************************************************************")
print("2. Nombres au carré avec map:")
numbers_squared = list(map(lambda x: x**2, numbers))
print(f"   {numbers_squared}")

# 3. utiliser map pour mettre les noms en majuscules
print("********************************************************************************")
print("3. Noms en majuscules avec map:")
names_uppercase = list(map(lambda name: name.upper(), names))
print(f"   {names_uppercase}")

# 4. utiliser filter pour filtrer les pays contenant 'land'
print("********************************************************************************")
print("4. Pays contenant 'land' avec filter:")
countries_with_land = list(filter(lambda country: 'land' in country.lower(), countries))
print(f"   {countries_with_land}")

# 5. utiliser filter pour filtrer les pays avec exactement 6 caractères
print("********************************************************************************")
print("5. Pays avec exactement 6 caractères avec filter:")
countries_six_chars = list(filter(lambda country: len(country) == 6, countries))
print(f"   {countries_six_chars}")

# 6. utiliser filter pour filtrer les pays avec 6 lettres et plus
print("********************************************************************************")
print("6. Pays avec 6 lettres ou plus avec filter:")
countries_six_or_more = list(filter(lambda country: len(country) >= 6, countries))
print(f"   {countries_six_or_more}")

# 7. utiliser filter pour filtrer les pays commençant par 'E'
print("********************************************************************************")
print("7. Pays commençant par 'E' avec filter:")
countries_starting_e = list(filter(lambda country: country.startswith('E'), countries))
print(f"   {countries_starting_e}")

# 8. Chaînage de map, filter et reduce
print("********************************************************************************")
print("8. Chaînage de map, filter et reduce:")
# Prendre les pays, les mettre en majuscules, filtrer ceux avec 6+ caractères, puis les concaténer
chained_result = reduce(
    lambda x, y: x + ', ' + y,
    filter(
        lambda country: len(country) >= 6,
        map(lambda country: country.upper(), countries)
    )
)
print(f"   Résultat chaîné: {chained_result}")

# 9. Fonction pour retourner seulement les éléments de type string d'une liste
print("********************************************************************************")
print("9. Fonction get_string_lists:")
def get_string_lists(lst):
    """Retourne seulement les éléments de type string d'une liste"""
    return list(filter(lambda item: isinstance(item, str), lst))

# Test avec une liste mixte
mixed_list = ['Estonia', 42, 'Finland', 3.14, 'Sweden', True, 'Denmark']
string_only = get_string_lists(mixed_list)
print(f"   Liste mixte: {mixed_list}")
print(f"   Seulement les strings: {string_only}")

# 10. Fonction pour calculer la somme de tous les nombres avec reduce
print("********************************************************************************")
print("10. Fonction pour calculer la somme de tous les nombres avec reduce:")
from functools import reduce
print("\n10. Somme de tous les nombres avec reduce:")
sum_all_numbers = reduce(lambda x, y: x + y, numbers)
print(f"   Somme: {sum_all_numbers}")

# 11. Use reduce to concatenate countries into a sentence
print("\n11. Concaténation des pays avec reduce:")
def concatenate_countries(x, y):
    """Fonction pour concaténer les pays avec la logique appropriée"""
    if x == countries[0]:  # Premier pays
        return x + ', ' + y
    elif y == countries[-1]:  # Dernier pays
        return x + ', and ' + y
    else:  # Pays du milieu
        return x + ', ' + y

countries_sentence = reduce(concatenate_countries, countries)
countries_sentence += " are north European countries"
print(f"   {countries_sentence}")

# Alternative plus simple pour la phrase
print("\n11b. Version alternative de la phrase:")
countries_text = reduce(lambda x, y: x + ', ' + y, countries[:-1])
final_sentence = f"{countries_text}, and {countries[-1]} are north European countries"
print(f"   {final_sentence}")

print("\n**********Exemples supplémentaires**********\n")

# Exemples de chaînage plus complexes
print("Exemples de chaînage avancés:")

# Chaîner: nombres -> carrés -> pairs -> somme
chained_numbers = reduce(
    lambda x, y: x + y,
    filter(
        lambda x: x % 2 == 0,
        map(lambda x: x**2, numbers)
    )
)
print(f"Somme des carrés pairs: {chained_numbers}")

# Chaîner: noms -> majuscules -> longs -> concaténer
long_names_upper = reduce(
    lambda x, y: x + ' & ' + y,
    filter(
        lambda name: len(name) > 6,
        map(lambda name: name.upper(), names)
    )
)
print(f"Noms longs en majuscules: {long_names_upper}")