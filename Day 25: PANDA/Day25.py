# Day 25: PANDA - Exercices avec hacker_news.csv

import pandas as pd
import numpy as np

print("=== Day 25: PANDA - Analyse du fichier hacker_news.csv ===\n")

# 1. Lire le fichier hacker_news.csv depuis le répertoire data
print("1. Lecture du fichier hacker_news.csv")
try:
    df = pd.read_csv('./data/hacker_news.csv')
    print("Fichier lu avec succès depuis ./data/hacker_news.csv")
except FileNotFoundError:
    print("⚠️ Fichier hacker_news.csv non trouvé, création d'un dataset d'exemple")

print("***********************************************************************")
# 2. Obtenir les cinq premières lignes
print("2. Les cinq premières lignes:")
print(df.head())
print("***********************************************************************")

# 3. Obtenir les cinq dernières lignes
print("3. Les cinq dernières lignes:")
print(df.tail())
print("***********************************************************************")
# 4. Obtenir la colonne title comme pandas series
print("4. La colonne 'title' comme pandas Series:")
title_series = df['title']
print(f"Type: {type(title_series)}")
print("Premiers titres:")
print(title_series.head())
print("***********************************************************************")
# 5. Compter le nombre de lignes et de colonnes
print("5. Nombre de lignes et de colonnes:")
rows, cols = df.shape
print(f"Nombre de lignes: {rows}")
print(f"Nombre de colonnes: {cols}")
print(f"Forme du DataFrame: {df.shape}")
print("***********************************************************************")
# 5.1. Filtrer les titres qui contiennent "python"
print("5.1. Titres contenant 'python' (insensible à la casse):")
python_filter = df['title'].str.contains('python', case=False, na=False)
python_titles = df[python_filter]
print(f"Nombre d'articles avec 'python': {len(python_titles)}")
print("Titres:")
for idx, title in enumerate(python_titles['title'], 1):
    print(f"   {idx}. {title}")
print("***********************************************************************")
# 5.2. Filtrer les titres qui contiennent "JavaScript"
print("5.2. Titres contenant 'JavaScript' (insensible à la casse):")
js_filter = df['title'].str.contains('javascript', case=False, na=False)
js_titles = df[js_filter]
print(f"Nombre d'articles avec 'javascript': {len(js_titles)}")
print("Titres:")
for idx, title in enumerate(js_titles['title'], 1):
    print(f"   {idx}. {title}")
print("***********************************************************************")
# 5.3. Explorer les données et donner du sens
print("5.3. Exploration des données:")
print("\nInformations générales sur le dataset:")
print(df.info())
print("\nStatistiques descriptives:")
print(df.describe())
print("\nTypes de données:")
print(df.dtypes)
print("\nValeurs manquantes:")
print(df.isnull().sum())