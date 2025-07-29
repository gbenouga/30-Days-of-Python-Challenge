### Exercice 1
# Données initiales
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1. Trouver la longueur du set it_companies
print("*****************************************************************************")
print("La Longueur du set :", len(it_companies))

# 2. Ajouter  la compagnie 'Twitter' au 
print("*****************************************************************************")
it_companies.add('Twitter')
print("Liste des compagnies après ajout de Twitter :", it_companies)

# 3. Ajouter plusieurs compagnies à la fois (Netflix, Tesla, Spotify)
print("*****************************************************************************")
it_companies.update(['Netflix', 'Tesla', 'Spotify'])
print("Liste des compagnies après ajout de Netflix, Tesla, Spotify :", it_companies)

# 4. Supprimer une compagnie du set
print("*****************************************************************************")
it_companies.remove('IBM')
print("Liste des compagnies après suppression de IBM :", it_companies)


### 4 . Supprimer une compagnie du set de façon aléatoire
print("*****************************************************************************")
it_companies.pop()
print("Liste des compagnies après suppression aléatoire :", it_companies)

### 4 . Supprimer une compagnie du set de façon sécurisé
print("*****************************************************************************")
it_companies.discard('IBM')
print("Liste des compagnies après suppression sécurisée de IBM :", it_companies)

# 5. Différence entre remove et discard
print("*****************************************************************************")
print("remove provoque une erreur si l'élément donné n'existe pas, discard ne provoque pas d'erreur dans ces cas.")


##### Exercice 2
# 1. Union de A et B
print("*****************************************************************************")
union_ab = A.union(B)
print("Union de A et B :", union_ab)

# 2. Intersection de A et B
print("*****************************************************************************")
intersection_ab = A.intersection(B)
print("Intersection de A et B :", intersection_ab)

# 3. A est-il un sous-ensemble de B ?
print("*****************************************************************************")
print("A est un sous-ensemble de B (Vrai ou faux):", A.issubset(B))

# 4. A et B sont-ils disjoints ?
print("*****************************************************************************")
print("A et B sont disjoints : (Vrai ou faux)", A.isdisjoint(B))

# 5. Joindre A avec B et B avec A
print("*****************************************************************************")
print("A | B :", A | B)
print("B | A :", B | A)

# 6. Différence symétrique entre A et B
print("*****************************************************************************")
symmetric_diff = A.symmetric_difference(B)
print("La Différence symétrique :", symmetric_diff)

# 7. Supprimer complètement les sets
print("*****************************************************************************")
del A
del B

#### Exercice 3
# Convertir ages en set et comparer leur longueur
print("*****************************************************************************")
ages_st = set(age)
print("Longueur de la liste :", len(age))
print("Longueur du set :", len(ages_st))
if len(age) > len(ages_st):
    print("La liste est la plus grande.")
elif len(age) < len(ages_st):
    print("Le set est le plus grand.")
else:
    print("Les deux ont la même taille.")

# Explication des types de données
print("*****************************************************************************")
print("""string : chaîne de caractères, immuable, utilisée pour du texte.
list : collection ordonnée et modifiable d'éléments, crochets [].
tuple : collection ordonnée et immuable d'éléments, parenthèses ().
set : collection non ordonnée, non indexée, sans doublons, accolades {}.
""")


# Compter les mots uniques dans la phrase
print("*****************************************************************************")
phrase = "I am a teacher and I love to inspire and teach people."
mots = phrase.split()
mot = set(mots)
print("Nombre de mots uniques dans la phrase :", len(mot))