# Day 12 : Modules - Exercices Level 1, Level 2 et Level 3
import random
import string

from imports import user

# Tests des fonctions
if __name__ == "__main__":
    print("****Exercices 1****")
    print('****************************************************************************')
    print("1. Génération d'un ID utilisateur aléatoire de 6 caractères:")
    print(f"  Identifiant généré : {user.random_user_id()}")
    print('****************************************************************************')
    print("2. Génération de plusieurs IDs selon les paramètres de l'utilisateur")
    print("   (Fonction interactive - décommentez user.user_id_gen_by_user() pour tester)")
    # user.user_id_gen_by_user()
    print('****************************************************************************')
    print("3. Génération de couleurs RGB aléatoires:")
    print(f"   Couleur générée : {user.rgb_color_gen()}")
    print('****************************************************************************')
    
    print("\n****Exercice 2****")
    print('****************************************************************************')
    print("1. Génération d'une liste de couleurs hexadécimales:")
    hexa_colors = user.list_of_hexa_colors(5)
    print(f" 5 couleurs hexadécimales : {hexa_colors}")
    print('****************************************************************************')
    print("2. Génération d'une liste de couleurs RGB:")
    rgb_colors = user.list_of_rgb_colors(3)
    print(f" 3 couleurs RGB : {rgb_colors}")
    print('****************************************************************************')
    print("3. Génération de couleurs avec generate_colors():")
    print(f"   generate_colors('hex', 3) : {user.generate_colors('hex', 3)}")
    print(f"   generate_colors('hex', 1) : {user.generate_colors('hex', 1)}")
    print(f"   generate_colors('rgb', 3) : {user.generate_colors('rgb', 3)}")
    print(f"   generate_colors('rgb', 1) : {user.generate_colors('rgb', 1)}")
    print('****************************************************************************')
    
    print("\n*****Exercice 3*****")
    print('****************************************************************************')
    print("1. Mélanger une liste avec shuffle_list():")
    original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    shuffled = user.shuffle_list(original_list)
    print(f"   Liste originale : {original_list}")
    print(f"   Liste mélangée  : {shuffled}")
    print('****************************************************************************')
    print("2. Générer 7 nombres uniques entre 0-9:")
    for i in range(3):  # Générer 3 exemples
        unique_nums = user.generate_unique_numbers()
        print(f"   Exemple {i+1} : {unique_nums} (longueur: {len(unique_nums)})")
    print('****************************************************************************')
