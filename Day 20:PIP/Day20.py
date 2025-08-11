### Day 20: PIP and HTTP Requests

import requests
import json
import statistics
from collections import Counter
import re
from bs4 import BeautifulSoup


# Exercice 1: Analyse du texte Romeo et Juliet
print("*************************************************************************")
def exercise1():
    print("10 mots les plus fréquents dans Romeo et Juliet")
    
    romeo_and_juliet_text = 'http://www.gutenberg.org/files/1112/1112.txt'
    
    try:
        response = requests.get(romeo_and_juliet_text)
        text = response.text.lower()
        
        # Nettoyer le texte et extraire les mots
        words = re.findall(r'\b[a-z]+\b', text)
        
        # Compter les mots les plus fréquents
        word_counts = Counter(words)
        most_common = word_counts.most_common(10)
        
        print("Les 10 mots les plus fréquents :")
        for i, (word, count) in enumerate(most_common, 1):
            print(f"{i}. {word}: {count}")
            
    except Exception as e:
        print(f"Erreur lors de la récupération du texte : {e}")

# Exercice 2: Analyse de l'API des 
print("*************************************************************************")
def exercise2():
    print("Analyse de l'API des chats :")
    
    cats_api = 'https://api.thecatapi.com/v1/breeds'
    
    try:
        response = requests.get(cats_api)
        cats_data = response.json()
        
        # Extraire les poids en métrique
        weights = []
        lifespans = []
        country_breed_pairs = []
        
        for cat in cats_data:
            # Poids en métrique
            if 'weight' in cat and 'metric' in cat['weight']:
                weight_range = cat['weight']['metric']
                if weight_range and ' - ' in weight_range:
                    try:
                        min_weight, max_weight = map(float, weight_range.split(' - '))
                        avg_weight = (min_weight + max_weight) / 2
                        weights.append(avg_weight)
                    except ValueError:
                        continue
            
            # Durée de vie
            if 'life_span' in cat:
                lifespan_range = cat['life_span']
                if lifespan_range and ' - ' in lifespan_range:
                    try:
                        min_life, max_life = map(int, lifespan_range.split(' - '))
                        avg_life = (min_life + max_life) / 2
                        lifespans.append(avg_life)
                    except ValueError:
                        continue
            
            # Pays et races
            if 'origin' in cat and 'name' in cat:
                country_breed_pairs.append((cat['origin'], cat['name']))
        
        # Statistiques des poids
        if weights:
            print("Statistiques des poids (kg) :")
            print(f"   Min: {min(weights):.2f} kg")
            print(f"   Max: {max(weights):.2f} kg")
            print(f"   Moyenne: {statistics.mean(weights):.2f} kg")
            print(f"   Médiane: {statistics.median(weights):.2f} kg")
            print(f"   Écart-type: {statistics.stdev(weights):.2f} kg")
        
        # Statistiques de la durée de vie
        if lifespans:
            print("Statistiques de la durée de vie (années) :")
            print(f"Min: {min(lifespans):.1f} ans")
            print(f"Max: {max(lifespans):.1f} ans")
            print(f"Moyenne: {statistics.mean(lifespans):.1f} ans")
            print(f"Médiane: {statistics.median(lifespans):.1f} ans")
            print(f"Écart-type: {statistics.stdev(lifespans):.1f} ans")
        
        # Tableau de fréquence pays-races
        print("Tableau de fréquence pays-races (top 10) :")
        country_counts = Counter([pair[0] for pair in country_breed_pairs])
        for country, count in country_counts.most_common(10):
            print(f"{country}: {count} races")
            
    except Exception as e:
        print(f"Erreur lors de la récupération des données des chats : {e}")

# Analyse de l'API des pays
def exercise3():
    print("Analyse de l'API des pays")
    
    countries_api = 'https://restcountries.com/rest/v2/all'
    
    try:
        response = requests.get(countries_api)
        countries_data = response.json()
        
        # Les 10 plus grands pays par superficie
        countries_with_area = []
        for country in countries_data:
            if 'area' in country and country['area']:
                name = country.get('name', {}).get('common', 'Unknown')
                countries_with_area.append((name, country['area']))
        
        largest_countries = sorted(countries_with_area, key=lambda x: x[1], reverse=True)[:10]
        
        print("\ni. Les 10 plus grands pays :")
        for i, (name, area) in enumerate(largest_countries, 1):
            print(f"   {i}. {name}: {area:,} km²")
        
        # Les 10 langues les plus parlées
        language_counts = Counter()
        for country in countries_data:
            if 'languages' in country:
                for lang in country['languages'].values():
                    language_counts[lang] += 1
        
        most_spoken = language_counts.most_common(10)
        print("\nii. Les 10 langues les plus parlées :")
        for i, (language, count) in enumerate(most_spoken, 1):
            print(f"    {i}. {language}: {count} pays")
        
        # Nombre total de langues
        total_languages = len(language_counts)
        print(f"\niii. Nombre total de langues : {total_languages}")
        
    except Exception as e:
        print(f"Erreur lors de la récupération des données des pays : {e}")

# Scraping UCI avec BeautifulSoup4
def exercise4():
    print("Scraping UCI (nécessite BeautifulSoup4)")
    
    try:        
        uci_url = 'https://archive.ics.uci.edu/ml/datasets.php'
        
        response = requests.get(uci_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Chercher les datasets dans le tableau
        datasets = []
        rows = soup.find_all('tr')
        
        for row in rows[1:11]:  # Prendre les 10 premiers datasets
            cells = row.find_all('td')
            if len(cells) >= 2:
                dataset_name = cells[0].get_text(strip=True)
                if dataset_name:
                    datasets.append(dataset_name)
        
        if not datasets:
            print("Aucun dataset trouvé")
            return
        print("Premiers datasets UCI trouvés :")
        for i, dataset in enumerate(datasets, 1):
            print(f"   {i}. {dataset}")
            

    except ImportError:
        print("BeautifulSoup4 n'est pas installé.")
    except Exception as e:
        print(f"Erreur lors du scraping UCI : {e}")

# Fonction principale
def main():
    print("Day 20 - Exercices PIP et requêtes HTTP")
    print("******************************************************************")
    exercise1()
    print("******************************************************************")
    exercise2()
    print("******************************************************************")
    exercise3()
    print("******************************************************************")
    exercise4()

if __name__ == "__main__":
    main()