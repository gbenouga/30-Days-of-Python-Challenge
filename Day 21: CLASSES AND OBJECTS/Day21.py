### Exercice Day 21
import math
from collections import Counter

class Statistics:
    def __init__(self, data):
        """Initialise la classe avec les données"""
        self.data = data
    
    def count(self):
        """Retourne le nombre d'éléments"""
        return len(self.data)
    
    def sum(self):
        """Retourne la somme des éléments"""
        return sum(self.data)
    
    def min(self):
        """Retourne la valeur minimale"""
        return min(self.data)
    
    def max(self):
        """Retourne la valeur maximale"""
        return max(self.data)
    
    def range(self):
        """Retourne l'étendue (max - min)"""
        return self.max() - self.min()
    
    def mean(self):
        """Retourne la moyenne"""
        return self.sum() / self.count()
    
    def median(self):
        """Retourne la médiane"""
        sorted_data = sorted(self.data)
        n = self.count()
        
        if n % 2 == 0:
            # Nombre pair d'éléments
            mid1 = sorted_data[n // 2 - 1]
            mid2 = sorted_data[n // 2]
            return (mid1 + mid2) / 2
        else:
            # Nombre impair d'éléments
            return sorted_data[n // 2]
    
    def mode(self):
        """Retourne le mode (valeur la plus fréquente) et sa fréquence"""
        counter = Counter(self.data)
        max_count = max(counter.values())
        modes = [k for k, v in counter.items() if v == max_count]
        
        # Si il y a plusieurs modes, retourner le premier
        return {'mode': modes[0], 'count': max_count}
    
    def var(self):
        """Retourne la variance"""
        mean_val = self.mean()
        variance = sum((x - mean_val) ** 2 for x in self.data) / self.count()
        return variance
    
    def std(self):
        """Retourne l'écart-type"""
        return math.sqrt(self.var())
    
    def freq_dist(self):
        """Retourne la distribution de fréquence sous forme de liste de tuples"""
        counter = Counter(self.data)
        total = self.count()
        
        # Calculer les pourcentages et trier par fréquence décroissante
        freq_list = []
        for value, count in counter.items():
            percentage = (count / total) * 100
            freq_list.append((percentage, value))
        
        # Trier par pourcentage décroissant
        freq_list.sort(key=lambda x: x[0], reverse=True)
        return freq_list
    


class PersonAccount:
    def __init__(self, firstname, lastname):
        """Initialise un compte personnel avec prénom et nom"""
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = {}  
        self.expenses = {}  
    
    def add_income(self, description, amount):
        """Ajoute un revenu avec sa description"""
        if description in self.incomes:
            self.incomes[description] += amount
        else:
            self.incomes[description] = amount
    
    def add_expense(self, description, amount):
        """Ajoute une dépense avec sa description"""
        if description in self.expenses:
            self.expenses[description] += amount
        else:
            self.expenses[description] = amount
    
    def total_income(self):
        """Calcule le total des revenus"""
        return sum(self.incomes.values())
    
    def total_expense(self):
        """Calcule le total des dépenses"""
        return sum(self.expenses.values())
    
    def account_balance(self):
        """Calcule le solde du compte (revenus - dépenses)"""
        return self.total_income() - self.total_expense()

# Test avec les données fournies
if __name__ == "__main__":
    ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32,
            33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
    
    data = Statistics(ages)
    print("***********************************************************************")
    print('Count:', data.count())  
    print('Sum:', data.sum())  
    print('Min:', data.min()) 
    print('Max:', data.max())  
    print('Range:', data.range()) 
    print('Mean:', data.mean()) 
    print('Median:', data.median())  
    print('Mode:', data.mode()) 
    print('Standard Deviation:', round(data.std(), 1))  
    print('Variance:', data.var())  
    print('Frequency Distribution:', data.freq_dist())

    print("\n***********************************************************************")
    # Création d'un compte personnel
    person = PersonAccount("Akue", "Ali")
    
    # Ajout de revenus
    person.add_income("Salaire", 3500)
    person.add_income("Freelance", 800)
    person.add_income("Investissements", 200)
    person.add_income("Salaire", 3500)  
    
    # Ajout de dépenses
    person.add_expense("Loyer", 9000)
    person.add_expense("Nourriture", 4000)
    person.add_expense("Transport", 1500)
    person.add_expense("Loisirs", 3000)
    person.add_expense("Nourriture", 1000)  # Ajout aux dépenses nourriture
    
    # Tests des méthodes
    print("Informations du compte :")
    print(f"Prénom: {person.firstname}")
    print(f"Nom: {person.lastname}")
    print(f"Total revenus: {person.total_income()}$")
    print(f"Total dépenses: {person.total_expense()}$")
    print(f"Solde: {person.account_balance()}$")