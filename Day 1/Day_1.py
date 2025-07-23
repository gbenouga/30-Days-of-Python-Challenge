####
a = 7
b = 9
#####
phrase = "votre nom, votre nom de famille, votre pays,je profite de 30 jours de python"
######
booleen = True
liste = [1, 2, 3, "Python"]
mon_tuple = (4, 5, 6, "Code")
ensemble = {7, 8, 9, "AI"}
mon_dict = {"nom": "Alice", "age": 25, "pays": "France"}

###operations 
print("********************Opérations arithmétiques :********************************")
print("Addition :", a + b)
print("Soustraction :", a - b)
print("Multiplication :", a * b)
print("Modulo :", a % b)
print("Division :", a / b)
print("Exponentielle :", a ** b)
print("Division entière :", a // b)

### affichage des variables
print("********************Affichage des variables :********************************")
print(phrase)

# Vérification des types de données
print("********************Vérification des types de données :********************************")
# int
print(type(10))
# float                                  
print(type(9.8))
# float
print(type(3.14))  
# complex                             
print(type(4 - 4j)) 
# liste                           
print(type(['Asabeneh', 'Python', 'Finlande']))
# str
print(type(phrase))
### Exemples pour differents types de données


# Affichage des exemples
print("********************Exemples de différents types de données :********************************")
#booleen
print("Booléen :", booleen)
#Liste
print("Liste :", liste)
# Tuple
print("Tuple :", mon_tuple)
# Ensemble
print("Set :", ensemble)
# Dictionnaire
print("Dictionnaire :", mon_dict)

### Vérification des types de données
print("********************Vérification des types de données :********************************")
print(type(booleen)) 
print(type(liste))   
print(type(mon_tuple)) 
print(type(ensemble))  
print(type(mon_dict)) 