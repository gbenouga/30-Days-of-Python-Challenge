### Cette classe Statistics 
implémente toutes les méthodes statistiques demandées :

# Mesures de tendance centrale :
```
mean() : moyenne arithmétique
median() : valeur médiane
mode() : valeur la plus fréquente avec son nombre d'occurrences
Mesures de variabilité :
```
```
range() : étendue (max - min)
var() : variance
std() : écart-type
Autres mesures :
```
```
min(), max() : valeurs minimale et maximale
count() : nombre d'éléments
sum() : somme des éléments
freq_dist() : distribution de fréquence en pourcentages
```

### Cette classe PersonAccount 
implémente toutes les fonctionnalités demandées :

# Propriétés :
```
firstname : prénom de la personne
lastname : nom de famille de la personne
incomes : dictionnaire des revenus avec descriptions
expenses : dictionnaire des dépenses avec descriptions
```
# Méthodes :
```
add_income(description, amount) : ajoute un revenu avec sa description
add_expense(description, amount) : ajoute une dépense avec sa description
total_income() : calcule le total des revenus
total_expense() : calcule le total des dépenses
account_balance() : calcule le solde (revenus - dépenses)
account_info() : affiche un résumé complet du compte
```
La classe gère automatiquement l'ajout de montants à des catégories existantes et fournit une vue d'ensemble claire de la situation financière.