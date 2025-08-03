#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 12 : Modules
Exercices sur les modules Python
"""

import random
import string

## Générer un ID utilisateur aléatoire de 6 caractères
def random_user_id():
    """Génère un ID utilisateur aléatoire de 6 caractères alphanumériques"""
    # Combinaison de lettres minuscules, majuscules et chiffres
    characters = string.ascii_letters + string.digits
    user_id = ''.join(random.choice(characters) for _ in range(6))
    return user_id

## Générer plusieurs IDs selon les paramètres de l'utilisateur
def user_id_gen_by_user():
    """
    Demande à l'utilisateur le nombre de caractères et le nombre d'IDs à générer
    Génère et affiche les IDs correspondants
    """
    try:
        num_chars = int(input("Entrez le nombre de caractères pour chaque ID: "))
        num_ids = int(input("Entrez le nombre d'IDs à générer: "))
        
        # Validation des entrées
        if num_chars <= 0 or num_ids <= 0:
            print("Les nombres doivent être positifs")
            return
        
        # Génération des IDs
        characters = string.ascii_letters + string.digits
        print(f"\nGénération de {num_ids} IDs de {num_chars} caractères:")
        for _ in range(num_ids):
            user_id = ''.join(random.choice(characters) for _ in range(num_chars))
            print(user_id)
            
    except ValueError:
        print("Veuillez entrer des nombres valides")

## Générer une couleur RGB aléatoire
def rgb_color_gen():
    """Génère une couleur RGB aléatoire avec des valeurs entre 0 et 255"""
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return f"rgb({red},{green},{blue})"

#### Exercice 2
# Générer une liste de couleurs hexadécimales
def list_of_hexa_colors(num_colors):
    """Retourne une liste de couleurs hexadécimales aléatoires"""
    hexa_colors = []
    hex_chars = "0123456789abcdef"
    
    for _ in range(num_colors):
        # Générer 6 caractères hexadécimaux aléatoirement
        color = "#" + ''.join(random.choice(hex_chars) for _ in range(6))
        hexa_colors.append(color)
    
    return hexa_colors

## Générer une liste de couleurs RGB
def list_of_rgb_colors(num_colors):
    """Retourne une liste de couleurs RGB aléatoires"""
    rgb_colors = []
    
    for _ in range(num_colors):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        rgb_colors.append(f"rgb({red},{green},{blue})")
    
    return rgb_colors

## Générer des couleurs selon le type spécifié
def generate_colors(color_type, num_colors):
    """
    Génère des couleurs selon le type spécifié ('hex' ou 'rgb')
    
    Args:
        color_type (str): Type de couleur ('hex' ou 'rgb')
        num_colors (int): Nombre de couleurs à générer
    
    Returns:
        list: Liste des couleurs générées
    """
    if color_type.lower() == 'hex':
        return list_of_hexa_colors(num_colors)
    elif color_type.lower() == 'rgb':
        return list_of_rgb_colors(num_colors)
    else:
        return f"Type de couleur non supporté. Utilisez 'hex' ou 'rgb'"

#### Exercice 3

## 1: Mélanger une liste
def shuffle_list(original_list):
    """
    Prend une liste comme paramètre et retourne une liste mélangée
    
    Args:
        original_list (list): Liste à mélanger
    
    Returns:
        list: Nouvelle liste mélangée (sans modifier l'originale)
    """
    # Créer une copie de la liste pour ne pas modifier l'originale
    shuffled = original_list.copy()
    random.shuffle(shuffled)
    return shuffled

## 2: Générer 7 nombres uniques entre 0-9
def generate_unique_numbers():
    """
    Retourne un tableau de 7 nombres aléatoires uniques dans la plage 0-9
    
    Returns:
        list: Liste de 7 nombres uniques entre 0 et 9
    """
    # Créer une liste des nombres de 0 à 9
    numbers = list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    # Utiliser random.sample pour sélectionner 7 nombres uniques
    unique_numbers = random.sample(numbers, 7)
    
    return unique_numbers