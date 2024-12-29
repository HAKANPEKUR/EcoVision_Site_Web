import os
import sqlite3
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import requests
import random
from datetime import datetime
from jinja2 import Template

app = FastAPI()

# Pour lancer sur web : http://localhost:8002/api/sensor

# Récupérer le chemin absolu du dossier contenant ce script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Construire le chemin complet vers database.db dans le même dossier
DATABASE = os.path.join(BASE_DIR, "database.db")

# Fonction pour se connecter à la DB si besoin
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Clé API OpenWeather
API_KEY = "952f2744d839909b9c0950a82b79a380"
BASE_URL_WEATHER = "https://api.openweathermap.org/data/2.5/forecast"
BASE_URL_GEOCODING = "http://api.openweathermap.org/geo/1.0/direct"

CITY_NAME = "Paris"

def get_city_coordinates(city_name):
    response = requests.get(BASE_URL_GEOCODING, params={
        "q": city_name,
        "limit": 1,
        "appid": API_KEY
    })
    if response.status_code == 200 and response.json():
        data = response.json()[0]
        return {"lat": data["lat"], "lon": data["lon"]}
    else:
        raise ValueError(f"Impossible de récupérer les coordonnées pour {city_name}")

def get_external_temperature(lat, lon):
    response = requests.get(BASE_URL_WEATHER, params={
        "lat": lat,
        "lon": lon,
        "units": "metric",
        "appid": API_KEY
    })
    if response.status_code == 200:
        data = response.json()
        # Récupérer la température moyenne du jour (premier élément de la liste)
        return data["list"][0]["main"]["temp"]  # °C
    else:
        return None

def simulate_dht22_data(external_temperature):
    sensor_data = []
    for _ in range(10):
        temperature = round(external_temperature + random.uniform(-3.0, 3.0), 1)
        humidity = round(random.uniform(40.0, 60.0), 1)
        sensor_data.append({
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "temperature": temperature,
            "humidity": humidity,
            "external_temperature": external_temperature,
            "led_state": "Allumée" if temperature > external_temperature else "Éteinte"
        })
    return sensor_data

@app.get("/api/sensor", response_class=HTMLResponse)
def display_sensor_data():
    try:
        coords = get_city_coordinates(CITY_NAME)
        external_temperature = get_external_temperature(coords["lat"], coords["lon"])
        if external_temperature is None:
            return HTMLResponse("<h1>Erreur : Impossible de récupérer la température extérieure.</h1>", status_code=500)

        sensor_data = simulate_dht22_data(external_temperature)

        # Template HTML pour afficher les données
        html_template = """
        <html>
        <head>
            <title>Données du Capteur DHT22</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 20px;
                }
                h1 {
                    color: #333;
                }
                table {
                    width: 100%;
                    border-collapse: collapse;
                    margin-top: 20px;
                }
                th, td {
                    border: 1px solid #ccc;
                    padding: 10px;
                    text-align: left;
                }
                th {
                    background-color: #f4f4f4;
                }
                .led-on {
                    color: green;
                    font-weight: bold;
                }
                .led-off {
                    color: red;
                    font-weight: bold;
                }
            </style>
        </head>
        <body>
            <h1>Données du Capteur DHT22</h1>
            <table>
                <tr>
                    <th>Horodatage</th>
                    <th>Température (°C)</th>
                    <th>Humidité (%)</th>
                    <th>Température extérieure (°C)</th>
                    <th>État de la LED</th>
                </tr>
                {% for data in sensor_data %}
                <tr>
                    <td>{{ data.timestamp }}</td>
                    <td>{{ data.temperature }}</td>
                    <td>{{ data.humidity }}</td>
                    <td>{{ data.external_temperature }}</td>
                    <td class="{{ 'led-on' if data.led_state == 'Allumée' else 'led-off' }}">{{ data.led_state }}</td>
                </tr>
                {% endfor %}
            </table>
        </body>
        </html>
        """

        template = Template(html_template)
        rendered_html = template.render(sensor_data=sensor_data)
        return HTMLResponse(content=rendered_html)

    except ValueError as e:
        return HTMLResponse(content=f"<h1>Erreur : {e}</h1>", status_code=500)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8002)
