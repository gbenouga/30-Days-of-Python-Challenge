import requests
from bs4 import BeautifulSoup
import json
import time
import re

# Exercice 1: Scraper le site de Boston University
def scrape_boston_university():
    """Scrape Boston University facts et sauvegarde en JSON"""
    print("*****Exercice 1: Scraping Boston University********")
    
    url = 'http://www.bu.edu/president/boston-university-facts-stats/'
    
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Structure pour stocker les données
        bu_data = {
            'title': 'Boston University Facts & Statistics',
            'url': url,
            'facts': [],
            'statistics': []
        }
        
        # Extraire le titre principal
        title = soup.find('h1')
        if title:
            bu_data['title'] = title.get_text(strip=True)
        
        # Chercher les faits et statistiques dans différents conteneurs possibles
        content_areas = soup.find_all(['div', 'section', 'article'])
        
        for area in content_areas:
            # Chercher les listes de faits
            lists = area.find_all(['ul', 'ol'])
            for lst in lists:
                items = lst.find_all('li')
                for item in items:
                    text = item.get_text(strip=True)
                    if text and len(text) > 10:  # Éviter les éléments trop courts
                        bu_data['facts'].append(text)
        
        # Chercher les statistiques dans les paragraphes
        paragraphs = soup.find_all('p')
        for p in paragraphs:
            text = p.get_text(strip=True)
            # Chercher des patterns de statistiques (nombres, pourcentages, etc.)
            if re.search(r'\d+(?:,\d+)*(?:\.\d+)?(?:%|\s+students|\s+faculty|\s+staff)', text, re.IGNORECASE):
                bu_data['statistics'].append(text)
        
        # Supprimer les doublons
        bu_data['facts'] = list(dict.fromkeys(bu_data['facts']))
        bu_data['statistics'] = list(dict.fromkeys(bu_data['statistics']))
        
        # Sauvegarder en JSON
        with open('data/boston_university_facts.json', 'w', encoding='utf-8') as f:
            json.dump(bu_data, f, indent=2, ensure_ascii=False)
        
        print(f"Données sauvegardées: {len(bu_data['facts'])} faits, {len(bu_data['statistics'])} statistiques")
        print(f"Fichier créé: boston_university_facts.json")
        
    except Exception as e:
        print(f"Erreur lors du scraping BU: {e}")
        # Créer un fichier de base en cas d'erreur
        error_data = {
            'error': str(e),
            'url': url,
            'message': 'Le scraping a échoué, possiblement dû à des restrictions du site'
        }
        with open('boston_university_facts.json', 'w', encoding='utf-8') as f:
            json.dump(error_data, f, indent=2, ensure_ascii=False)

# Exercice 2: Scraper les datasets UCI
def scrape_uci_datasets():
    """Scrape la table des datasets UCI et sauvegarde en JSON"""
    print("\n*******Exercice 2: Scraping UCI Datasets*******")
    
    url = 'https://archive.ics.uci.edu/ml/datasets.php'
    
    
    try:
        response = requests.get(url, timeout=15)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        datasets = []
        
        # Chercher la table des datasets
        table = soup.find('table')
        if not table:
            tables = soup.find_all('table')
            if tables:
                table = tables[0]  # Prendre la première table trouvée
        
        if table:
            rows = table.find_all('tr')
            
            # Extraire l'en-tête
            header_row = rows[0] if rows else None
            headers = []
            if header_row:
                for th in header_row.find_all(['th', 'td']):
                    headers.append(th.get_text(strip=True))
            
            # Si pas d'en-têtes trouvés, utiliser des en-têtes par défaut
            if not headers:
                headers = ['Name', 'Data Types', 'Default Task', 'Attribute Types', 'Instances', 'Attributes', 'Year']
            
            # Extraire les données
            for row in rows[1:]:  # Ignorer l'en-tête
                cells = row.find_all(['td', 'th'])
                if len(cells) >= 2:
                    dataset = {}
                    for i, cell in enumerate(cells):
                        if i < len(headers):
                            # Nettoyer le texte
                            text = cell.get_text(strip=True)
                            # Extraire les liens si présents
                            link = cell.find('a')
                            if link:
                                dataset[headers[i]] = {
                                    'text': text,
                                    'link': link.get('href', '')
                                }
                            else:
                                dataset[headers[i]] = text
                        
                    if dataset and any(dataset.values()):  # Éviter les lignes vides
                        datasets.append(dataset)
        
        # Structure finale
        uci_data = {
            'title': 'UCI Machine Learning Repository Datasets',
            'url': url,
            'scraped_at': time.strftime('%Y-%m-%d %H:%M:%S'),
            'total_datasets': len(datasets),
            'headers': headers,
            'datasets': datasets[:50]  # Limiter à 50 pour éviter des fichiers trop lourds
        }
        
        # Sauvegarder en JSON
        with open('data/uci_datasets.json', 'w', encoding='utf-8') as f:
            json.dump(uci_data, f, indent=2, ensure_ascii=False)
        
        print(f"✅ {len(datasets)} datasets extraits")
        print(f"Fichier créé: uci_datasets.json")
        
    except Exception as e:
        print(f"❌ Erreur lors du scraping UCI: {e}")
        error_data = {'error': str(e), 'url': url}
        with open('uci_datasets.json', 'w', encoding='utf-8') as f:
            json.dump(error_data, f, indent=2, ensure_ascii=False)

# Exercice 3: Scraper la liste des présidents US
def scrape_us_presidents():
    """Scrape la liste des présidents américains de Wikipedia"""
    print("\n********Exercice 3: Scraping US Presidents********")
    
    url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'

    
    try:
        print("⏳ Scraping en cours (peut prendre du temps)...")
        response = requests.get(url, timeout=20)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        presidents = []
        
        # Chercher la table des présidents (généralement la première grande table)
        tables = soup.find_all('table', class_='wikitable')
        
        main_table = None
        for table in tables:
            # Chercher une table qui contient des informations sur les présidents
            if table.find('th') and ('president' in str(table).lower() or 'term' in str(table).lower()):
                main_table = table
                break
        
        if not main_table and tables:
            main_table = tables[0]  # Prendre la première table wikitable
        
        if main_table:
            rows = main_table.find_all('tr')
            
            for i, row in enumerate(rows):
                cells = row.find_all(['td', 'th'])
                
                if len(cells) >= 3:  # Au moins 3 colonnes pour avoir des données utiles
                    president = {}
                    
                    # Extraire les informations de base
                    for j, cell in enumerate(cells[:10]):  # Limiter à 10 colonnes max
                        text = cell.get_text(strip=True)
                        text = re.sub(r'\[\d+\]', '', text)  # Supprimer les références [1], [2], etc.
                        
                        # Colonnes typiques d'une table de présidents
                        column_names = ['Number', 'Portrait', 'Name', 'Term_Start', 'Term_End', 
                                      'Party', 'Vice_President', 'Prior_Office', 'Age', 'State']
                        
                        if j < len(column_names):
                            president[column_names[j]] = text
                    
                    # Extraire les images si présentes
                    img = row.find('img')
                    if img:
                        president['Portrait_URL'] = img.get('src', '')
                    
                    # Nettoyer et valider les données
                    if president.get('Name') and len(president.get('Name', '')) > 1:
                        # Nettoyer le nom (supprimer les numéros, références, etc.)
                        name = president.get('Name', '')
                        name = re.sub(r'^\d+\.?\s*', '', name)  # Supprimer les numéros au début
                        president['Name'] = name
                        
                        presidents.append(president)
        
        # Structure finale
        presidents_data = {
            'title': 'List of Presidents of the United States',
            'url': url,
            'scraped_at': time.strftime('%Y-%m-%d %H:%M:%S'),
            'total_presidents': len(presidents),
            'presidents': presidents
        }
        
        # Sauvegarder en JSON
        with open('data/us_presidents.json', 'w', encoding='utf-8') as f:
            json.dump(presidents_data, f, indent=2, ensure_ascii=False)
        
        print(f"✅ {len(presidents)} présidents extraits")
        print(f"Fichier créé: data/us_presidents.json")

        # Afficher les premiers résultats pour vérification
        if presidents:
            print("\n📋 Premiers présidents extraits:")
            for i, p in enumerate(presidents[:3]):
                print(f"  {i+1}. {p.get('Name', 'N/A')}")
        
    except Exception as e:
        print(f"❌ Erreur lors du scraping des présidents: {e}")
        error_data = {'error': str(e), 'url': url}
        with open('us_presidents.json', 'w', encoding='utf-8') as f:
            json.dump(error_data, f, indent=2, ensure_ascii=False)

# Afficher un résumé des données JSON
def main():
    print("Day 22 - Web Scraping avec BeautifulSoup")
    print("******************************************************************")
    
    # Exécuter les exercices
    scrape_boston_university()
    time.sleep(2)  # Pause entre les requêtes
    print("******************************************************************")
    scrape_uci_datasets()
    time.sleep(2)  # Pause entre les requêtes
    print("******************************************************************")
    scrape_us_presidents()
    

if __name__ == "__main__":
    main()