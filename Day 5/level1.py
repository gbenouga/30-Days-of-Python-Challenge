# 1. Déclaration  d'une liste vide
print("****************************************************")
# liste_vide = list()
liste_vide = []
print("Liste vide :", liste_vide)

# 2. Déclarer une liste avec plus de 5 éléments
ma_liste = [ 8, 7, 89, 4, 10, 6, 7]

# 3. Trouver la longueur de la liste
print("****************************************************")
print("Longueur de ma_liste :", len(ma_liste))

# 4. récupérer le premier, le milieu et le dernier élément
print("****************************************************")
print("Premier élément :", ma_liste[0])
index_milieu = len(ma_liste) // 2
print("Élément se trouvant au milieu :", ma_liste[index_milieu])
print("Dernier élément :", ma_liste[-1])

# 5. Liste mixed_data_types
print("****************************************************")
mixed_data_types = ["Laurent", 24, 1.75, "Célibataire", "Agodékè"]
print("mixed_data_types :", mixed_data_types)

# 6. Liste nommée it_companies
print("****************************************************")
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7. Afficher la liste
print("****************************************************")
print("it_companies :", it_companies)

# 8. Afficher le nombre de sociétés dans la liste
print("****************************************************")
print("Nombre de sociétés :", len(it_companies))

# 9. Premier, milieu et dernier élément
print("****************************************************")
print("Première société :", it_companies[0])
index_milieu = len(it_companies) // 2
print("Société se trouvant au milieu :", it_companies[index_milieu])
print("Dernière société :", it_companies[-1])

# 10. Modifier une société et afficher la liste
print("****************************************************")
it_companies[3] = "Tesla"
print("Liste des compagnies après modification :", it_companies)

# 11. Ajouter une société à it_companies
print("****************************************************")
it_companies.append("Twitter")
print("Liste des compagnies après ajout :", it_companies)

# 12. Insérer une société au milieu de la liste
print("****************************************************")
index_milieu = len(it_companies) // 2
it_companies.insert(index_milieu, "Netflix")
print("Liste des compagnies après insertion au milieu :", it_companies)

# 13. Mettre un nom de société en majuscule (sauf IBM)
print("****************************************************")

it_companies[2] = it_companies[2].upper()  # Mettre Microsoft en majuscule
print("Liste des compagnies après modification en majuscule de Microsoft :", it_companies)

# 14. Joindre les sociétés avec '#; '
print("****************************************************")
companies_join = '#; '.join(it_companies)
print(" Liste des compagnies :", companies_join)

# 15. Vérifier si une société existe dans la liste
print("****************************************************")
company = "Tesla"
print(f"{company} existe t-elle dans la liste :", company in it_companies)

# 16. Trier la liste des compagnies
print("****************************************************")
it_companies.sort()
print("Liste triée :", it_companies)

# 17. Inverser la liste (ordre décroissant)
print("****************************************************")
it_companies.reverse()
print("Liste inversée :", it_companies)

# 18. Extraire les 3 premières sociétés
print("****************************************************")
print("3 premières sociétés :", it_companies[:3])

# 19. Extraire les 3 dernières sociétés
print("****************************************************")
print("3 dernières sociétés :", it_companies[-3:])

# 20. Extraire la/les société(s) du milieu
print("****************************************************")
n = len(it_companies)

var1 = it_companies[n // 2 - 1 : n // 2 + 1]
var2 = it_companies[n // 2]
if n % 2 == 1:
    print("Société du milieu :", var2)
else:
    print("Sociétés du milieu :", var1)


# 21. Supprimer la première société de la liste
print("****************************************************")
it_companies.pop(0)
print("Liste des sociétés après suppression du premier élément :", it_companies)

# 22. Supprimer la/les société(s) du milieu
print("****************************************************")
n = len(it_companies)
var1 = n // 2 - 1 
var2 = n // 2 + 1
var3 = n // 2
if n % 2 == 1:
    it_companies.pop(var3)
else:
    del it_companies[var1 : var2]
print("Liste des sociétés après suppression du/des élément(s) du milieu :", it_companies)

# 23. Supprimer la dernière société de la liste
print("****************************************************")
it_companies.pop(-1)
print("Liste des sociétés après suppression du dernier élément :", it_companies)

# 24. Supprimer toutes les sociétés de la liste
print("****************************************************")
it_companies.clear()
print("Liste après suppression de tous les éléments :", it_companies)

# 25. Détruire la liste it_companies
print("****************************************************")
del it_companies
# print(it_companies)  # Provoque une erreur si elle est décommentée

# 26. Joindre les listes front_end et back_end
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
print("Liste full_stack :", full_stack)

# 27. Insérer Python et SQL après Redux
index_redux = full_stack.index('Redux')
full_stack.insert(index_redux + 1, 'Python')
full_stack.insert(index_redux + 2, 'SQL')
print("Liste full_stack après insertion :", full_stack)
