#### Day 18 : REGULAR EXPRESSIONS

import re
from collections import Counter

print("****************************************************************************")
# 1. Trouver le mot le plus fréquent dans un paragraphe
print("1. Mot le plus fréquent dans le paragraphe:")
paragraphe = '''I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'''

print(f"texte original:\n{paragraphe}\n")

# Avec les expressions régulières
# Trouver tous les mots (lettres seulement, ignorer la ponctuation)
words = re.findall(r'\b[a-zA-Z]+\b', paragraphe.lower())
print(f"La liste des mots extraits: {words}")

# Compter la fréquence des mots
word_count = Counter(words)
print(f"\nListe de la fréquence des mots:")
for word, count in word_count.most_common():
    print(f"({count}, '{word}')")

most_frequent = word_count.most_common(1)[0]
print(f"\nMot le plus fréquent: '{most_frequent[1]}' ({most_frequent[0]} fois)")

print("***************************************************************************\n")
# 2. Extraction des positions des particules et calcul de la distance maximale
print("2. Position des particules et distance maximale:")

texte = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction."

print(f"Texte original:\n{texte}\n")

# Extraire tous les nombres (positifs et négatifs)
# Pattern pour les nombres entiers (positifs et négatifs)
numbers_pattern = r'-?\d+'
points_str = re.findall(numbers_pattern, texte)
print(f"Points extraits (chaînes): {points_str}")

# Convertir en entiers
points = [int(point) for point in points_str]
print(f"Points convertis: {points}")

# Trier les points
sorted_points = sorted(points)
print(f"Points triés: {sorted_points}")

# Calculer la distance entre les deux points les plus éloignés
min_point = min(points)
max_point = max(points)
distance = max_point - min_point

print(f"\nPoint minimum: {min_point}")
print(f"Point maximum: {max_point}")
print(f"Distance maximale: {max_point} - ({min_point}) = {distance}")

print("***************************************************************************\n")

# Cheat sheet des patterns regex courants
print(f"\n🔍 CHEAT SHEET - Patterns Regex Courants:")
print("-" * 45)
patterns_info = [
    (r'\d+', "Un ou plusieurs chiffres"),
    (r'\w+', "Un ou plusieurs caractères de mot"),
    (r'\s+', "Un ou plusieurs espaces"),
    (r'^...', "Début de chaîne"),
    (r'...$', "Fin de chaîne"),
    (r'[a-z]+', "Lettres minuscules"),
    (r'[A-Z]+', "Lettres majuscules"),
    (r'[0-9]{3}', "Exactement 3 chiffres"),
    (r'.+@.+\..+', "Adresse email simple"),
    (r'\b\w+\b', "Mot entier"),
]

for pattern, description in patterns_info:
    print(f"  {pattern:<15} - {description}")
    
print("***************************************************************************\n")
print("**********Exercice 2**********")
    
# 1. Pattern pour identifier une variable Python valide
print("1. Validation de noms de variables Python:")    
def is_valid_variable(name):
    """
        Vérifie si une chaîne est un nom de variable Python valide.
        Règles:
        - Commence par une lettre (a-z, A-Z) ou underscore (_)
        - Suivi de lettres, chiffres ou underscores
        - Ne peut pas commencer par un chiffre
        - Pas de caractères spéciaux comme -, espace, etc.
        """
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
        
    # Vérifier aussi que ce n'est pas un mot-clé Python
    python_keywords = {
            'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del',
            'elif', 'else', 'except', 'exec', 'finally', 'for', 'from', 'global',
            'if', 'import', 'in', 'is', 'lambda', 'not', 'or', 'pass', 'print',
            'raise', 'return', 'try', 'while', 'with', 'yield', 'True', 'False',
            'None', 'async', 'await', 'nonlocal'
    }
        
    if name in python_keywords:
        return False
        
    return bool(re.match(pattern, name))
    
# Tests de validation
test_variables = [
    'first_name',      
    'first-name',      
    '1first_name',     
    'firstname',       
    '_private',        
    '__special__',     
    'var123',          
    'class',           
    'my var',          
    'my@var',          
    '',                
    '123',             
    'camelCase',       
    'UPPER_CASE',      
    ]
    
print("Tests de validation de variables Python:")
for var in test_variables:
    result = is_valid_variable(var)
    status = "Valide" if result else "Invalide"
    print(f"  is_valid_variable('{var}') -> {result} ({status})")
    
print("\n***************************************************************************\n")
print("**********Exercice 3 **********\n")
    
# 6. Nettoyer le texte et trouver les 3 mots les plus fréquents
print("6. Nettoyage de texte avec caractères spéciaux et analyse de fréquence:")
    
phrase = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

print("Texte original avec caractères spéciaux:")
print(f"'{phrase}'\n")

def clean_text_advanced(texte):
    """
    Nettoie un texte en supprimant tous les caractères spéciaux
    et en gardant seulement les lettres et espaces
    """
    # Supprimer tous les caractères qui ne sont pas des lettres ou des espaces
    cleaned = re.sub(r'[^a-zA-Z\s]', '', texte)
    # Remplacer les espaces multiples par un seul espace
    cleaned = re.sub(r'\s+', ' ', cleaned)
    return cleaned.strip()

def most_frequent_words(texte, top_n=3):
    """
    Trouve les mots les plus fréquents dans un texte nettoyé
    """
    # Convertir en minuscules et diviser en mots
    words = texte.lower().split()
    # Compter la fréquence
    word_count = Counter(words)
    # Retourner les top_n mots les plus fréquents
    return word_count.most_common(top_n)
    
# Nettoyer le texte
cleaned_text = clean_text_advanced(phrase)
print("Texte nettoyé:")
print(f"'{cleaned_text}'\n")
    
# Trouver les 3 mots les plus fréquents
most_frequent = most_frequent_words(cleaned_text, 3)
print("Les 3 mots les plus fréquents:")
print(f"{most_frequent}")
    
# Affichage détaillé
print("\nRécapitulatif:")
print(f"Nombre total de mots: {len(cleaned_text.split())}")
print(f"Nombre de mots uniques: {len(set(cleaned_text.lower().split()))}")

