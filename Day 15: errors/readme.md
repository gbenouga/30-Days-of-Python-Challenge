# Types d'Erreurs Natifs en Python

Python possède plusieurs types d'erreurs (exceptions) qui peuvent survenir lors de l'exécution d'un programme. Voici les principales :

## 1. SyntaxError
Se produit lorsque le code Python n'est pas correctement écrit.

```python
print("Hello"
```

## 2. NameError
Se produit lorsqu'une variable ou une fonction n'est pas définie.

```python
print(variable_inexistante)
```

## 3. TypeError
Se produit lorsqu'une opération ou une fonction est appliquée à un objet de type inapproprié.

```python
len(5)
```

## 4. ValueError
Se produit lorsqu'une opération reçoit un argument de type correct mais de valeur inappropriée.

```python
int("abc")
```

## 5. IndexError
Se produit lorsqu'on tente d'accéder à un index inexistant dans une séquence.

```python
liste = [1, 2, 3]
print(liste[5])
```

## 6. KeyError
Se produit lorsqu'on tente d'accéder à une clé inexistante dans un dictionnaire.

```python
d = {"a": 1}
print(d["b"])
```

## 7. AttributeError
Se produit lorsqu'on tente d'accéder à un attribut inexistant d'un objet.

```python
"abc".non_existant()
```

## 8. ImportError
Se produit lorsqu'un module ou une fonction ne peut pas être importé.

```python
import module_inexistant
```

## 9. ZeroDivisionError
Se produit lorsqu'on tente de diviser par zéro.

```python
print(1 / 0)
```

## 10. FileNotFoundError
Se produit lorsqu'un fichier ou un dossier n'est pas trouvé.

```python
open("fichier_inexistant.txt")
```

---

Pour gérer ces erreurs, on utilise généralement les blocs `try` et `except`.