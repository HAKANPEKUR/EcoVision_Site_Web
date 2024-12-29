# Partie 2 : Serveurs RESTful

Cette partie explique la mise en place et l'utilisation des serveurs RESTful pour différentes fonctionnalités du projet. Elle couvre les exercices 2.1 à 2.4.

---

## **Exercice 2.1 : Remplissage de la base de données**

### Objectif
Remplir la base de données via des requêtes REST (GET et POST) pour simuler l'insertion dynamique des données.

### Fonctionnalité
Le script `remplissage_python.py` permet d'insérer des données aléatoires dans les tables `Mesure` et `Facture`. 

- **Requête GET** : Permet de récupérer les données de la base.
- **Requête POST** : Utilisée pour insérer de nouvelles données.

Le code correspondant se trouve dans le fichier **Serveur_Capteur.py**. Consultez ce fichier pour le détail des fonctions utilisées.

---

## **Exercice 2.2 : Serveur Web**

### Objectif
Créer une API RESTful qui génère un graphique en camembert représentant les factures par type.

### Fonctionnalité
Le fichier **Serveur_Camembert.py** génère une page HTML avec un graphique interactif. Voici les détails :
- **Route GET** : `/api/factures/chart` : Génère un camembert basé sur les factures stockées dans la base de données.
- **Technologie utilisée** : Google Charts pour le rendu graphique.
- **Port** : `8001`.

### Exemple d'accès
Lancez le serveur via :
```bash
python Serveur_Camembert.py
```
Ouvrez votre navigateur et accédez à `http://localhost:8001/api/factures/chart` pour voir le graphique.

---

## **Exercice 2.3 : Météo**

### Objectif
Afficher les prévisions météo pour plusieurs jours et fournir des recommandations adaptées pour les actions éco-responsables.

### Fonctionnalité
Le fichier **Serveur_Meteo.py** permet de :
- Récupérer les prévisions météo sur 5 jours via l'API d'OpenWeatherMap.
- Générer des recommandations dynamiques pour les logements (exemple : "Protégez vos plantes des gelées").
- Afficher les données météo et recommandations dans un tableau HTML.

### Exemple d'accès
Lancez le serveur via :
```bash
python Serveur_Meteo.py
```
Ouvrez votre navigateur et accédez à `http://localhost:8003/meteo` pour afficher les prévisions et recommandations.

---

## **Exercice 2.4 : Intégration**

### Objectif
Utiliser les données des capteurs et des prévisions météo pour prendre des décisions dynamiques (exemple : allumer une LED si la température extérieure dépasse un certain seuil).

### Fonctionnalité
Le fichier **Serveur_Capteur.py** intègre :
- La récupération de la température extérieure via l'API météo.
- La simulation des données de capteurs DHT22 pour température et humidité.
- Une action conditionnelle (allumage d'une LED) basée sur la température extérieure.

### Exemple d'accès
Lancez le serveur via :
```bash
python Serveur_Capteur.py
```
Ouvrez votre navigateur et accédez à `http://localhost:8002/api/sensor` pour afficher les données des capteurs et l'état de la LED.

