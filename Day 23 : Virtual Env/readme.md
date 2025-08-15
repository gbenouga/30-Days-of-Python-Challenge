# Day 23: Virtual Environment

Ce projet Python du **Day 23** montre comment utiliser les environnements virtuels pour isoler les dépendances d'un projet.

## Fichier principal

- **Day23.py** : Script principal illustrant la création et l'utilisation d'un environnement virtuel.

## Instructions

1. Créez un environnement virtuel :
    ```bash
    python -m venv venv
    ```
2. Activez l'environnement :
    - Sur Windows :
      ```bash
      venv\Scripts\activate
      ```
    - Sur macOS/Linux :
      ```bash
      source venv/bin/activate
      ```
3. Installez les dépendances nécessaires :
    ```bash
    pip install -r requirements.txt
    ```
4. Exécutez le script :
    ```bash
    python Day23.py
    ```

## Objectif

Apprendre à :
- Créer et activer un environnement virtuel
- Gérer les dépendances d’un projet Python
- Exécuter un script dans un environnement isolé

## Ressources

- [Documentation officielle Python venv](https://docs.python.org/fr/3/library/venv.html)
- [Guide sur les environnements virtuels](https://realpython.com/python-virtual-environments-a-primer/)
