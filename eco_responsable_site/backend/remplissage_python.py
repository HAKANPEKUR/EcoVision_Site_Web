import sqlite3
import random
import os
from datetime import datetime, timedelta

# Récupérer le chemin absolu du dossier contenant ce script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Construire le chemin complet vers database.db (dans le même dossier)
db_path = os.path.join(BASE_DIR, "database.db")

# Connexion à la base de données
conn = sqlite3.connect(db_path)
conn.row_factory = sqlite3.Row
c = conn.cursor()

# Fonction pour générer une date aléatoire
def generate_random_date():
    return (datetime.now() - timedelta(days=random.randint(0, 30))).strftime('%Y-%m-%d %H:%M:%S')

# Insertion de mesures dans la table Mesure
def insert_measures():
    # On récupère tous les capteurs existants
    c.execute("SELECT id_capteur FROM Capteur_Actionneur")
    capteurs = c.fetchall()

    for capteur in capteurs:
        id_capteur = capteur['id_capteur']
        # Insérer deux mesures aléatoires pour chaque capteur
        for _ in range(2):
            valeur = round(random.uniform(10.0, 100.0), 2)  # Génère une valeur aléatoire entre 10 et 100
            date_insertion = generate_random_date()
            c.execute("""
                INSERT INTO Mesure (valeur, date_insertion, id_capteur)
                VALUES (?, ?, ?)
            """, (valeur, date_insertion, id_capteur))

# Insertion de factures dans la table Facture
def insert_bills():
    # On récupère tous les logements existants
    c.execute("SELECT id_logement FROM Logement")
    logements = c.fetchall()

    types_factures = ['Électricité', 'Eau', 'Gaz', 'Déchets']

    for logement in logements:
        id_logement = logement['id_logement']
        # Insérer une facture pour chaque type
        for type_facture in types_factures:
            montant = round(random.uniform(20.0, 150.0), 2)  # Montant aléatoire
            valeur_consomme = round(random.uniform(5.0, 100.0), 2)  # Consommation aléatoire
            date_facture = generate_random_date()
            c.execute("""
                INSERT INTO Facture (type, date, montant, valeur_consomme, id_logement)
                VALUES (?, ?, ?, ?, ?)
            """, (type_facture, date_facture, montant, valeur_consomme, id_logement))

# Exécuter les fonctions pour insérer des données
insert_measures()
insert_bills()

# Valider les changements et fermer la connexion
conn.commit()
conn.close()

print("Remplissage de la base de données terminé avec succès.")
