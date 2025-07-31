#### Day 9: Conditions
## Exercice 1: Level 1
# 1. Condition pour verifier si l'utilisateur peut apprendre à conduire Level 3
print("*****************************************************************************")
print("********** Exercice 1 *****")
print("1. Condition pour vérifier si l'utilisateur peut apprendre à conduire")
age = int(input("Entrez votre âge: "))
if age >= 18:
    print("Vous êtes assez vieux pour apprendre à conduire.")
else:
    annees_restantes = 18 - age
    print(f"Vous avez besoin de {annees_restantes} année{'s' if annees_restantes > 1 else ''} supplémentaires pour apprendre à conduire.")

# 2. Comparaison d'âge Level 3
print("******************************************************************************")
print("\n 2. Comparaison d'âge")
mon_age = 32
ton_age = int(input("Entrez votre âge: "))
if ton_age > mon_age:
    difference = ton_age - mon_age
    print(f"Vous avez {difference} an{'s' if difference > 1 else ''} de plus que moi.")
elif ton_age < mon_age:
    difference = mon_age - ton_age
    print(f"J'ai {difference} an{'s' if difference > 1 else ''} de plus que vous.")
else:
    print("Nous avons le même âge.")

# 3. Comparer deux nombres
print("******************************************************************************")
print("\n 3. Comparer deux nombres")
a = int(input("Entrez le premier nombre: "))
b = int(input("Entrez le deuxième nombre: "))
if a > b:
    print(f"{a} est plus grand que {b}")
elif a < b:
    print(f"{a} est plus petit que {b}")
else:
    print(f"{a} est égal à {b}")


### Exercice 2:
print("********* Exercice 2 *****")
print("******************************************************************************")
# 1. Attribuer une note selon le score de l'étudiant
print(" 1. Attribuer une note selon le score")
score = int(input("Entrez le score de l'étudiant : "))
if score <= 100:
    if score < 80:
        if score < 70:
            if score < 60:
                if score < 50:
                    print("Note : F")
                else:
                    print("Note : D")
            else:
                print("Note : C")
        else:
            print("Note : B")
    else:
        print("Note : A")
else:
    print("Score invalide, veuillez entrer un score entre 0 et 100.")

# 2. Vérifier la saison selon le mois
print("******************************************************************************")
mois = input("Entrez le mois : ").strip().capitalize()
if mois in ['Septembre', 'Octobre', 'Novembre']:
    print("La saison est : Automne ")
elif mois in ['Décembre', 'Janvier', 'Février', 'Decembre', 'Janvier', 'Fevrier']:
    print("La saison est : Hiver")
elif mois in ['Mars', 'Avril', 'Mai']:
    print("La saison est : Printemps")
elif mois in ['Juin', 'Juillet', 'Août', 'Aout']:
    print("La saison est : Été")
else:
    print("Mois invalide")

# 3. Vérifier et ajouter un fruit à la liste
print("******************************************************************************")
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Entrez un fruit : ").lower()
if fruit in fruits:
    print("Ce fruit existe déjà dans la liste")
else:
    fruits.append(fruit)
    print("les fruits:", fruits)


### Exercice 3:
print("********* Exercice 3 *****")
print("******************************************************************************")
# 1. Vérifier si le dictionnaire a la clé 'skills' et afficher la compétence du milieu
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person:
    skills = person['skills']
    n = len(skills)
    # Afficher la compétence du milieu
    if n % 2 == 1:
        print("Compétence du milieu :", skills[n // 2])
    else:
        print("Compétences du milieu :", skills[n // 2 - 1 : n // 2 + 1])
    # Vérifier si 'Python' est dans les compétences
    print("A la compétence Python :", 'Python' in skills)

    # Détection du titre selon les compétences
    if set(skills) == {'JavaScript', 'React'}:
        print("He is a front end developer")
    elif all(skill in skills for skill in ['Node', 'Python', 'MongoDB']):
        print("He is a backend developer")
    elif all(skill in skills for skill in ['React', 'Node', 'MongoDB']):
        print("He is a fullstack developer")
    else:
        print("unknown title")

# Vérifier si la personne est mariée et vit en Finlande
if person.get('is_marred') and person.get('country') == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in Finland. He is married.")