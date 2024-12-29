import subprocess
import time        
import os         

def main():
    """
    Cette fonction lance en parallèle 3 serveurs Python :
      - Serveur_Camembert.py sur port 8001
      - Serveur_Capteur.py   sur port 8002
      - Serveur_Meteo.py     sur port 8003
    """

    # Obtenir le répertoire du script actuel
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Liste des scripts à lancer
    servers = [
        "Serveur_Camembert.py",
        "Serveur_Capteur.py",
        "Serveur_Meteo.py"
    ]

    processes = []  # Liste pour stocker les processus en cours

    # Boucle pour lancer chaque serveur
    for script_name in servers:
        # Construire le chemin absolu du script
        script_path = os.path.join(base_dir, script_name)
        print(f"Démarrage de {script_name}...")

        # Lancer le script en tant que processus indépendant
        p = subprocess.Popen(["python", script_path])
        processes.append(p)  # Ajouter le processus à la liste

        # Ajouter un délai d'une seconde entre chaque lancement
        time.sleep(1)

    # Tous les serveurs sont démarrés
    print("\nTous les serveurs sont démarrés.\n")
    print("Pour arrêter, faire CTRL + C dans ce terminal.")

    # Attendre la fin de tous les processus
    for proc in processes:
        proc.wait()

# Point d'entrée du programme
if __name__ == "__main__":
    main()
