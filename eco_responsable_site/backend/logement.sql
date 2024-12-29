--------------------------------------------------------------------------
-- Question 2 : Destruction des tables existantes (si elles sont présentes)
--------------------------------------------------------------------------

DROP TABLE IF EXISTS Mesure;
DROP TABLE IF EXISTS Capteur_Actionneur;
DROP TABLE IF EXISTS Piece;
DROP TABLE IF EXISTS Type_Capteur;
DROP TABLE IF EXISTS Facture;
DROP TABLE IF EXISTS Logement;

--------------------------------------------------------------------------
-- Question 3 : Création des tables
--------------------------------------------------------------------------

-- Création de la table Logement
-- Cette table contient les informations générales sur chaque logement
CREATE TABLE Logement (
    id_logement INTEGER PRIMARY KEY AUTOINCREMENT,
    adresse TEXT NOT NULL,
    numero_telephone TEXT,
    adresse_ip TEXT,
    date_insertion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Création de la table Piece
-- Cette table représente les pièces associées à chaque logement
CREATE TABLE Piece (
    id_piece INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    coordonnee_x INTEGER,
    coordonnee_y INTEGER,
    coordonnee_z INTEGER,
    id_logement INTEGER NOT NULL,
    FOREIGN KEY (id_logement) REFERENCES Logement(id_logement)
);

-- Création de la table Type_Capteur
-- Cette table contient les types généraux des capteurs/actionneurs
CREATE TABLE Type_Capteur (
    id_type INTEGER PRIMARY KEY AUTOINCREMENT,
    unite_mesure TEXT,
    precision TEXT,
    autres_informations TEXT
);

-- Création de la table Capteur_Actionneur
-- Cette table représente chaque capteur/actionneur installé dans une pièce
CREATE TABLE Capteur_Actionneur (
    id_capteur INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT NOT NULL,
    reference TEXT,
    port_communication TEXT,
    date_insertion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    id_piece INTEGER NOT NULL,
    id_type INTEGER NOT NULL,
    FOREIGN KEY (id_piece) REFERENCES Piece(id_piece),
    FOREIGN KEY (id_type) REFERENCES Type_Capteur(id_type)
);

-- Création de la table Mesure
-- Cette table enregistre les mesures effectuées par les capteurs
CREATE TABLE Mesure (
    id_mesure INTEGER PRIMARY KEY AUTOINCREMENT,
    valeur REAL NOT NULL,
    date_insertion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    id_capteur INTEGER NOT NULL,
    FOREIGN KEY (id_capteur) REFERENCES Capteur_Actionneur(id_capteur)
);

-- Création de la table Facture
-- Cette table stocke les factures associées à chaque logement
CREATE TABLE Facture (
    id_facture INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT NOT NULL,
    date TIMESTAMP NOT NULL,
    montant REAL NOT NULL,
    valeur_consomme REAL,
    id_logement INTEGER NOT NULL,
    FOREIGN KEY (id_logement) REFERENCES Logement(id_logement)
);

--------------------------------------------------------------------------
-- Question 4 : Insertion d'un logement avec 4 pièces
--------------------------------------------------------------------------

-- Insertion d'un logement
INSERT INTO Logement (adresse, numero_telephone, adresse_ip)
VALUES ('5 rue de Jussieu, Paris', '0663184027', '192.168.10.10');
-- Insertion d'un deuxième logement
INSERT INTO Logement (adresse, numero_telephone, adresse_ip)
VALUES 
('10 Avenue des Champs Elysées, Paris', '0678901234', '192.168.10.20');

-- Insertion des pièces associées au logement nouvellement créé
INSERT INTO Piece (nom, coordonnee_x, coordonnee_y, coordonnee_z, id_logement)
VALUES 
('Salon', 0, 0, 0, 1),
('Cuisine', 1, 0, 0, 1),
('Chambre', 0, 1, 0, 1),
('Salle de Bain', 1, 1, 0, 1);

---------------------------------------------------------------------------
-- Question 5 : Insertion de types de capteurs/actionneurs
--------------------------------------------------------------------------

-- Insertion de types de capteurs/actionneurs dans la table Type_Capteur
INSERT INTO Type_Capteur (unite_mesure, precision, autres_informations)
VALUES 
('Température', '0.1°C', 'Capteur de température pour monitoring de la pièce'),
('Humidité', '1%', 'Capteur humidité pour mesurer le taux humidité ambiant'),
('Luminosité', '0.5 lux', 'Capteur de luminosité pour ajuster éclairage'),
('Présence', 'Détection', 'Capteur de mouvement pour détecter la présence dans une pièce');

---------------------------------------------------------------------------
-- Question 6 : Insertion de capteurs/actionneurs
---------------------------------------------------------------------------

-- Insertion de capteurs/actionneurs dans la table Capteur_Actionneur
-- On suppose que les id_piece et id_type existent déjà dans la base

INSERT INTO Capteur_Actionneur (type, reference, port_communication, id_piece, id_type)
VALUES 
    ('Température', 'TEMP-001', 'WiFi', 1, 1),    -- Capteur de température dans le Salon
    ('Humidité', 'HUM-002', 'Zigbee', 2, 2),      -- Capteur d'humidité dans la Cuisine
    ('Luminosité', 'LUX-001', 'WiFi', 1, 3),      -- Capteur de luminosité dans le Salon
    ('Présence', 'PRS-001', 'Zigbee', 1, 4),      -- Capteur de présence dans le Salon
    ('Luminosité', 'LUX-002', 'WiFi', 2, 3);      -- Capteur de luminosité dans la Cuisine

---------------------------------------------------------------------------
-- Question 7 : Insertion de mesures pour les capteurs/actionneurs
---------------------------------------------------------------------------

-- Insertion de mesures pour le capteur de température (id_capteur = 1)
INSERT INTO Mesure (valeur, id_capteur)
VALUES 
(22.5, 1), -- Mesure de 22.5°C
(23.0, 1); -- Mesure de 23.0°C

-- Insertion de mesures pour le capteur d'humidité (id_capteur = 2)
INSERT INTO Mesure (valeur, id_capteur)
VALUES 
(55.0, 2), -- Mesure d'humidité de 55%
(57.3, 2); -- Mesure d'humidité de 57.3%

---------------------------------------------------------------------------
-- Question 8 : Insertion de factures pour les logements
---------------------------------------------------------------------------

-- Insertion de factures dans la table Facture

-- Factures pour Logement 1
INSERT INTO Facture (type, date, montant, valeur_consomme, id_logement) VALUES 
('Électricité', '2024-01-15', 80.00, 130.0, 1),
('Eau', '2024-01-20', 35.00, 20.0, 1),
('Gaz', '2024-01-25', 50.00, 90.0, 1),
('Déchets', '2024-01-30', 15.00, 5.0, 1),

('Électricité', '2024-02-15', 78.00, 125.0, 1),
('Eau', '2024-02-20', 32.00, 18.0, 1),
('Gaz', '2024-02-25', 48.00, 85.0, 1),
('Déchets', '2024-02-28', 14.00, 4.0, 1),

('Électricité', '2024-03-15', 82.00, 135.0, 1),
('Eau', '2024-03-20', 36.00, 22.0, 1),
('Gaz', '2024-03-25', 52.00, 95.0, 1),
('Déchets', '2024-03-30', 16.00, 6.0, 1),

('Électricité', '2024-04-15', 85.00, 140.0, 1),
('Eau', '2024-04-20', 38.00, 24.0, 1),
('Gaz', '2024-04-25', 55.00, 100.0, 1),
('Déchets', '2024-04-30', 17.00, 6.5, 1),

('Électricité', '2024-05-15', 80.00, 130.0, 1),
('Eau', '2024-05-20', 35.00, 20.0, 1),
('Gaz', '2024-05-25', 50.00, 90.0, 1),
('Déchets', '2024-05-30', 15.00, 5.0, 1),

('Électricité', '2024-06-15', 78.00, 125.0, 1),
('Eau', '2024-06-20', 32.00, 18.0, 1),
('Gaz', '2024-06-25', 48.00, 85.0, 1),
('Déchets', '2024-06-28', 14.00, 4.0, 1),

('Électricité', '2024-07-15', 82.00, 135.0, 1),
('Eau', '2024-07-20', 36.00, 22.0, 1),
('Gaz', '2024-07-25', 52.00, 95.0, 1),
('Déchets', '2024-07-30', 16.00, 6.0, 1),

('Électricité', '2024-08-15', 85.00, 140.0, 1),
('Eau', '2024-08-20', 38.00, 24.0, 1),
('Gaz', '2024-08-25', 55.00, 100.0, 1),
('Déchets', '2024-08-30', 17.00, 6.5, 1),

('Électricité', '2024-09-15', 80.00, 130.0, 1),
('Eau', '2024-09-20', 35.00, 20.0, 1),
('Gaz', '2024-09-25', 50.00, 90.0, 1),
('Déchets', '2024-09-30', 15.00, 5.0, 1),

('Électricité', '2024-10-15', 75.50, 120.0, 1),
('Eau', '2024-10-20', 30.20, 15.0, 1),
('Gaz', '2024-10-25', 45.00, 80.0, 1),
('Déchets', '2024-10-30', 12.80, 5.0, 1),

('Électricité', '2024-11-15', 78.00, 125.0, 1),
('Eau', '2024-11-20', 32.00, 18.0, 1),
('Gaz', '2024-11-25', 48.00, 85.0, 1),
('Déchets', '2024-11-28', 14.00, 4.0, 1),

('Électricité', '2024-12-15', 82.00, 135.0, 1),
('Eau', '2024-12-20', 36.00, 22.0, 1),
('Gaz', '2024-12-25', 52.00, 95.0, 1),
('Déchets', '2024-12-30', 16.00, 6.0, 1),

-- Factures pour Logement 2
('Électricité', '2024-01-10', 70.00, 110.0, 2),
('Eau', '2024-01-15', 25.00, 12.0, 2),
('Gaz', '2024-01-20', 40.00, 75.0, 2),
('Déchets', '2024-01-25', 10.00, 3.0, 2),
('Internet', '2024-01-05', 45.00, 0.0, 2),

('Électricité', '2024-02-10', 68.00, 105.0, 2),
('Eau', '2024-02-15', 23.00, 11.0, 2),
('Gaz', '2024-02-20', 38.00, 70.0, 2),
('Déchets', '2024-02-25', 9.00, 3.0, 2),
('Internet', '2024-02-05', 45.00, 0.0, 2),

('Électricité', '2024-03-10', 72.00, 115.0, 2),
('Eau', '2024-03-15', 27.00, 14.0, 2),
('Gaz', '2024-03-20', 42.00, 78.0, 2),
('Déchets', '2024-03-25', 11.00, 4.0, 2),
('Internet', '2024-03-05', 45.00, 0.0, 2),

('Électricité', '2024-04-10', 75.00, 120.0, 2),
('Eau', '2024-04-15', 28.00, 15.0, 2),
('Gaz', '2024-04-20', 44.00, 80.0, 2),
('Déchets', '2024-04-25', 12.00, 4.5, 2),
('Internet', '2024-04-05', 45.00, 0.0, 2),

('Électricité', '2024-05-10', 70.00, 110.0, 2),
('Eau', '2024-05-15', 25.00, 12.0, 2),
('Gaz', '2024-05-20', 40.00, 75.0, 2),
('Déchets', '2024-05-25', 10.00, 3.0, 2),
('Internet', '2024-05-05', 45.00, 0.0, 2),

('Électricité', '2024-06-10', 68.00, 105.0, 2),
('Eau', '2024-06-15', 23.00, 11.0, 2),
('Gaz', '2024-06-20', 38.00, 70.0, 2),
('Déchets', '2024-06-25', 9.00, 3.0, 2),
('Internet', '2024-06-05', 45.00, 0.0, 2),

('Électricité', '2024-07-10', 72.00, 115.0, 2),
('Eau', '2024-07-15', 27.00, 14.0, 2),
('Gaz', '2024-07-20', 42.00, 78.0, 2),
('Déchets', '2024-07-25', 11.00, 4.0, 2),
('Internet', '2024-07-05', 45.00, 0.0, 2),

('Électricité', '2024-08-10', 75.00, 120.0, 2),
('Eau', '2024-08-15', 28.00, 15.0, 2),
('Gaz', '2024-08-20', 44.00, 80.0, 2),
('Déchets', '2024-08-25', 12.00, 4.5, 2),
('Internet', '2024-08-05', 45.00, 0.0, 2),

('Électricité', '2024-09-10', 70.00, 110.0, 2),
('Eau', '2024-09-15', 25.00, 12.0, 2),
('Gaz', '2024-09-20', 40.00, 75.0, 2),
('Déchets', '2024-09-25', 10.00, 3.0, 2),
('Internet', '2024-09-05', 45.00, 0.0, 2),

('Électricité', '2024-10-10', 75.50, 120.0, 2),
('Eau', '2024-10-15', 30.20, 15.0, 2),
('Gaz', '2024-10-20', 45.00, 80.0, 2),
('Déchets', '2024-10-25', 12.80, 5.0, 2),
('Internet', '2024-10-05', 45.00, 0.0, 2),

('Électricité', '2024-11-10', 78.00, 125.0, 2),
('Eau', '2024-11-15', 32.00, 18.0, 2),
('Gaz', '2024-11-20', 48.00, 85.0, 2),
('Déchets', '2024-11-25', 14.00, 4.0, 2),
('Internet', '2024-11-05', 45.00, 0.0, 2),

('Électricité', '2024-12-10', 82.00, 135.0, 2),
('Eau', '2024-12-15', 36.00, 22.0, 2),
('Gaz', '2024-12-20', 52.00, 95.0, 2),
('Déchets', '2024-12-25', 16.00, 6.0, 2),
('Internet', '2024-12-05', 45.00, 0.0, 2);