#### Day 19 : FILE HANDLING
import json
import os
from collections import Counter
import re

print("*******************************************************************")
# 1. Fonction pour compter les lignes et les mots dans un fichier texte
print("1. Comptage de lignes et mots dans les fichiers texte:")
def count_lines_and_words(filename):
    """
    Compte le nombre de lignes et de mots dans un fichier texte
    Retourne: (nombre_lignes, nombre_mots)
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            line_count = len(lines)
            
            # Compter les mots
            word_count = 0
            for line in lines:
                words = line.split()
                word_count += len(words)
            
            return line_count, word_count
    
    except FileNotFoundError:
        print(f"Fichier '{filename}' non trouvé")
        return 0, 0
    except Exception as e:
        print(f"Erreur lors de la lecture de '{filename}': {e}")
        return 0, 0

# Créer le dossier data s'il n'existe pas
data_dir = "./data"
if not os.path.exists(data_dir):
    os.makedirs(data_dir)
    print(f"Dossier '{data_dir}' créé")

# Fichiers de discours à analyser
speech_files = [
    'obama_speech.txt',
    'michelle_obama_speech.txt',
    'donald_speech.txt',
    'melina_trump_speech.txt'
]

# Créer des fichiers d'exemple s'ils n'existent pas
sample_speeches = {
    'obama_speech.txt': '''My fellow Americans, tonight I want to speak to you about what the United States will do with our friends and allies to degrade and ultimately destroy the terrorist group known as ISIL.

As Commander-in-Chief, my highest priority is the security of the American people.

Over the last several years, we have consistently taken the fight to terrorists who threaten our country.

We took out Osama bin Laden and much of al Qaeda's leadership in Afghanistan and Pakistan.

We've targeted al Qaeda's affiliate in Yemen, and recently eliminated the top commander of its affiliate in Somalia.''',
    
    'michelle_obama_speech.txt': '''Thank you so much, everyone. Thank you for that very kind introduction.

When I first met Barack, he took me on a date to a community meeting.

I know, how romantic, right?

But when we walked in, Barack immediately went up to this group of older women who were sitting in the front row.

And he sat down and he started talking and listening to what they had to say.''',
    
    'donald_speech.txt': '''My fellow Americans: Today, I want to tell the world that America First does not mean America alone.

When the United States grows, so does the world.

American prosperity has created countless jobs all around the globe.

And the drive for excellence, creativity, and innovation in the U.S. has led to important discoveries that help people everywhere live more prosperous and far healthier lives.''',
    
    'melina_trump_speech.txt': '''Thank you very much. One year ago, I introduced my husband when he declared his candidacy.

Here we are again. This time as the Republican nominee for President of the United States of America.

From the bottom of my heart, I want to thank you for your support.

It is an honor to be here tonight and to share the stage with my husband who I love very much.'''
}

# Créer les fichiers d'exemple
for filename, content in sample_speeches.items():
    filepath = os.path.join(data_dir, filename)
    if not os.path.exists(filepath):
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fichier d'exemple '{filename}' créé")

# Analyser chaque fichier de discours
print("********************************************************************")
print("Analyse des fichiers de discours:")
for filename in speech_files:
    filepath = os.path.join(data_dir, filename)
    lines, words = count_lines_and_words(filepath)
    print(f"{filename}:")
    print(f"Lignes: {lines}")
    print(f"Mots: {words}")

print(f"*********************************************************************")
# 2. Fonction pour trouver les langues les plus parlées
print("2. Langues les plus parlées dans le monde:")
def most_spoken_languages(filename, top_n=10):
    """
    Trouve les langues les plus parlées à partir du fichier countries_data.json
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            countries = json.load(file)
        
        # Compter toutes les langues
        language_count = Counter()
        
        for country in countries:
            if 'languages' in country:
                for language in country['languages']:
                    language_count[language] += 1
        
        # Retourner les top_n langues les plus parlées
        return language_count.most_common(top_n)
    
    except FileNotFoundError:
        print(f"Fichier '{filename}' non trouvé")
        return []
    except json.JSONDecodeError:
        print(f"Erreur de format JSON dans '{filename}'")
        return []
    except Exception as e:
        print(f"Erreur: {e}")
        return []

# 3. Fonction pour trouver les pays les plus peuplés
print("3. Pays les plus peuplés:")
def most_populated_countries(filename, top_n=10):
    """
    Trouve les pays les plus peuplés à partir du fichier countries_data.json
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            countries = json.load(file)
        
        # Trier par population (décroissant)
        sorted_countries = sorted(countries, 
                                key=lambda x: x.get('population', 0), 
                                reverse=True)
        
        # Retourner les top_n pays avec seulement nom et population
        result = []
        for country in sorted_countries[:top_n]:
            result.append({
                'country': country.get('name', 'Unknown'),
                'population': country.get('population', 0)
            })
        
        return result
    
    except FileNotFoundError:
        print(f"Fichier '{filename}' non trouvé")
        return []
    except json.JSONDecodeError:
        print(f"Erreur de format JSON dans '{filename}'")
        return []
    except Exception as e:
        print(f"Erreur: {e}")
        return []

# Créer un fichier countries_data.json d'exemple
countries_data_file = os.path.join(data_dir, 'countries_data.json')

if not os.path.exists(countries_data_file):
    # Données d'exemple (extrait simplifié)
    sample_countries_data = [
        {
            "name": "China",
            "population": 1377422166,
            "languages": ["Chinese"]
        },
        {
            "name": "India", 
            "population": 1295210000,
            "languages": ["Hindi", "English"]
        },
        {
            "name": "United States of America",
            "population": 323947000,
            "languages": ["English"]
        },
        {
            "name": "Indonesia",
            "population": 258705000,
            "languages": ["Indonesian"]
        },
        {
            "name": "Brazil",
            "population": 206135893,
            "languages": ["Portuguese"]
        },
        {
            "name": "Pakistan",
            "population": 194125062,
            "languages": ["English", "Urdu"]
        },
        {
            "name": "Nigeria",
            "population": 186988000,
            "languages": ["English"]
        },
        {
            "name": "Bangladesh",
            "population": 161006790,
            "languages": ["Bengali"]
        },
        {
            "name": "Russian Federation",
            "population": 146599183,
            "languages": ["Russian"]
        },
        {
            "name": "Japan",
            "population": 126960000,
            "languages": ["Japanese"]
        },
        {
            "name": "France",
            "population": 66710000,
            "languages": ["French"]
        },
        {
            "name": "Germany",
            "population": 82175700,
            "languages": ["German"]
        },
        {
            "name": "Spain",
            "population": 46438422,
            "languages": ["Spanish"]
        },
        {
            "name": "Canada",
            "population": 36290000,
            "languages": ["English", "French"]
        },
        {
            "name": "Morocco",
            "population": 34377511,
            "languages": ["Arabic", "French"]
        }
    ]
    
    with open(countries_data_file, 'w', encoding='utf-8') as f:
        json.dump(sample_countries_data, f, indent=2, ensure_ascii=False)
    print(f"Fichier d'exemple 'countries_data.json' créé")

print(f"main")
print("*********************************************************************")
print("\nTop 10 des langues les plus parlées:")
top_languages_10 = most_spoken_languages(countries_data_file, 10)
for count, language in top_languages_10:
    print(f"   ({count}, '{language}')")

print(f"\nTop 3 des langues les plus parlées:")
top_languages_3 = most_spoken_languages(countries_data_file, 3)
for count, language in top_languages_3:
    print(f"   ({count}, '{language}')")

print(f"\nTop 10 des pays les plus peuplés:")
top_countries_10 = most_populated_countries(countries_data_file, 10)
for country_data in top_countries_10:
    print(f"   {{'country': '{country_data['country']}', 'population': {country_data['population']}}}")

print

print("**********Exercice 2**********")

# 4. extraction d'adresses email depuis un fichier
print("*********************************************************************")
print("4. Extraction d'adresses email depuis un fichier:")

def extract_email_addresses(filename):
    """
    Extrait toutes les adresses email d'un fichier texte
    Retourne une liste d'adresses email uniques
    """
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = []
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            
        # Trouver toutes les adresses email
        found_emails = re.findall(email_pattern, content)
        
        # Supprimer les doublons en gardant l'ordre
        seen = set()
        for email in found_emails:
            email_lower = email.lower()
            if email_lower not in seen:
                emails.append(email)
                seen.add(email_lower)
        
        return emails
    
    except FileNotFoundError:
        print(f"Fichier '{filename}' non trouvé")
        return []
    except Exception as e:
        print(f"Erreur: {e}")
        return []

# Créer un fichier d'exemple email_exchange_big.txt
email_file = os.path.join(data_dir, 'email_exchange_big.txt')

if not os.path.exists(email_file):
    sample_email_content = '''From: john.doe@company.com
To: jane.smith@example.org, mike.wilson@test.net
Cc: admin@company.com, support@helpdesk.co.uk
Subject: Weekly Report

Hello team,

Please find the weekly report attached. For any questions, contact me at john.doe@company.com 
or reach out to our support team at support@helpdesk.co.uk.

You can also contact:
- Sales: sales@company.com
- Marketing: marketing@company.com  
- HR: hr@company.com
- Technical Support: tech.support@company.com

Best regards,
John Doe
john.doe@company.com

---
From: jane.smith@example.org
To: all-staff@company.com
Subject: Meeting Tomorrow

Hi everyone,

Don't forget about tomorrow's meeting. Please confirm your attendance by sending an email to 
meeting-organizer@company.com.

For remote participants, join via: video.conf@company.com
Technical issues? Contact: it-support@company.com

Thanks,
Jane Smith
jane.smith@example.org

---
From: admin@company.com
To: john.doe@company.com, jane.smith@example.org
Subject: System Maintenance

Dear users,

System maintenance is scheduled for this weekend. 
Contact emergency@company.com for urgent issues.

Admin Team
admin@company.com

P.S: Invalid emails like not-an-email, @invalid.com, and user@ should be ignored.
'''
    
    with open(email_file, 'w', encoding='utf-8') as f:
        f.write(sample_email_content)
    print(f"Fichier d'exemple 'email_exchange_big.txt' créé")

# Extraire les adresses email
print(f"Extraction des adresses email depuis 'email_exchange_big.txt':")
extracted_emails = extract_email_addresses(email_file)

print(f"{len(extracted_emails)} adresses email trouvées:")
for i, email in enumerate(extracted_emails, 1):
    print(f"   {i:2d}. {email}")
print("*********************************************************************")

# 5. Afficher les mots les plus fréquents
print("5. Fonction find_most_common_words:")

def find_most_common_words(source, top_n=10):
    """
    Trouve les mots les plus fréquents dans un texte ou fichier
    
    Args:
        source: nom de fichier (str) ou contenu texte (str)
        top_n: nombre de mots les plus fréquents à retourner
        
    Returns:
        Liste de tuples (count, word) en ordre décroissant
    """
    try:
        # Déterminer si c'est un fichier ou du texte direct
        if os.path.isfile(source):
            # C'est un fichier
            with open(source, 'r', encoding='utf-8') as file:
                text = file.read()
        else:
            # C'est du texte direct
            text = source
        
        # Nettoyer le texte et extraire les mots
        # Convertir en minuscules et supprimer la ponctuation
        cleaned_text = re.sub(r'[^\w\s]', ' ', text.lower())
        words = cleaned_text.split()
        
        # Filtrer les mots vides courants (optionnel)
        # Pour cet exercice, on garde tous les mots
        
        # Compter la fréquence des mots
        word_count = Counter(words)
        
        # Retourner les top_n mots les plus fréquents
        return word_count.most_common(top_n)
    
    except FileNotFoundError:
        print(f"Fichier '{source}' non trouvé")
        return []
    except Exception as e:
        print(f"Erreur: {e}")
        return []

# Créer un fichier d'exemple sample.txt
sample_file = os.path.join(data_dir, 'sample.txt')

if not os.path.exists(sample_file):
    sample_text_content = '''The quick brown fox jumps over the lazy dog. The dog was lazy and the fox was quick.
To be or not to be, that is the question. To be happy is to be free.
The sun is bright and the sky is blue. The birds sing in the morning.
I have a dream that one day we will be free. I have hope and I have faith.
The cat sat on the mat. The mat was soft and the cat was comfortable.
And so it goes, and so it will be. The end of the story is near.
A bird in the hand is worth two in the bush. A friend in need is a friend indeed.
That is all I have to say about that. That was a long time ago.
The time has come to say goodbye. The time is now to make a change.
I will be back tomorrow. I will have the answer then.'''
    
    with open(sample_file, 'w', encoding='utf-8') as f:
        f.write(sample_text_content)
    print(f"Fichier d'exemple 'sample.txt' créé")

# Tester la fonction find_most_common_words
print(f"Top 10:")
result_10 = find_most_common_words(sample_file, 10)
for count, word in result_10:
    print(f"   ({count}, '{word}')")

print(f"Top 5:")
result_5 = find_most_common_words(sample_file, 5)
for count, word in result_5:
    print(f"   ({count}, '{word}')")