# Day 14 : Higher Order Functions

## 1. Différences entre map, filter, et reduce

### **map()**
- **But** : Applique une fonction à chaque élément d'un itérable
- **Retourne** : Un nouvel itérable (map object) de même taille
- **Utilisation** : Transformer chaque élément

```python
# Exemple map()
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16, 25]
```

### **filter()**
- **But** : Filtre les éléments selon une condition (True/False)
- **Retourne** : Un nouvel itérable contenant seulement les éléments qui satisfont la condition
- **Utilisation** : Sélectionner des éléments spécifiques

```python
# Exemple filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4, 6, 8, 10]
```

### **reduce()**
- **But** : Applique une fonction de façon cumulative pour réduire l'itérable à une seule valeur
- **Retourne** : Une seule valeur (pas un itérable)
- **Utilisation** : Accumuler, sommer, multiplier, etc.

```python
# Exemple reduce()
from functools import reduce
numbers = [1, 2, 3, 4, 5]
sum_all = reduce(lambda x, y: x + y, numbers)
print(sum_all)  # 15
```

## 2. Différences entre Higher Order Function, Closure et Decorator

### **Higher Order Function (Fonction d'ordre supérieur)**
Une fonction qui :
- Prend une ou plusieurs fonctions comme arguments, ET/OU
- Retourne une fonction comme résultat

```python
# Exemple Higher Order Function
def apply_operation(func, x, y):
    """Fonction qui prend une autre fonction comme argument"""
    return func(x, y)

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

result1 = apply_operation(add, 5, 3)      # 8
result2 = apply_operation(multiply, 5, 3) # 15

# map, filter, reduce sont des exemples de higher order functions
```

### **Closure (Fermeture)**
Une fonction qui :
- Capture et "se souvient" des variables de son environnement externe
- Peut accéder à ces variables même après que la fonction externe ait terminé

```python
# Exemple Closure
def outer_function(x):
    """Fonction externe"""
    def inner_function(y):
        """Fonction interne qui capture 'x' de l'environnement externe"""
        return x + y  # 'x' est capturé de outer_function
    return inner_function

# Création d'une closure
add_10 = outer_function(10)  # x = 10 est "capturé"
print(add_10(5))  # 15 (10 + 5)

# Même après que outer_function soit terminée, inner_function 
# se souvient encore de x = 10
```

### **Decorator (Décorateur)**
Une fonction qui :
- Modifie ou étend le comportement d'une autre fonction
- Utilise le symbole `@` pour une syntaxe plus propre
- Est essentiellement une higher order function avec une syntaxe spéciale

```python
# Exemple Decorator
def my_decorator(func):
    """Décorateur qui ajoute du comportement avant et après la fonction"""
    def wrapper(*args, **kwargs):
        print("Avant l'exécution de la fonction")
        result = func(*args, **kwargs)
        print("Après l'exécution de la fonction")
        return result
    return wrapper

# Utilisation avec @
@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")
# Sortie:
# Avant l'exécution de la fonction
# Hello, Alice!
# Après l'exécution de la fonction
```

## Résumé des différences

| Concept | Description | Exemple d'utilisation |
|---------|-------------|----------------------|
| **map()** | Transforme chaque élément | Convertir des températures |
| **filter()** | Sélectionne des éléments | Filtrer des nombres pairs |
| **reduce()** | Réduit à une seule valeur | Calculer une somme totale |
| **Higher Order Function** | Prend/retourne des fonctions | `map()`, `filter()`, fonctions personnalisées |
| **Closure** | Capture des variables externes | Fonctions de configuration, callbacks |
| **Decorator** | Modifie le comportement | Logging, authentification, timing |

## Exemples pratiques combinés

```python
from functools import reduce

# Données
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. map: doubler chaque nombre
doubled = list(map(lambda x: x * 2, numbers))
print(f"Doublés: {doubled}")

# 2. filter: garder seulement les nombres pairs
evens = list(filter(lambda x: x % 2 == 0, doubled))
print(f"Pairs: {evens}")

# 3. reduce: sommer tous les nombres pairs doublés
total = reduce(lambda x, y: x + y, evens)
print(f"Total: {total}")

# 4. Closure pour créer des multiplicateurs
def create_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

times_3 = create_multiplier(3)
result = list(map(times_3, numbers))
print(f"Multipliés par 3: {result}")

# 5. Decorator pour mesurer le temps d'exécution
import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} a pris {end - start:.4f} secondes")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(1)
    return "Terminé!"

slow_function()
```