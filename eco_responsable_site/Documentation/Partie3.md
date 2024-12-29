# Partie 3 : Conception et Développement de l'Application Web

## Introduction

La **Partie 3** de ce TP consiste à concevoir et développer une application web permettant de gérer l’ensemble des fonctionnalités d’un logement éco-responsable. L’application est entièrement **responsive**, utilisant les fonctionnalités avancées de **HTML5**, **JavaScript**, et **Bootstrap** pour offrir une expérience utilisateur fluide et intuitive.


## Technologies Utilisées

- **HTML5** : Structure sémantique et moderne des pages web.
- **CSS3** : Stylisation et mise en page responsive avec des styles personnalisés.
- **JavaScript** : Interactivité et gestion dynamique des données.
- **Bootstrap 4.6.2** : Framework CSS pour faciliter le développement de sites web responsive et esthétiques.
- **SQLite** : Base de données légère pour stocker les informations sur les capteurs, consommations et économies.
- **Python (FastAPI)** : Backend pour gérer les requêtes API et l'interaction avec la base de données.

## Fonctionnalités des Pages

### 1. Page d’Accueil (`index.html`)

- **Présentation Générale** : Introduction à l’application EcoVision avec un slogan motivant.
- **Navigation Intuitive** : Barre de navigation permettant d'accéder facilement aux différentes sections.
- **Image de Fond Floutée** : Esthétique visuelle avec une image de fond légèrement floutée pour mettre en valeur le contenu.
- **Sections de Fonctionnalités** : Quatre cartes interactives menant aux pages spécifiques :
  - **Suivi en Temps Réel** : Accès aux données de consommation.
  - **Capteurs & Actionneurs** : Surveillance des dispositifs installés.
  - **Économies Réalisées** : Visualisation des économies via des graphiques.
  - **Configuration** : Gestion des paramètres utilisateurs et ajout de nouveaux capteurs/actionneurs.

### 2. Page de Consommation (`consommation.html`)

- **Graphiques Interactifs** : Visualisation des consommations d’électricité, d’eau et de déchets sur différentes échelles de temps (mensuelle, trimestrielle, annuelle).
- **Filtrage des Données** : Options pour filtrer les données selon les périodes souhaitées.
- **Actualisation en Temps Réel** : Mise à jour dynamique des graphiques en fonction des données reçues du backend.

### 3. Page des Capteurs (`capteurs.html`)

- **Liste des Capteurs/Actionneurs** : Affichage des différents dispositifs installés dans le logement.
- **État en Temps Réel** : Indication de l’état actuel de chaque capteur/actionneur (fonctionnel, en panne, etc.).
- **Options de Gestion** : Possibilité de configurer ou de redémarrer les capteurs directement depuis la page.

### 4. Page des Économies (`economies.html`)

- **Comparatifs Graphiques** : Graphiques montrant les économies réalisées grâce aux actions éco-responsables.
- **Analyse des Tendances** : Visualisation des progrès sur différentes périodes.
- **Rapports Détaillés** : Accès à des rapports détaillés pour une analyse approfondie.

### 5. Page de Configuration (`configuration.html`)

- **Paramètres Utilisateurs** : Gestion des informations personnelles et des préférences de l’utilisateur.
- **Ajout de Capteurs/Actionneurs** : Interface pour ajouter de nouveaux dispositifs au système.
- **Gestion des Capteurs Existants** : Options pour modifier ou supprimer les capteurs/actionneurs déjà installés.

## Design Responsive

L’application utilise **Bootstrap 4.6.2** pour assurer une mise en page responsive, garantissant une expérience utilisateur optimale sur tous les appareils (ordinateurs, tablettes, smartphones). Les éléments s’ajustent automatiquement en fonction de la taille de l’écran, assurant une lisibilité et une navigabilité sans faille.

### Points Clés :

- **Grille Flexible** : Utilisation des classes de grille Bootstrap pour structurer les sections et les cartes.
- **Images Adaptatives** : Images redimensionnées et optimisées pour différents écrans.
- **Navigation Mobile-Friendly** : Barre de navigation adaptable avec un menu hamburger sur les petits écrans.

## Interaction avec le Backend et la Base de Données

Le backend de l’application est développé en **Python** avec le framework **FastAPI**, facilitant la création d’API rapides et efficaces.

### Fonctionnement :

1. **Requêtes API** : Les pages frontend envoient des requêtes HTTP au backend pour récupérer ou envoyer des données.
2. **Gestion de la Base de Données** : **SQLAlchemy** est utilisé pour interagir avec la base de données SQLite, permettant de stocker et de gérer les informations sur les capteurs, les consommations et les économies.
3. **Scripts Serveur** : Divers scripts Python (`Serveur_Camembert.py`, `Serveur_Capteur.py`, `Serveur_Meteo.py`) gèrent des fonctionnalités spécifiques comme les graphiques Camembert, la surveillance des capteurs et l’intégration des données météo.

### Étapes de Communication :

- **Frontend** : Utilisation de JavaScript pour envoyer des requêtes AJAX aux endpoints API.
- **Backend** : FastAPI reçoit les requêtes, traite les données via SQLAlchemy, et renvoie les réponses au frontend.
- **Affichage des Données** : Les données reçues sont utilisées pour mettre à jour dynamiquement les graphiques et les états des capteurs sur les pages web.

## Utilisation de HTML5 et JavaScript

### HTML5 :

- **Sémantique** : Utilisation de balises sémantiques (`<header>`, `<nav>`, `<section>`, `<footer>`) pour une meilleure structuration du contenu.
- **Formulaires Modernes** : Champs de saisie optimisés avec des types HTML5 (`email`, `number`, `date`) pour une meilleure validation et expérience utilisateur.

### JavaScript :

- **Interactivité** : Scripts personnalisés (`consommation.js`, `capteur.js`, etc.) pour gérer l’interaction utilisateur et la manipulation dynamique du DOM.
- **Graphiques Dynamiques** : Intégration de bibliothèques comme **Chart.js** pour générer des graphiques interactifs basés sur les données récupérées du backend.
- **Gestion des Événements** : Gestion des clics, des soumissions de formulaires et des mises à jour en temps réel pour une expérience utilisateur fluide.

## Originalité et Conception Esthétique

L’application **EcoVision** se distingue par son design épuré et moderne, combinant des éléments visuels attractifs avec une fonctionnalité avancée. L’utilisation d’images de haute qualité, de couleurs harmonieuses et de typographies lisibles contribue à une apparence professionnelle et engageante.

### Points d'Originalité :

- **Graphiques Interactifs** : Présentation des données sous forme de graphiques interactifs, permettant aux utilisateurs de visualiser facilement leurs consommations et économies.
- **Gestion Intuitive des Capteurs** : Interface utilisateur permettant une gestion facile et rapide des capteurs/actionneurs, avec des indications claires de leur état.
- **Responsive Design** : Assure une accessibilité et une navigabilité optimales sur tous les appareils, répondant ainsi aux besoins des utilisateurs modernes.

## Conclusion

La **Partie 3** du TP a permis de développer une application web complète et fonctionnelle pour la gestion d’un logement éco-responsable. En combinant des technologies modernes comme HTML5, JavaScript, Bootstrap et FastAPI, l’application offre une expérience utilisateur riche et interactive, tout en garantissant une performance et une esthétique de haut niveau. L’architecture bien structurée et l’interaction fluide entre le frontend et le backend assurent une gestion efficace des données et une navigabilité optimisée.



