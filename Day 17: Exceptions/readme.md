# Jour 17 : Exceptions

Bienvenue au **Jour 17** du défi 30 Jours de Python !

## 📚 Sujets abordés
- Introduction aux exceptions
- Gestion des exceptions avec `try`, `except`, `else` et `finally`
- Lever des exceptions avec `raise`
- Création de classes d'exceptions personnalisées

## 📝 Tâches
- S'exercer à gérer différents types d'exceptions
- Écrire du code qui lève et intercepte des exceptions
- Implémenter des classes d'exceptions personnalisées

## 🚀 Ressources
- [Documentation sur les exceptions en Python](https://docs.python.org/3/tutorial/errors.html)
- [Real Python : Exceptions](https://realpython.com/python-exceptions/)

## 💡 Exemple

```python
try:
    number = int(input("Entrez un nombre : "))
    print(10 / number)
except ValueError:
    print("Veuillez entrer un entier valide.")
except ZeroDivisionError:
    print("Impossible de diviser par zéro.")
finally:
    print("Exécution terminée.")
```