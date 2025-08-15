#### Day 23 : Virtual Env
# Script pour créer un environnement virtuel Python et y installer Flask

import os
import subprocess
import sys

# Nom du dossier de l'environnement
env_name = "venv"

# 1. Créer l'environnement virtuel
print("*************************************************************************")
print(f"📦 Création de l'environnement virtuel '{env_name}'...")
subprocess.check_call([sys.executable, "-m", "venv", env_name])

# 2. Déterminer le chemin vers pip dans l'env
if os.name == "nt":  # Windows
    pip_path = os.path.join(env_name, "Scripts", "pip")
else:  # Linux / macOS
    pip_path = os.path.join(env_name, "bin", "pip")

# 3. Installer Flask
print("*************************************************************************")
print("📥 Installation de Flask...")
subprocess.check_call([pip_path, "install", "flask"])
print("*************************************************************************")
print("✅ Environnement prêt !")
print(f"Pour l'activer :\n  Windows : {env_name}\\Scripts\\activate\n  Linux/Mac : source {env_name}/bin/activate")
