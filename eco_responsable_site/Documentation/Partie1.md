# Partie 1 : Base de données

Cette partie couvre les étapes nécessaires pour construire, configurer et remplir une base de données pour gérer un logement éco-responsable. Elle inclut les réponses aux questions 1 à 8, ainsi que le point 1.2 sur le remplissage automatique de la base de données.

---

## **Question 2 : Destruction des tables existantes**

Avant de créer de nouvelles tables, nous supprimons celles déjà existantes afin d'assurer une base propre. Voici les lignes SQL correspondantes :

```sql
DROP TABLE IF EXISTS Mesure;
DROP TABLE IF EXISTS Capteur_Actionneur;
DROP TABLE IF EXISTS Piece;
DROP TABLE IF EXISTS Type_Capteur;
DROP TABLE IF EXISTS Facture;
DROP TABLE IF EXISTS Logement;
```

---

## **Question 3 : Création des tables**

Les tables suivantes ont été créées pour organiser les données :

### 1. **Table `Logement`**
- Contient les informations générales sur chaque logement.
- Clé primaire : `id_logement`.

### 2. **Table `Piece`**
- Représente les pièces associées à un logement.
- Clé primaire : `id_piece`.
- Clé étrangère : `id_logement`.

### 3. **Table `Type_Capteur`**
- Contient les informations générales sur les types de capteurs/actionneurs.
- Clé primaire : `id_type`.

### 4. **Table `Capteur_Actionneur`**
- Liste des capteurs/actionneurs installés dans les pièces.
- Clé primaire : `id_capteur`.
- Clés étrangères : `id_piece` et `id_type`.

### 5. **Table `Mesure`**
- Stocke les mesures effectuées par les capteurs.
- Clé primaire : `id_mesure`.
- Clé étrangère : `id_capteur`.

### 6. **Table `Facture`**
- Contient les factures associées aux logements.
- Clé primaire : `id_facture`.
- Clé étrangère : `id_logement`.

L'intégralité du script SQL est dans le fichier `logement.sql`.

---

## **Question 4 : Insertion d'un logement et des pièces associées**

Deux logements ont été insérés dans la table `Logement`. Le premier logement a 4 pièces associées : Salon, Cuisine, Chambre et Salle de Bain.

Exemple d'insertion SQL (logement et ses pièces) :

```sql
INSERT INTO Logement (adresse, numero_telephone, adresse_ip)
VALUES ('5 rue de Jussieu, Paris', '0663184027', '192.168.10.10');

INSERT INTO Piece (nom, coordonnee_x, coordonnee_y, coordonnee_z, id_logement)
VALUES ('Salon', 0, 0, 0, 1);
```

Détails complets dans le fichier `logement.sql`.

---

## **Question 5 : Types de capteurs/actionneurs**

Quatre types de capteurs/actionneurs ont été insérés dans la table `Type_Capteur` : Température, Humidité, Luminosité, et Présence. Exemple d'insertion :

```sql
INSERT INTO Type_Capteur (unite_mesure, precision, autres_informations)
VALUES ('Température', '0.1°C', 'Capteur de température pour monitoring de la pièce');
```

Détails complets dans le fichier `logement.sql`.

---

## **Question 6 : Insertion de capteurs/actionneurs**

Exemple d'insertion d'un capteur de température dans le Salon :

```sql
INSERT INTO Capteur_Actionneur (type, reference, port_communication, id_piece, id_type)
VALUES ('Température', 'TEMP-001', 'WiFi', 1, 1);
```

Détails complets dans le fichier `logement.sql`.

---

## **Question 7 : Insertion de mesures**

Deux mesures par capteur ont été insérées pour simuler des relevés :

```sql
INSERT INTO Mesure (valeur, id_capteur)
VALUES (22.5, 1), (23.0, 1);
```

Détails complets dans le fichier `logement.sql`.

---

## **Question 8 : Insertion de factures**

Des factures ont été ajoutées pour chaque logement. Exemple pour le premier logement :

```sql
INSERT INTO Facture (type, date, montant, valeur_consomme, id_logement)
VALUES ('Électricité', '2024-01-15', 80.00, 130.0, 1);
```

Détails complets dans le fichier `logement.sql`.

---

## **Point 1.2 : Remplissage automatique de la base de données**

### Script Python

Un script Python (`remplissage_python.py`) a été créé pour automatiser l'insertion de données aléatoires dans les tables `Mesure` et `Facture`. 

Exemple de code pour insérer des mesures :

```python
for capteur in capteurs:
    id_capteur = capteur['id_capteur']
    for _ in range(2):
        valeur = round(random.uniform(10.0, 100.0), 2)
        date_insertion = generate_random_date()
        c.execute("""
            INSERT INTO Mesure (valeur, date_insertion, id_capteur)
            VALUES (?, ?, ?)
        """, (valeur, date_insertion, id_capteur))
```

Le fichier `remplissage_python.py` contient :
- Connexion à la base de données.
- Génération aléatoire des valeurs pour les mesures et factures.
- Validation et insertion dans la base.

Pour plus de détails, consultez le fichier Python directement "remplissage_python.py".