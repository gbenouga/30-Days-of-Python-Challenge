### Day 8: Dictionnaires
# 1. Créer un dictionnaire vide dog
print("*****************************************************************************")
dog = {}
print("Dictionnaire dog créé :", dog)

# 2. Ajouter des clés au dictionnaire dog
print("*****************************************************************************")
dog['name'] = 'Gwetta'
dog['color'] = 'Noir'
dog['breed'] = 'Pitbull'
dog['legs'] = 4
dog['age'] = 3
print("Dictionnaire dog :", dog)

# 3. Créer un dictionnaire student
student = {
    'first_name': 'Amah',
    'last_name': 'kwatcha',
    'gender': 'Masculin',
    'age': 24,
    'marital_status': 'Célibataire',
    'skills': ['Python', 'Communication', 'Administration Système et Réseau', 'Gestion de Projet'],
    'country': 'France',
    'city': 'Paris',
    'address': '123 rue Exemple'
}

# 4. Longueur du dictionnaire student
print("*****************************************************************************")
print("Longueur du dictionnaire student :", len(student))

# 5. skills et type
print("*****************************************************************************")
print("Skills :", student['skills'])
print("Type de skills :", type(student['skills']))

# 6. Modifier skills en ajoutant des compétences
print("*****************************************************************************")
student['skills'].extend(['Java', 'Gaming', 'Web Development'])
print("Skills après modification :", student['skills'])

# 7. les clés du dictionnaire
print("*****************************************************************************")
print("Clés :", list(student.keys()))

# 8. les valeurs du dictionnaire
print("*****************************************************************************")
print("Valeurs :", list(student.values()))

# 9. Transformer le dictionnaire en liste de tuples
print("*****************************************************************************")
print("Liste de tuples :", list(student.items()))

# 10. Supprimer un élément du dictionnaire
print("*****************************************************************************")
del student['marital_status']
print("Student :", student)

# 11. Supprimer un dictionnaire
del dog
print("*****************************************************************************")

