// On charge Google Charts pour les graphiques
google.charts.load('current', { packages: ['corechart'] });
// Une fois Google Charts chargé, on appelle la fonction loadConsommationData
google.charts.setOnLoadCallback(loadConsommationData);

// Adresse de base pour les appels API
const BASE_URL = "http://localhost:8000";

// Fonction pour charger les données de consommation depuis l'API
function loadConsommationData() {
  // Requête GET pour récupérer les données depuis l'endpoint /api/factures_data
  fetch(`${BASE_URL}/api/factures_data`)
    .then(response => {
      if (!response.ok) {
        // Gestion des erreurs si la requête échoue
        throw new Error("Erreur lors de la récupération des données de consommation.");
      }
      return response.json(); // Conversion de la réponse en JSON
    })
    .then(data => {
      // Les données reçues doivent être de la forme : [{type: "Électricité", total: 123.45}, ...]
      drawConsommationChart(data); // Dessiner le graphique avec les données
    })
    .catch(error => {
      // Gestion des erreurs lors de l'appel API
      console.error("Erreur lors du fetch /api/factures_data:", error);
    });
}

// Fonction pour dessiner un camembert avec les données de consommation
function drawConsommationChart(data) {
  // Création d'un tableau de données pour Google Charts
  let chartData = new google.visualization.DataTable();
  chartData.addColumn("string", "Type"); // Colonne pour le type de consommation (ex. Électricité)
  chartData.addColumn("number", "Montant total"); // Colonne pour le montant total

  // Ajout des lignes de données dans le tableau
  data.forEach(item => {
    chartData.addRow([item.type, item.total]); // Exemple : ["Électricité", 123.45]
  });

  // Options de style pour le graphique
  let options = {
    title: "Répartition de la Consommation", // Titre du graphique
    is3D: true, // Activer l'effet 3D pour le camembert
    width: "100%", // Largeur du graphique
    height: 500 // Hauteur du graphique
  };

  // On dessine le graphique dans le div HTML avec l'id "chart_div"
  let chart = new google.visualization.PieChart(document.getElementById("chart_div"));
  chart.draw(chartData, options); // Dessiner le graphique avec les données et les options
}
