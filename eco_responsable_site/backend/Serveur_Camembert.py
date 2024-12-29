import os
import sqlite3
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from jinja2 import Template

# Pour lancer sur web : http://localhost:8001/api/factures/chart

app = FastAPI()

# Récupérer le chemin absolu du dossier contenant ce script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Construire le chemin complet vers database.db
DATABASE = os.path.join(BASE_DIR, "database.db")

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.get("/api/factures/chart", response_class=HTMLResponse)
def get_factures_chart():
    conn = get_db_connection()
    factures = conn.execute('SELECT type, SUM(montant) AS total FROM Facture GROUP BY type').fetchall()
    conn.close()

    # Préparer les données pour Google Charts
    data = [["Type", "Montant"]]
    for facture in factures:
        data.append([facture["type"], facture["total"]])

    # Générer le template HTML pour Google Charts
    html_template = """
    <html>
    <head>
        <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
        <script type="text/javascript">
            google.charts.load('current', {'packages':['corechart']});
            google.charts.setOnLoadCallback(drawChart);

            function drawChart() {
                var data = google.visualization.arrayToDataTable({{ chart_data }});

                var options = {
                    title: 'Répartition des factures',
                    is3D: true,
                    width: 900,
                    height: 500
                };

                var chart = new google.visualization.PieChart(document.getElementById('piechart'));
                chart.draw(data, options);
            }
        </script>
    </head>
    <body>
        <h2>Camembert des factures</h2>
        <div id="piechart" style="width: 900px; height: 500px;"></div>
    </body>
    </html>
    """

    template = Template(html_template)
    chart_data = str(data)
    rendered_html = template.render(chart_data=chart_data)

    return HTMLResponse(content=rendered_html)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
