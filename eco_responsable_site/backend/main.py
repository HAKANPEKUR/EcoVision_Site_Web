import os
import sqlite3
from fastapi import FastAPI, Request, Query, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from typing import Optional

app = FastAPI()

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Pour des raisons de sécurité spécifie les origines autorisées comme ["http://localhost:5500"]
    allow_credentials=True,
    allow_methods=["*"],  # Autorise toutes les méthodes (GET, POST, DELETE, etc.)
    allow_headers=["*"],  # Autorise tous les headers
)

# Repère le chemin du dossier courant
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database.db")

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

###############################################################################
# 1) LOGEMENTS
###############################################################################
@app.get("/api/logements")
def list_logements():
    """
    Renvoie la liste de tous les logements dans la table Logement
    Format JSON: [ { id_logement, adresse, numero_telephone, adresse_ip, date_insertion }, ... ]
    """
    conn = get_db_connection()
    c = conn.cursor()
    rows = c.execute("SELECT * FROM Logement").fetchall()
    conn.close()

    data = []
    for row in rows:
        data.append({
            "id_logement": row["id_logement"],
            "adresse": row["adresse"],
            "numero_telephone": row["numero_telephone"],
            "adresse_ip": row["adresse_ip"],
            "date_insertion": row["date_insertion"]
        })
    return JSONResponse(data)

@app.post("/api/logements")
async def create_logement(request: Request):
    """
    Reçoit un JSON : { "adresse":..., "numero_telephone":..., "adresse_ip":... }
    Insère un Logement dans la base et renvoie l'objet inséré
    """
    body = await request.json()
    adresse = body.get("adresse", "").strip()
    numero_telephone = body.get("numero_telephone", "")
    adresse_ip = body.get("adresse_ip", "")

    if not adresse:
        raise HTTPException(status_code=400, detail="Adresse requise.")

    conn = get_db_connection()
    c = conn.cursor()
    c.execute("""
        INSERT INTO Logement (adresse, numero_telephone, adresse_ip)
        VALUES (?, ?, ?)
    """, (adresse, numero_telephone, adresse_ip))
    conn.commit()
    new_id = c.lastrowid
    conn.close()

    return JSONResponse({
        "id_logement": new_id,
        "adresse": adresse,
        "numero_telephone": numero_telephone,
        "adresse_ip": adresse_ip,
        "date_insertion": datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Ajoute la date d'insertion
    })

@app.delete("/api/logements/{id_logement}")
def delete_logement(id_logement: int):
    """
    Supprime un logement par son ID.
    """
    conn = get_db_connection()
    c = conn.cursor()
    
    # Vérifie si le logement existe
    logement = c.execute("SELECT * FROM Logement WHERE id_logement = ?", (id_logement,)).fetchone()
    if not logement:
        conn.close()
        raise HTTPException(status_code=404, detail="Logement non trouvé.")

    try:
        # Commence une transaction
        conn.execute("BEGIN")

        # Suppression des factures associées
        c.execute("DELETE FROM Facture WHERE id_logement = ?", (id_logement,))
        
        # Suppression des pièces associées (si elles existent)
        c.execute("DELETE FROM Piece WHERE id_logement = ?", (id_logement,))
        
        # Suppression des logements
        c.execute("DELETE FROM Logement WHERE id_logement = ?", (id_logement,))

        # Commit de la transaction
        conn.commit()
    except Exception as e:
        # En cas d'erreur, rollback
        conn.rollback()
        conn.close()
        raise HTTPException(status_code=500, detail="Erreur lors de la suppression du logement.")
    
    conn.close()
    return JSONResponse({"detail": f"Logement {id_logement} supprimé avec succès."})

###############################################################################
# 2) CAPTEURS
###############################################################################
@app.get("/api/capteurs")
def list_capteurs():
    """
    Renvoie la liste de tous les capteurs/actionneurs dans la table Capteur_Actionneur
    Format JSON: [ { id_capteur, type, reference, port_communication, date_insertion, ... }, ... ]
    """
    conn = get_db_connection()
    c = conn.cursor()
    rows = c.execute("SELECT * FROM Capteur_Actionneur").fetchall()
    conn.close()

    data = []
    for row in rows:
        data.append({
            "id_capteur": row["id_capteur"],
            "type": row["type"],
            "reference": row["reference"],
            "port_communication": row["port_communication"],
            "date_insertion": row["date_insertion"]
        })
    return JSONResponse(data)

@app.post("/api/capteurs")
async def create_capteur(request: Request):
    """
    Reçoit un JSON: { "type":..., "reference":..., "port_communication":..., ... }
    Insère un capteur/actionneur dans la base
    """
    body = await request.json()
    type_capteur = body.get("type", "").strip()
    reference = body.get("reference", "").strip()
    port_comm = body.get("port_communication", "").strip()

    if not type_capteur:
        raise HTTPException(status_code=400, detail="Type de capteur requis.")
    if not reference:
        raise HTTPException(status_code=400, detail="Référence du capteur requise.")
    if not port_comm:
        raise HTTPException(status_code=400, detail="Port de communication requis.")

    # Pour l'exemple, on fixe : id_piece=1, id_type=1
    id_piece = 1
    id_type = 1

    conn = get_db_connection()
    c = conn.cursor()
    c.execute("""
        INSERT INTO Capteur_Actionneur (type, reference, port_communication, id_piece, id_type)
        VALUES (?, ?, ?, ?, ?)
    """, (type_capteur, reference, port_comm, id_piece, id_type))
    conn.commit()
    new_id = c.lastrowid
    conn.close()

    return JSONResponse({
        "id_capteur": new_id,
        "type": type_capteur,
        "reference": reference,
        "port_communication": port_comm,
        "id_piece": id_piece,
        "id_type": id_type,
        "date_insertion": datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Ajoute la date d'insertion
    })

@app.delete("/api/capteurs/{id_capteur}")
def delete_capteur(id_capteur: int):
    """
    Supprime un capteur/actionneur par son ID.
    """
    conn = get_db_connection()
    c = conn.cursor()
    
    # Vérifie si le capteur existe
    capteur = c.execute("SELECT * FROM Capteur_Actionneur WHERE id_capteur = ?", (id_capteur,)).fetchone()
    if not capteur:
        conn.close()
        raise HTTPException(status_code=404, detail="Capteur non trouvé.")

    try:
        # Commence une transaction
        conn.execute("BEGIN")

        # Suppression des mesures associées
        c.execute("DELETE FROM Mesure WHERE id_capteur = ?", (id_capteur,))
        
        # Suppression des capteurs/actionneurs
        c.execute("DELETE FROM Capteur_Actionneur WHERE id_capteur = ?", (id_capteur,))

        # Commit de la transaction
        conn.commit()
    except Exception as e:
        # En cas d'erreur, rollback
        conn.rollback()
        conn.close()
        raise HTTPException(status_code=500, detail="Erreur lors de la suppression du capteur.")
    
    conn.close()
    return JSONResponse({"detail": f"Capteur {id_capteur} supprimé avec succès."})

###############################################################################
# 3) FACTURES_DATA pour Consommation
###############################################################################
@app.get("/api/factures_data")
def get_factures_data():
    """
    Pour la page Consommation (camembert).
    Renvoie un tableau JSON: [ { "type":..., "total":...}, ... ]
    en agrégeant la table Facture par type.
    """
    conn = get_db_connection()
    c = conn.cursor()
    rows = c.execute("""
        SELECT type, SUM(montant) as total
        FROM Facture
        GROUP BY type
    """).fetchall()
    conn.close()

    data = []
    for row in rows:
        data.append({
            "type": row["type"],
            "total": row["total"]
        })
    return JSONResponse(data)

###############################################################################
# 4) FACTURES_EVOLUTION pour Economies
###############################################################################
@app.get("/api/factures_evolution")
def get_factures_evolution(scale: str = Query("monthly")):
    """
    Renvoie un JSON du style [ { "periode":..., "montant":... }, ... ]
    en fonction de scale=monthly|quarterly|yearly
    """
    conn = get_db_connection()
    c = conn.cursor()
    today = datetime.today()
    current_year = today.year
    
    data = []
    
    if scale == "monthly":
        # Liste des mois de janvier à décembre
        months = [
            "01", "02", "03", "04", "05", "06",
            "07", "08", "09", "10", "11", "12"
        ]
        for month in months:
            periode = f"{current_year}-{month}"
            row = c.execute("""
                SELECT SUM(montant) as total
                FROM Facture
                WHERE strftime('%Y-%m', date) = ?
            """, (periode,)).fetchone()
            total = row["total"] if row["total"] else 0
            # Nom du mois pour une meilleure lisibilité
            month_name = datetime.strptime(month, "%m").strftime("%B")
            data.append({
                "periode": month_name,
                "montant": total
            })
    
    elif scale == "quarterly":
        # Définir les trimestres T1 à T4
        trimesters = {
            "T1": (1, 3),
            "T2": (4, 6),
            "T3": (7, 9),
            "T4": (10, 12)
        }
        for trimester, (start_month, end_month) in trimesters.items():
            periode = f"{trimester} {current_year}"
            row = c.execute("""
                SELECT SUM(montant) as total
                FROM Facture
                WHERE 
                    CAST(STRFTIME('%m', date) as integer) BETWEEN ? AND ?
                    AND CAST(STRFTIME('%Y', date) as integer) = ?
            """, (start_month, end_month, current_year)).fetchone()
            total = row["total"] if row["total"] else 0
            data.append({
                "periode": periode,
                "montant": total
            })
    
    elif scale == "yearly":
        # Total pour l'année entière
        periode = f"{current_year}"
        row = c.execute("""
            SELECT SUM(montant) as total
            FROM Facture
            WHERE strftime('%Y', date) = ?
        """, (str(current_year),)).fetchone()
        total = row["total"] if row["total"] else 0
        data.append({
            "periode": periode,
            "montant": total
        })
    
    else:
        raise HTTPException(status_code=400, detail="Scale must be 'monthly', 'quarterly', or 'yearly'.")
    
    conn.close()
    
    return JSONResponse(data)

###############################################################################
# MAIN
###############################################################################
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
