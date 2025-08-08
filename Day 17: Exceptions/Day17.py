#### Day 17 : EXCEPTIONS & UNPACKING

print("=== Day 17 : EXCEPTIONS & UNPACKING ===\n")

# 1. Unpacking exercise avec les pays
print("1. Exercice d'unpacking avec les pays:")
names = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland', 'Estonia', 'Russia']

print(f"Liste originale: {names}")

# Unpacking des 5 premiers pays dans nordic_countries, Estonia dans es, Russia dans ru
*nordic_countries, es, ru = names

print(f"Pays nordiques (5 premiers): {nordic_countries}")
print(f"Estonie (es): {es}")
print(f"Russie (ru): {ru}")


# Unpacking avec slice
print("\nAutre méthode avec slice:")
nordic_countries_alt = names[:5]
es_alt = names[5]
ru_alt = names[6]

print(f"Pays nordiques (slice): {nordic_countries_alt}")
print(f"Estonie (slice): {es_alt}")
print(f"Russie (slice): {ru_alt}")

print("\n" + "="*60)
print("GESTION DES EXCEPTIONS EN PYTHON")
print("="*60)

# Exemples d'exceptions courantes
print("\n2. Exemples d'exceptions courantes:")

# Exception IndexError
print("\na) IndexError - Index hors limites:")
try:
    print(f"Élément à l'index 10: {names[10]}")
except IndexError as e:
    print(f"Erreur: {e}")
    print("Solution: Vérifier la taille de la liste avant d'accéder à un index")

# Exception KeyError
print("\nb) KeyError - Clé inexistante dans un dictionnaire:")
person = {'nom': 'Alice', 'âge': 25, 'ville': 'Paris'}
try:
    print(f"Profession: {person['profession']}")
except KeyError as e:
    print(f"Erreur: Clé {e} non trouvée")
    print("Solution: Utiliser .get() ou vérifier l'existence de la clé")
    print(f"Avec .get(): {person.get('profession', 'Non spécifiée')}")

# Exception ValueError
print("\nc) ValueError - Conversion impossible:")
try:
    nombre = int("abc")
except ValueError as e:
    print(f"Erreur: {e}")
    print("Solution: Valider les données avant conversion")

# Exception ZeroDivisionError
print("\nd) ZeroDivisionError - Division par zéro:")
try:
    resultat = 10 / 0
except ZeroDivisionError as e:
    print(f"Erreur: {e}")
    print("Solution: Vérifier que le diviseur n'est pas zéro")

# Exception FileNotFoundError
print("\ne) FileNotFoundError - Fichier inexistant:")
try:
    with open("fichier_inexistant.txt", "r") as f:
        contenu = f.read()
except FileNotFoundError as e:
    print(f"Erreur: {e}")
    print("Solution: Vérifier l'existence du fichier ou créer un fichier par défaut")

print("\n" + "="*60)
print("3. Gestion avancée des exceptions:")

# Fonction avec gestion d'exceptions multiple
def diviser_nombres(a, b):
    """Fonction qui divise deux nombres avec gestion d'exceptions"""
    try:
        # Conversion en float si ce sont des chaînes
        num1 = float(a)
        num2 = float(b)
        
        # Division
        resultat = num1 / num2
        return resultat
        
    except ValueError:
        print(f"Erreur: Impossible de convertir '{a}' ou '{b}' en nombre")
        return None
    except ZeroDivisionError:
        print("Erreur: Division par zéro impossible")
        return None
    except Exception as e:
        print(f"Erreur inattendue: {e}")
        return None

# Tests de la fonction
print("\nTests de la fonction diviser_nombres:")
tests = [
    (10, 2),
    ("15", "3"),
    (8, 0),
    ("abc", 5),
    (None, 2)
]

for a, b in tests:
    print(f"diviser_nombres({a}, {b}) = {diviser_nombres(a, b)}")

print("\n" + "="*60)
print("4. Try-except-else-finally:")

def lire_fichier_safe(nom_fichier):
    """Fonction de lecture de fichier avec gestion complète"""
    fichier = None
    try:
        print(f"Tentative d'ouverture de {nom_fichier}")
        fichier = open(nom_fichier, "r")
        contenu = fichier.read()
        print("Fichier lu avec succès")
        
    except FileNotFoundError:
        print(f"Fichier {nom_fichier} non trouvé")
        contenu = None
        
    except PermissionError:
        print(f"Permission refusée pour {nom_fichier}")
        contenu = None
        
    else:
        print("Aucune exception rencontrée")
        
    finally:
        if fichier:
            fichier.close()
            print("Fichier fermé")
        print("Nettoyage terminé")
    
    return contenu

# Test de la fonction
print("\nTest de lecture de fichier:")
contenu = lire_fichier_safe("test.txt")

print("\n" + "="*60)
print("5. Création d'exceptions personnalisées:")

# Exception personnalisée
class AgeInvalideError(Exception):
    """Exception levée quand l'âge est invalide"""
    def __init__(self, age, message="Âge invalide"):
        self.age = age
        self.message = message
        super().__init__(self.message)

class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.set_age(age)
    
    def set_age(self, age):
        if not isinstance(age, int):
            raise AgeInvalideError(age, "L'âge doit être un entier")
        if age < 0:
            raise AgeInvalideError(age, "L'âge ne peut pas être négatif")
        if age > 150:
            raise AgeInvalideError(age, "L'âge ne peut pas dépasser 150 ans")
        self.age = age
    
    def __str__(self):
        return f"{self.nom}, {self.age} ans"

# Tests avec exceptions personnalisées
print("\nTests avec exceptions personnalisées:")
test_personnes = [
    ("Alice", 25),
    ("Bob", -5),
    ("Charlie", 200),
    ("David", "trente")
]

for nom, age in test_personnes:
    try:
        personne = Personne(nom, age)
        print(f"✓ Personne créée: {personne}")
    except AgeInvalideError as e:
        print(f"✗ Erreur pour {nom}: {e.message} (âge fourni: {e.age})")

print("\n" + "="*60)
print("6. Unpacking avancé:")

# Unpacking avec différentes structures
print("\nUnpacking avec tuples et listes:")

# Tuple simple
coordonnees = (10, 20, 30)
x, y, z = coordonnees
print(f"Coordonnées: x={x}, y={y}, z={z}")

# Unpacking avec *
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
premier, second, *milieu, avant_dernier, dernier = nombres
print(f"Premier: {premier}")
print(f"Second: {second}")
print(f"Milieu: {milieu}")
print(f"Avant-dernier: {avant_dernier}")
print(f"Dernier: {dernier}")

# Unpacking avec dictionnaires
print("\nUnpacking avec dictionnaires:")
info = {'nom': 'Alice', 'age': 30, 'ville': 'Paris', 'profession': 'Ingénieur'}

def presenter_personne(**kwargs):
    for cle, valeur in kwargs.items():
        print(f"  {cle}: {valeur}")

print("Informations de la personne:")
presenter_personne(**info)

# Unpacking dans les fonctions
print("\nUnpacking dans les appels de fonction:")
def calculer(a, b, c):
    return a + b + c

valeurs = [5, 10, 15]
resultat = calculer(*valeurs)
print(f"Somme de {valeurs}: {resultat}")

print(f"\n{'='*60}")
print(f"\n{'='*60}")