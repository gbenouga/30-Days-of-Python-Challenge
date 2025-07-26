
# 1. Concaténer les chaînes pour obtenir 'Thirty Days Of Python'
print("***********************************************************************")
str1 = 'Thirty'
str2 = 'Days'
str3 = 'Of'
str4 = 'Python'
result1 = str1 + ' ' + str2 + ' ' + str3 + ' ' + str4
print(result1)

# 2. Concaténer les chaînes pour obtenir 'Coding For All'
print("***********************************************************************")
str1 = 'Coding'
str2 = 'For'
str3 = 'All'
str4 = ' '
result2 = str1 + str4 + str2 + str4 + str3
print(result2)


# 3. Déclarer une variable company
print("***********************************************************************")
company = "Coding For All"

# 4. Afficher la variable company
print(company)

# 5. Afficher la longueur de la chaîne company
print("***********************************************************************")
print(len(company))

# 6. Mettre tous les caractères en majuscules
print("***********************************************************************")
print(company.upper())

# 7. Mettre tous les caractères en minuscules
print("***********************************************************************")
print(company.lower())

# 8. Utiliser capitalize(), title(), swapcase() sur 'Coding For All'
print("***********************************************************************")
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9. retourner le premier mot de la chaîne company
print("***********************************************************************")
first_word = company[0]
print("Premier mot :", first_word)

# 10. Vérifier si 'Coding' est dans company
print("***********************************************************************")
print("l' Index de 'Coding' :", company.index('Coding'))
print("'Coding' trouvé avec find  à l' Index :", company.find('Coding'))
print("'Coding' dans company :", 'Coding' in company)

# 11. Remplacer 'Coding' par 'Python' dans company
print("***********************************************************************")
company_python = company.replace('Coding', 'Python')
print(company_python)

# 12. Remplacer 'Everyone' par 'All' dans 'Python for Everyone'
print("***********************************************************************")
phrase = "Python for Everyone"
phrase_modifiee = phrase.replace('Everyone', 'All')
print(phrase_modifiee)

# 13. Séparer la chaîne 'Coding For All' avec l'espace comme séparateur
print("***********************************************************************")
split_company = company.split(' ')
print(split_company)

# 14. Séparer la chaîne à la virgule
print("***********************************************************************")
grands = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
split_ = grands.split(', ')
print(split_)

# 15. Caractère à l'index 0 dans 'Coding For All'
print("***********************************************************************")
print("Caractère à l'index 0 :", company[0])

# 16. Dernier index de la chaîne 'Coding For All'
print("***********************************************************************")
last_index = len(company) - 1
print("Dernier index :", last_index)

# 17. Caractère à l'index 10 dans 'Coding For All'
print("***********************************************************************")
print("Caractère à l'index 10 :", company[10])

# 18. Acronyme pour 'Python For Everyone'
print("***********************************************************************")
phrase = "Python For Everyone"
acronyme = ''.join([mot[0].upper() for mot in phrase.split()])
print("Acronyme de 'Python For Everyone' :", acronyme)

# 19. Acronyme pour 'Coding For All'
print("***********************************************************************")
phrase2 = "Coding For All"
acronyme2 = ''.join([mot[0].upper() for mot in phrase2.split()])
print("Acronyme de 'Coding For All' :", acronyme2)

# 20. Position de la première occurrence de 'C' dans 'Coding For All'
print("***********************************************************************")
print("Index du premier 'C' :", phrase2.index('C'))

# 21. Position de la première occurrence de 'F' dans 'Coding For All'
print("***********************************************************************")
print("Index du premier 'F' :", phrase2.index('F'))

# 22. Position de la dernière occurrence de 'l' dans 'Coding For All People'
print("***********************************************************************")
phrase3 = "Coding For All People"
print("Index du dernier 'l' :", phrase3.rfind('l'))

# 23. Position de la première occurrence du mot 'because'
print("***********************************************************************")
sentence = 'You cannot end a sentence with because because because is a conjunction'
premiere_because = sentence.find('because')
print("Première occurrence de 'because' :", premiere_because)

# 24. Position de la dernière occurrence du mot 'because'
print("***********************************************************************")
dernier_because = sentence.rindex('because')
print("Dernière occurrence de 'because' :", dernier_because)

# 25. Extraire la phrase 'because because because'
print("***********************************************************************")
start = sentence.find('because')
end = sentence.find('is a conjunction')
phrase_because = sentence[start:end].strip()
print("Phrase extraite :", phrase_because)

# 26. Position de la première occurrence du mot 'because'
print("***********************************************************************")
sentence = 'You cannot end a sentence with because because because is a conjunction'
premiere_because_position = sentence.find('because')
print("Première occurrence de 'because' :", premiere_because_position)

# 27. Extraire la phrase 'because because because'
print("***********************************************************************")
start = sentence.find('because')
end = start + len('because because because')
phrase_because = sentence[start:end]
print("Phrase extraite :", phrase_because)

# 28. Vérifier si 'Coding For All' commence par 'Coding'
print("***********************************************************************")
print("Commence t-elle par 'Coding' ?:", company.startswith('Coding'))

# 29. Vérifier si 'Coding For All' se termine par 'coding'
print("***********************************************************************")
print("Se termine t-elle par 'coding' ?:", company.endswith('coding'))

# 30. Supprimer les espaces à gauche et à droite de la chaîne
print("***********************************************************************")
chaine_avec_espaces = ' Coding For All '
chaine_sans_espaces = chaine_avec_espaces.strip()
print("Sans espaces :", chaine_sans_espaces)

# 31. Vérifier si les variables sont des identifiants valides
print("***********************************************************************")
var1 = '30DaysOfPython'
var2 = 'thirty_days_of_python'
print("30DaysOfPython est un identifiant :", var1.isidentifier())
print("thirty_days_of_python est un identifiant :", var2.isidentifier())

# 32. Joindre la liste avec un hash et un espace
print("***********************************************************************")
libs = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
libs_joined = ' # '.join(libs)
print("Librairies jointes :", libs_joined)

# 33. Séparer les phrases avec le saut de ligne
print("***********************************************************************")
print("I am enjoying this challenge.\nI just wonder what is next.")

# 34. Utiliser la tabulation pour séparer les colonnes
print("***********************************************************************")
print("Name\t\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")


# 35. Affichage formaté de la zone d'un cercle
print("***********************************************************************")
radius = 10
aire = 3.14 * radius ** 2
print("RADIUS = {}\nAire = 3.14 * {} ** 2\nLe cercle de rayon {} est de {} mètres carrés.".format(radius, radius, radius, aire))

# 36. Affichage formaté des opérations
print("***********************************************************************")
a, b = 8, 6
print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {:.2f}".format(a, b, a / b))
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} ** {} = {}".format(a, b, a ** b))