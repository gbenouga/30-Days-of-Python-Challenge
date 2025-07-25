#### 1 Déclarez votre âge comme variable entière
age = 20

### 2 Déclarez votre taille comme variable flottante
taille = 1.78

### 3 Déclarez une variable qui stocke un nombre complexe
nombre_complexe = 2 + 4j

#### 4 calculer l'aire d'un triangle à partir de la base et de la hauteur saisies par l'utilisateur
print("***********************************************************")
base = float(input("Entrer une base: "))
hauteur = float(input("Entrer une hauteur: "))
aire = 0.5 * base * hauteur
print("L'aire du triangle est", aire)


#### 5 calculer le périmètre d'un triangle à partir des trois côtés saisis par l'utilisateur
print("***********************************************************")

a = float(input("Entrer le côté a: "))
b = float(input("Entrer le côté b: "))
c = float(input("Entrer le côté c: "))
perimetre = a + b + c
print("Le périmètre du triangle est", perimetre)


#### 6 Aire et périmètre d'un rectangle
print("***********************************************************")

longueur = float(input("Entrer la longueur du rectangle: "))
largeur = float(input("Entrer la largeur du rectangle: "))
aire_rectangle = longueur * largeur
perimetre_rectangle = 2 * (longueur + largeur)
print("L'aire du rectangle est", aire_rectangle)
print("Le périmètre du rectangle est", perimetre_rectangle)


#### 7 Aire et circonférence d'un cercle
print("***********************************************************")
rayon = float(input("Entrer le rayon du cercle: "))
pi = 3.14
aire_cercle = pi * rayon * rayon
circonference = 2 * pi * rayon
print("L'aire du cercle est", aire_cercle)
print("La circonférence du cercle est", circonference)

#### 8 Calcul de la pente, l'ordonnée à l'origine et l'abscisse à l'origine de y = 2x - 2
print("***********************************************************")
pente = 2
y = -2
x = -y / pente
print("La pente est", pente)
print("L'ordonnée à l'origine (y-intercept) est", y)
print("L'abscisse à l'origine (x-intercept) est", x)

##### 9. Calcul de la pente et de la distance euclidienne entre (2, 2) et (6, 10)
print("***********************************************************")
x1, y1 = 2, 2
x2, y2 = 6, 10
# calcul de la pente entre les deux points
pentes = (y2 - y1) / (x2 - x1)
print("La pente entre (2,2) et (6,10) est", pentes)

# Distance euclidienne
distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print("La distance euclidienne entre (2,2) et (6,10) est", distance)

#### 10.Comparaison des pentes
print("***********************************************************")
print("Comparaison des pentes :")
print("Pente de y = 2x - 2 :", pente)
print("Pente entre les points (2,2) et (6,10) :", pentes)
print(" pente = pentes :" , pente == pentes)
print(" pente > pentes :", pente > pentes)
print(" pente < pentes :", pente < pentes)

# 11. Calculer la valeur de y (y = x^2 + 6x + 9) pour différents x et trouver pour quel x y = 0
print("***********************************************************")
x1, x2, x3 = -3, 0, 3
y1 = x1**2 + 6*x1 + 9
y2 = x2**2 + 6*x2 + 9
y3 = x3**2 + 6*x3 + 9
print("Pour x = ", x1," y = ", y1)
print("Pour x = ", x2," y = ", y2)
print("Pour x = ", x3," y = ", y3)

# 12. Comparaison false entre la longueur de 'python' et 'dragon'
print("***********************************************************")
len_python = len('python')
len_dragon = len('dragon')
print("Longueur de 'python' :", len_python)
print("Longueur de 'dragon' :", len_dragon)
print("Comparaison false :", len_python == len_dragon)

# 13. Vérifier si 'on' est présent dans les deux mots avec l'opérateur and
print("***********************************************************")
print("'on' dans 'python' et 'dragon' :", ('on' in 'python') and ('on' in 'dragon'))


# 14. Vérifier si 'jargon' est dans la phrase
print("***********************************************************")
phrase = "I hope this course is not full of jargon."
print("'jargon' est dans la phrase :", 'jargon' in phrase)

# 15. Il n'y a pas 'on' dans les deux mots 'dragon' et 'python'
print("***********************************************************")
print("Il n'y a pas 'on' dans les deux mots :", not (('on' in 'dragon') and ('on' in 'python')))

# 16. Longueur du texte 'python', conversion en float puis en string
print("***********************************************************")
longueur_python = len('python')
longueur_float = float(longueur_python)
longueur_str = str(longueur_float)
print("Longueur de 'python' :", longueur_python)
print("Longueur en float :", longueur_float)
print("Longueur en string :", longueur_str)

# 17. Vérifier si un nombre est pair
print("***********************************************************")
nombre = int(input("Entrez un nombre pour vérifier s'il est pair : "))
modulo = nombre % 2
is_pair = modulo == 0
print("Le nombre est pair :", is_pair)

# 18. Vérifier si la division entière de 7 par 3 est égale à la valeur entière de 2.7
print("***********************************************************")
print("7 // 3 == int(2.7) :", 7 // 3 == int(2.7))

# 19. Vérifier si le type de '10' est égal au type de 10
print("***********************************************************")
print("type('10') == type(10) :", type('10') == type(10))

# 20. Vérifier si int('9.8') est égal à 10
print("***********************************************************")
print("int('9.8') == 10 :", int(float('9.8')) == 10)


# 21. Calcul de la renumération hebdomadaire par l'utilisateur
print("***********************************************************")
heures = float(input("Entrez le nombre d'heures : "))
taux_par_heure = float(input("Entrez le taux par heure : "))
gain_hebdomadaire = heures * taux_par_heure
print("Votre gain hebdomadaire est", gain_hebdomadaire)

# 22. Écrivez un script qui invite l'utilisateur à saisir le nombre d'années.
print("***********************************************************")
annees_vécues = int(input("Entrez le nombre d'années que vous avez vécues : "))
secondes_vécues = annees_vécues * 365 * 24 * 60 * 60
print("Vous avez vécu pendant", secondes_vécues, "secondes.")

# 23. Affichage du tableau demandé (script de vrai dilemme mathématique)
print("***********************************************************")
print("N 1 N N^2 N^3")
for n in range(1, 6):
    print(n, 1, n, n**2, n**3)
