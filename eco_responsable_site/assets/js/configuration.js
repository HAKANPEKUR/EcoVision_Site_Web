// URL de base pour l'API
const CONFIG_BASE_URL = "http://localhost:8000";

document.addEventListener("DOMContentLoaded", () => {
  // Charger les données dès le chargement de la page
  loadLogementsFromAPI();
  loadCapteursFromAPI();

  // Gestion de l'ajout d'un logement via le formulaire
  const formLogement = document.getElementById("form-logement");
  if (formLogement) {
    formLogement.addEventListener("submit", (e) => {
      e.preventDefault(); // Empêche le rechargement de la page
      addLogementToAPI(); // Ajoute le logement via l'API
    });
  }

  // Gestion de l'ajout d'un capteur via le formulaire
  const formCapteur = document.getElementById("form-capteur");
  if (formCapteur) {
    formCapteur.addEventListener("submit", (e) => {
      e.preventDefault(); // Empêche le rechargement de la page
      addCapteurToAPI(); // Ajoute le capteur via l'API
    });
  }
});

// ---------------------- LOGEMENTS ----------------------

// Fonction pour récupérer et afficher les logements depuis l'API
function loadLogementsFromAPI() {
  fetch(`${CONFIG_BASE_URL}/api/logements`)
    .then(res => {
      if (!res.ok) throw new Error("Erreur GET logements"); // Gère les erreurs
      return res.json(); // Parse la réponse en JSON
    })
    .then(data => {
      afficherLogements(data); // Affiche les logements récupérés
    })
    .catch(err => console.error("Erreur GET logements:", err)); // Affiche les erreurs dans la console
}

// Fonction pour ajouter un nouveau logement via l'API
function addLogementToAPI() {
  const adresse = document.getElementById("adresse").value.trim();
  const telephone = document.getElementById("telephone").value.trim();
  const ip = document.getElementById("ip").value.trim();

  // Préparation des données à envoyer
  const payload = {
    adresse: adresse,
    numero_telephone: telephone,
    adresse_ip: ip
  };

  fetch(`${CONFIG_BASE_URL}/api/logements`, {
    method: "POST", // Méthode POST pour envoyer les données
    headers: { "Content-Type": "application/json" }, // En-têtes
    body: JSON.stringify(payload) // Données envoyées en JSON
  })
  .then(res => {
    if (!res.ok) {
      return res.json().then(err => { throw err; }); // Gère les erreurs spécifiques
    }
    return res.json();
  })
  .then(insertedLog => {
    alert("Logement ajouté avec succès!"); // Confirmation à l'utilisateur
    document.getElementById("form-logement").reset(); // Réinitialise le formulaire
    loadLogementsFromAPI(); // Recharge la liste des logements
  })
  .catch(err => {
    console.error("Erreur POST logements:", err); // Affiche les erreurs dans la console
    alert(`Erreur: ${err.detail || err.message}`); // Affiche un message d'erreur
  });
}

// Fonction pour afficher les logements dans le tableau HTML
function afficherLogements(logements) {
  const tbody = document.querySelector("#table-logements tbody");
  if (!tbody) return; // Si le tableau n'existe pas, arrêter la fonction

  tbody.innerHTML = ""; // Efface les anciennes données

  logements.forEach((log) => {
    const tr = document.createElement("tr");
    tr.innerHTML = `
      <td>${log.id_logement}</td> <!-- ID du logement -->
      <td>${log.adresse}</td> <!-- Adresse -->
      <td>${log.numero_telephone || ""}</td> <!-- Téléphone -->
      <td>${log.adresse_ip || ""}</td> <!-- Adresse IP -->
      <td>
        <!-- Bouton pour supprimer un logement -->
        <button class="btn btn-danger btn-sm" onclick="deleteLogement(${log.id_logement})">Supprimer</button>
      </td>
    `;
    tbody.appendChild(tr); // Ajoute la ligne au tableau
  });
}

// Fonction pour supprimer un logement via l'API
function deleteLogement(id_logement) {
  if (!confirm(`Êtes-vous sûr de vouloir supprimer le logement ID ${id_logement} ?`)) return;

  fetch(`${CONFIG_BASE_URL}/api/logements/${id_logement}`, {
    method: "DELETE" // Méthode DELETE pour supprimer
  })
  .then(res => {
    if (!res.ok) {
      return res.json().then(err => { throw err; });
    }
    return res.json();
  })
  .then(response => {
    alert(response.detail); // Message de confirmation
    loadLogementsFromAPI(); // Recharge la liste des logements
  })
  .catch(err => {
    console.error("Erreur DELETE logement:", err); // Affiche les erreurs dans la console
    alert(`Erreur: ${err.detail || err.message}`); // Affiche un message d'erreur
  });
}

// ---------------------- CAPTEURS ----------------------

// Fonction pour récupérer et afficher les capteurs depuis l'API
function loadCapteursFromAPI() {
  fetch(`${CONFIG_BASE_URL}/api/capteurs`)
    .then(res => {
      if (!res.ok) throw new Error("Erreur GET capteurs"); // Gère les erreurs
      return res.json();
    })
    .then(data => {
      afficherCapteurs(data); // Affiche les capteurs récupérés
    })
    .catch(err => console.error("Erreur GET capteurs:", err)); // Affiche les erreurs dans la console
}

// Fonction pour ajouter un nouveau capteur via l'API
function addCapteurToAPI() {
  const typeC = document.getElementById("typeCapteur").value.trim();
  const ref = document.getElementById("refCapteur").value.trim();
  const port = document.getElementById("portCapteur").value.trim();

  // Préparation des données à envoyer
  const payload = {
    type: typeC,
    reference: ref,
    port_communication: port
  };

  fetch(`${CONFIG_BASE_URL}/api/capteurs`, {
    method: "POST", // Méthode POST pour envoyer les données
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  })
  .then(res => {
    if (!res.ok) {
      return res.json().then(err => { throw err; });
    }
    return res.json();
  })
  .then(insertedCapteur => {
    alert("Capteur ajouté avec succès!"); // Confirmation à l'utilisateur
    document.getElementById("form-capteur").reset(); // Réinitialise le formulaire
    loadCapteursFromAPI(); // Recharge la liste des capteurs
  })
  .catch(err => {
    console.error("Erreur POST capteurs:", err); // Affiche les erreurs dans la console
    alert(`Erreur: ${err.detail || err.message}`); // Affiche un message d'erreur
  });
}

// Fonction pour afficher les capteurs dans le tableau HTML
function afficherCapteurs(capteurs) {
  const tbody = document.querySelector("#table-capteurs tbody");
  if (!tbody) return; // Si le tableau n'existe pas, arrêter la fonction

  tbody.innerHTML = ""; // Efface les anciennes données

  capteurs.forEach((cap) => {
    const tr = document.createElement("tr");
    tr.innerHTML = `
      <td>${cap.id_capteur}</td> <!-- ID du capteur -->
      <td>${cap.type}</td> <!-- Type du capteur -->
      <td>${cap.reference}</td> <!-- Référence commerciale -->
      <td>${cap.port_communication || ""}</td> <!-- Port de communication -->
      <td>
        <!-- Bouton pour supprimer un capteur -->
        <button class="btn btn-danger btn-sm" onclick="deleteCapteur(${cap.id_capteur})">Supprimer</button>
      </td>
    `;
    tbody.appendChild(tr); // Ajoute la ligne au tableau
  });
}

// Fonction pour supprimer un capteur via l'API
function deleteCapteur(id_capteur) {
  if (!confirm(`Êtes-vous sûr de vouloir supprimer le capteur ID ${id_capteur} ?`)) return;

  fetch(`${CONFIG_BASE_URL}/api/capteurs/${id_capteur}`, {
    method: "DELETE" // Méthode DELETE pour supprimer
  })
  .then(res => {
    if (!res.ok) {
      return res.json().then(err => { throw err; });
    }
    return res.json();
  })
  .then(response => {
    alert(response.detail); // Message de confirmation
    loadCapteursFromAPI(); // Recharge la liste des capteurs
  })
  .catch(err => {
    console.error("Erreur DELETE capteur:", err); // Affiche les erreurs dans la console
    alert(`Erreur: ${err.detail || err.message}`); // Affiche un message d'erreur
  });
}
