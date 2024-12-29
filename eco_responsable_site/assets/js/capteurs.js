// URL de base pour l'API des capteurs
const CAPTEURS_BASE_URL = "http://localhost:8000"; 

// Exécute ce code une fois que la page est complètement chargée
document.addEventListener("DOMContentLoaded", () => {
  // Charger automatiquement la liste des capteurs au chargement de la page
  loadCapteurs();

  // Gestion du clic sur le bouton "Rafraîchir"
  const refreshBtn = document.getElementById("refresh-btn");
  if (refreshBtn) {
    refreshBtn.addEventListener("click", () => {
      // Recharge la liste des capteurs lorsque le bouton est cliqué
      loadCapteurs();
    });
  }
});

// Fonction pour récupérer les capteurs via une requête API
function loadCapteurs() {
  // Effectue une requête GET vers l'API pour obtenir les capteurs
  fetch(`${CAPTEURS_BASE_URL}/api/capteurs`)
    .then(response => {
      // Vérifie si la réponse est correcte
      if (!response.ok) {
        throw new Error("Erreur lors de la récupération des capteurs.");
      }
      // Convertit la réponse en JSON
      return response.json();
    })
    .then(data => {
      // Affiche les données des capteurs dans le tableau
      afficherCapteurs(data);
    })
    .catch(error => console.error("Erreur:", error)); // Affiche les erreurs dans la console
}

// Fonction pour afficher les capteurs dans le tableau HTML
function afficherCapteurs(data) {
  // Sélectionne le corps du tableau (tbody) dans la page
  const tbody = document.querySelector("#capteurs-table tbody");
  if (!tbody) return; // Si le tableau n'existe pas, on arrête la fonction

  // Vide le tableau avant de le remplir avec de nouvelles données
  tbody.innerHTML = "";

  // Parcourt chaque capteur et crée une nouvelle ligne pour chaque entrée
  data.forEach(capteur => {
    let row = document.createElement("tr");
    row.innerHTML = `
      <td>${capteur.id_capteur}</td> <!-- ID du capteur -->
      <td>${capteur.type}</td> <!-- Type du capteur -->
      <td>${capteur.reference}</td> <!-- Référence commerciale du capteur -->
      <td>${capteur.port_communication}</td> <!-- Port de communication -->
      <td>${capteur.date_insertion || ""}</td> <!-- Date d'insertion (vide si non fournie) -->
    `;
    // Ajoute la ligne créée au tableau
    tbody.appendChild(row);
  });
}
