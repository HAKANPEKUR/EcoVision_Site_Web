import os
import sqlite3
import requests
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from jinja2 import Template

app = FastAPI()

# Pour lancer : http://localhost:8003/meteo

# Récupérer le chemin absolu de ce script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, "database.db")

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

API_KEY = "952f2744d839909b9c0950a82b79a380"
BASE_URL_WEATHER = "https://api.openweathermap.org/data/2.5/forecast"
BASE_URL_GEOCODING = "http://api.openweathermap.org/geo/1.0/direct"

# Liste des villes
CITIES = ["Paris", "Marseille"]

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

@app.get("/meteo", response_class=HTMLResponse)
def display_weather():
    weather_data = {}

    for city in CITIES:
        try:
            coords = get_city_coordinates(city)
            response = requests.get(BASE_URL_WEATHER, params={
                "lat": coords["lat"],
                "lon": coords["lon"],
                "units": "metric",  # °C
                "appid": API_KEY
            })

            if response.status_code == 200:
                data = response.json()
                daily_forecast = {
                    "dates": [],
                    "temperature_max": [],
                    "temperature_min": [],
                    "recommendations": [],
                }

                # Regrouper les données par jour
                forecast_by_day = {}
                for item in data["list"]:
                    date = item["dt_txt"].split(" ")[0]
                    temp = item["main"]["temp"]

                    if date not in forecast_by_day:
                        forecast_by_day[date] = {"temps": []}
                    forecast_by_day[date]["temps"].append(temp)

                # Calculer les max/min et ajouter des recommandations pour 5 jours
                for date, values in list(forecast_by_day.items())[:5]:
                    max_temp = round(max(values["temps"]), 1)
                    min_temp = round(min(values["temps"]), 1)

                    recommendations = []
                    if max_temp < 10:
                        recommendations.append("Protégez vos plantes des gelées.")
                        recommendations.append("Limitez l'arrosage pour éviter un excès d'eau.")
                    if min_temp < 0:
                        recommendations.append("Vidangez vos tuyaux pour éviter les dégâts causés par le gel.")

                    if 10 <= max_temp <= 15:
                        recommendations.append("Ajoutez un paillis autour des plantes.")
                        recommendations.append("Préparez vos sols pour les prochaines plantations.")
                        recommendations.append("Aérez votre serre pour équilibrer l'humidité.")
                    if 15 <= max_temp <= 25:
                        recommendations.append("Nettoyez vos panneaux solaires pour optimiser leur efficacité.")
                        recommendations.append("Arrosez tôt le matin ou tard le soir pour minimiser l'évaporation.")

                    if max_temp > 25:
                        recommendations.append("Réduisez l’arrosage en journée pour économiser l'eau.")
                        recommendations.append("Protégez vos plantes en les plaçant à l'ombre si possible.")
                        recommendations.append("Allumez vos panneaux solaires pour maximiser l'énergie produite.")

                    if not recommendations:
                        recommendations.append("Profitez de la journée pour entretenir votre jardin.")
                        recommendations.append("Vérifiez l'état des systèmes d'irrigation et des panneaux solaires.")

                    daily_forecast["dates"].append(date)
                    daily_forecast["temperature_max"].append(max_temp)
                    daily_forecast["temperature_min"].append(min_temp)
                    daily_forecast["recommendations"].append(recommendations)

                weather_data[city] = {
                    "city": city,
                    "daily_forecast": daily_forecast,
                }

        except ValueError as e:
            print(e)

    # Template HTML d'affichage
    html_template = """
    <html>
    <head>
        <title>Prévisions Météo</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 20px;
            }
            h1 { color: #333; }
            table {
                width: 100%;
                border-collapse: collapse;
                margin-bottom: 20px;
            }
            th, td {
                border: 1px solid #ccc;
                padding: 10px;
                text-align: left;
            }
            th {
                background-color: #f4f4f4;
            }
        </style>
    </head>
    <body>
        <h1>Prévisions Météo et Recommandations</h1>
        {% for city, data in weather_data.items() %}
        <h2>{{ city }}</h2>
        <table>
            <tr>
                <th>Date</th>
                <th>Température Max (°C)</th>
                <th>Température Min (°C)</th>
                <th>Recommandations</th>
            </tr>
            {% for i in range(data['daily_forecast']['dates']|length) %}
            <tr>
                <td>{{ data['daily_forecast']['dates'][i] }}</td>
                <td>{{ data['daily_forecast']['temperature_max'][i] }}</td>
                <td>{{ data['daily_forecast']['temperature_min'][i] }}</td>
                <td>
                    <ul>
                        {% for rec in data['daily_forecast']['recommendations'][i] %}
                        <li>{{ rec }}</li>
                        {% endfor %}
                    </ul>
                </td>
            </tr>
            {% endfor %}
        </table>
        {% endfor %}
    </body>
    </html>
    """

    template = Template(html_template)
    rendered_html = template.render(weather_data=weather_data)
    return HTMLResponse(content=rendered_html)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8003)
