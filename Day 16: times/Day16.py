#### Day 16 : DATETIME MODULE

from datetime import datetime, date, time, timedelta
import time as time_module

print("**************************************************************************")
# 1. Afficher les informations de date/heure actuelles
print("**************************************************************************")
print("1. Informations date/heure actuelles:")
now = datetime.now()
print(f"Date et heure complètes: {now}")
print(f"Jour: {now.day}")
print(f"Mois: {now.month}")
print(f"Année: {now.year}")
print(f"Heure: {now.hour}")
print(f"Minute: {now.minute}")
print(f"Seconde: {now.second}")
print(f"Timestamp: {now.timestamp()}")

# 2. écrire la date actuelle dans un format personnalisé %m/%d/%Y, %H:%M:%S
print("***************************************************************************")
print("2. Format de date personnalisée :")
formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print(f"Date formatée: {formatted_date}")

# Autres formats trouvées
print("****************************************************************************")
print(f"Format français: {now.strftime('%d/%m/%Y, %H:%M:%S')}")
print(f"Format long: {now.strftime('%A %d %B %Y, %H:%M:%S')}")


# 3. Today is 5 December, 2019. Change this time string to time.
print("****************************************************************************")
print("3. Conversion d'une chaîne de date en objet datetime:")

date_string = "5 December, 2019"
print(f"Chaîne originale: {date_string}")
date_object = datetime.strptime(date_string, "%d %B, %Y")
print(f"Objet datetime: {date_object}")
print(f"Type: {type(date_object)}")

# 4. Calculer la différence de temps entre maintenant et le nouvel an
print("****************************************************************************")
print("4. Différence de temps entre maintenant et le nouvel an:")
# Nouvel an prochain
current_year = now.year
next_new_year = datetime(current_year + 1, 1, 1)

# Si on est déjà en janvier, prendre le nouvel an de l'année suivante
if now.month == 1 and now.day == 1:
    next_new_year = datetime(current_year + 1, 1, 1)

time_to_new_year = next_new_year - now
print(f"   Prochain Nouvel An: {next_new_year.strftime('%d/%m/%Y %H:%M:%S')}")
print(f"   Temps restant: {time_to_new_year}")


# 5. Calculate the time difference between 1 January 1970 and now.
print("****************************************************************************")
print("5. Différence de temps entre le 1er janvier 1970 et maintenant:")

time_start = datetime(1970, 1, 1)
time_since_epoch = now - time_start

print(f"Époque Unix (1970-01-01): {time_start}")
print(f"Maintenant: {now}")
print(f"Temps écoulé depuis l'époque: {time_since_epoch}")

# 6. Applications du module datetime
print("****************************************************************************")
print("6. Applications du module datetime:")

print("\n   a) Time series analysis (Analyse de séries temporelles):")
# Exemple: données de ventes par jour
sales_data = [
    (datetime(2024, 1, 1), 1500),
    (datetime(2024, 1, 2), 1800),
    (datetime(2024, 1, 3), 1200),
    (datetime(2024, 1, 4), 2100),
    (datetime(2024, 1, 5), 1900)
]

print("   Données de ventes:")
for date, sales in sales_data:
    print(f"     {date.strftime('%Y-%m-%d')}: {sales}€")

# Calcul de tendance
total_days = (sales_data[-1][0] - sales_data[0][0]).days + 1
total_sales = sum(sale[1] for sale in sales_data)
avg_daily_sales = total_sales / len(sales_data)
print(f"   Ventes moyennes par jour: {avg_daily_sales:.2f}€")

print("\n   b) Timestamp pour activités d'application:")
class ActivityLogger:
    def __init__(self):
        self.activities = []
    
    def log_activity(self, activity):
        timestamp = datetime.now()
        self.activities.append((timestamp, activity))
        print(f"     [{timestamp.strftime('%Y-%m-%d %H:%M:%S')}] {activity}")
    
    def show_activities(self):
        print("   Historique des activités:")
        for timestamp, activity in self.activities:
            print(f"     {timestamp.strftime('%d/%m/%Y %H:%M:%S')} - {activity}")

# Demo du logger
logger = ActivityLogger()
logger.log_activity("Utilisateur connecté")
time_module.sleep(1)  # Petite pause pour différencier les timestamps
logger.log_activity("Page d'accueil visitée")
logger.log_activity("Profil mis à jour")

print("\n   c) Posts de blog avec timestamps:")
class BlogPost:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.created_at = datetime.now()
        self.updated_at = self.created_at
    
    def update_content(self, new_content):
        self.content = new_content
        self.updated_at = datetime.now()
    
    def time_since_creation(self):
        return datetime.now() - self.created_at
    
    def display(self):
        print(f"     Titre: {self.title}")
        print(f"     Créé le: {self.created_at.strftime('%d/%m/%Y à %H:%M')}")
        print(f"     Modifié le: {self.updated_at.strftime('%d/%m/%Y à %H:%M')}")
        time_diff = self.time_since_creation()
        if time_diff.days > 0:
            print(f"     Il y a {time_diff.days} jour(s)")
        elif time_diff.seconds > 3600:
            print(f"     Il y a {time_diff.seconds // 3600} heure(s)")
        else:
            print(f"     Il y a {time_diff.seconds // 60} minute(s)")

# Demo des posts de blog
post1 = BlogPost("Challenge 30 days Python", "Python est un langage formidable...")
time_module.sleep(2)
post1.update_content("Python est un langage de programmation puissant et facile à apprendre...")

print("   Post de blog:")
post1.display()