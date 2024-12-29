# TP IOT : EcoVision - Logement Éco-Responsable

Ce TP propose une solution web pour gérer un logement éco-responsable. Il inclut un site web interactif et des serveurs backend pour collecter et afficher les données en temps réel.

## **Contenu de l'archive**

### **Arborescence générale**
- **eco_responsable_site** (Dossier principal)
  - **assets** (Contient les ressources du site)
    - **css**
      - `style.css` : Fichier de styles CSS du site web.
    - **images**
      - Contient toutes les images utilisées pour le site (logos, illustrations, etc.).
    - **js**
      - `capteurs.js` : Fichier JavaScript pour gérer les données des capteurs.
      - `configuration.js` : Fichier JavaScript pour gérer les configurations.
      - `consommation.js` : Fichier JavaScript pour gérer les données de consommation.
      - `economies.js` : Fichier JavaScript pour visualiser les économies réalisées.
  - **backend** (Contient les fichiers Python pour les serveurs et la base de données)
    - `all_serveur.py` : Script pour lancer tous les serveurs simultanément.
    - `database.db` : Base de données SQLite contenant les données du projet.
    - `logement.sql` : Script SQL pour initialiser la base de données.
    - `main.py` : Script principal pour tester le backend.
    - `remplissage_python.py` : Script Python pour remplir la base de données avec des données initiales.
    - `Serveur_Camembert.py` : Serveur pour les graphiques camembert des économies.
    - `Serveur_Capteur.py` : Serveur pour gérer les données des capteurs.
    - `Serveur_Meteo.py` : Serveur pour interagir avec les API météo.
  - **Pages HTML**
    - `index.html` : Page d'accueil du site web.
    - `capteurs.html` : Page de gestion des capteurs et actionneurs.
    - `configuration.html` : Page pour configurer le logement.
    - `consommation.html` : Page pour visualiser les consommations.
    - `economies.html` : Page pour afficher les économies réalisées.
  - **Documentation**
    - `markdown.md` : Fichier expliquant le contenu global de l'archive
    - `Partie1.md` : Fichier expliquant la partie 1 du TP
    - `Partie2.md` : Fichier expliquant la partie 2 du TP

---

## Prérequis pour le bon fonctionnement

### 1. Logiciels nécessaires
Pour exécuter ce projet sur un autre poste, vous devez installer les logiciels suivants :
- **Python 3.11 ou version supérieure** (indispensable pour exécuter le backend)
- **Visual Studio Code** (recommandé pour modifier ou exécuter le projet)
- **Un navigateur web** (comme Google Chrome, Firefox...) pour afficher le site.

### 2. Dépendances Python
Vous devez installer les bibliothèques suivantes pour que le backend fonctionne correctement. Exécutez les commandes suivantes dans un terminal :

```bash
pip install fastapi==0.88.0
pip install uvicorn==0.20.0
pip install jinja2==3.1.2
pip install requests==2.28.1
```
### 3. Lancement du site web avec les serveurs
1. Dans un premier temps, il faut faire la connexion à la base de données :
- **Ouvrez un premier terminal et placez-vous dans le dossier backend** : cd backend
- **Lancez le fichier "main.py"** : python main.py
2. Dans un second temps, il faut lancer les serveurs déjà existants via le fichier "all_serveur.py" :
- **Dans un nouveau terminal, placez-vous dans le dossier backend également, puis tapez** : python all_serveur.py
3. Nous pouvons accéder au site web en ouvrant le fichier **index.html** dans un navigateur web comme Google Chrome.

### Notes importantes
- Assurez-vous de lancer tous les serveurs avant d’accéder au site web pour que toutes les fonctionnalités (graphiques, données météo, etc.) fonctionnent correctement.
- Ce TP est configuré pour fonctionner en local.

### Auteur
- Hakan PEKUR
- Numéro étudiant : 21301964
- Groupe : TP-D2