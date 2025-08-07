# Day 16: Time and Date in Python

Bienvenue dans le jour 16 du défi **30 Days of Python** !

## Objectifs

- Comprendre la gestion du temps et des dates en Python.
- Utiliser les modules `datetime`, `time` et `calendar`.
- Manipuler, formater et effectuer des calculs sur les dates et heures.

## Contenu

- Introduction aux modules de gestion du temps.
- Création et modification d'objets date et heure.
- Conversion entre chaînes de caractères et objets date/heure.
- Calculs sur les dates (différences, ajouts, soustractions).
- Utilisation du module `calendar` pour afficher des calendriers.

## Exemples

```python
from datetime import datetime, timedelta

now = datetime.now()
print("Maintenant :", now)

hier = now - timedelta(days=1)
print("Hier :", hier)
```

## Exercices

- Afficher la date et l'heure actuelles.
- Calculer le nombre de jours entre deux dates.
- Générer le calendrier d'un mois donné.

---

**Bonne pratique !**