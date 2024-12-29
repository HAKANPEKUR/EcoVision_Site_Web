// URL de base pour l'API
const ECONOMIES_BASE_URL = "http://localhost:8000";

// On charge la bibliothèque Google Charts
google.charts.load('current', { packages: ['corechart'] });
// Une fois la bibliothèque chargée, on appelle la fonction initEconomiesPage
google.charts.setOnLoadCallback(initEconomiesPage);

// Initialisation de la page des économies
function initEconomiesPage() {
  // Charger les données pour l'échelle mensuelle par défaut
  loadEconomiesData("monthly");

  // Ajouter un écouteur sur le menu déroulant pour changer l'échelle (mensuelle, trimestrielle, annuelle)
  const selectEchelle = document.getElementById("selectEchelle");
  if (selectEchelle) {
    selectEchelle.addEventListener("change", () => {
      // Charger les données en fonction de l'échelle sélectionnée
      loadEconomiesData(selectEchelle.value);
    });
  }
}

// Fonction pour récupérer les données d'économies depuis l'API
function loadEconomiesData(echelle) {
  // Requête GET vers l'endpoint /api/factures_evolution avec le paramètre d'échelle
  fetch(`${ECONOMIES_BASE_URL}/api/factures_evolution?scale=${echelle}`)
    .then(res => {
      if (!res.ok) {
        // Lever une erreur si la réponse n'est pas correcte
        throw new Error("Erreur GET factures_evolution");
      }
      return res.json(); // Convertir la réponse en JSON
    })
    .then(data => {
      // Les données doivent être de la forme : [{periode: "Janv 2024", montant: 120}, ...]
      drawEconomiesChart(data, echelle); // Dessiner le graphique avec les données reçues
    })
    .catch(err => {
      // Gérer les erreurs lors de la requête API
      console.error("Erreur /api/factures_evolution:", err);
    });
}

// Fonction pour dessiner le graphique d'évolution des économies
function drawEconomiesChart(data, echelle) {
  // Création d'un tableau de données pour Google Charts
  const dataTable = new google.visualization.DataTable();
  dataTable.addColumn("string", "Période"); // Colonne pour les périodes (mois, trimestres, années)
  dataTable.addColumn("number", "Montant (€)"); // Colonne pour les montants en euros

  // Remplissage des données dans le tableau
  data.forEach(item => {
    dataTable.addRow([item.periode, item.montant]); // Exemple : ["Janv 2024", 120]
  });

  // Options de style pour le graphique
  const options = {
    title: "Évolution des Factures / Consommations", // Titre du graphique
    width: "100%", // Largeur du graphique
    height: 500, // Hauteur du graphique
    legend: { position: "bottom" }, // Position de la légende
    hAxis: { title: "Période" }, // Titre de l'axe horizontal
    vAxis: { title: "Montant en €" } // Titre de l'axe vertical
  };

  // On dessine un graphique en colonnes dans le conteneur HTML avec l'id "economies_chart"
  const chart = new google.visualization.ColumnChart(document.getElementById("economies_chart"));
  chart.draw(dataTable, options); // Dessiner le graphique avec les données et les options
}
