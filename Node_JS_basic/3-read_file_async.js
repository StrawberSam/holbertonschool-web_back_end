// Import du module fs avec support Promises
const fs = require('fs').promises;

async function countStudents(path) {
  let data;

  try {
    // Lecture asynchrone du fichier CSV en UTF-8
    data = await fs.readFile(path, 'utf-8');
  } catch (err) {
    // Gestion d’erreur : message exact attendu par la consigne
    throw new Error('Cannot load the database');
  }

  // Découpe du fichier en lignes, suppression des lignes vides éventuelles
  const lines = data.trim().split('\n');
  const rows = lines.slice(1).filter((line) => line.trim() !== '');
  // on ignore l’en-tête

  // On récupère les index des colonnes utiles dynamiquement
  const header = lines[0].trim().split(',');
  const idxFirst = header.indexOf('firstname');
  const idxField = header.indexOf('field');

  // Initialisation des compteurs
  let total = 0;
  const groups = {}; // objet qui regroupe les prénoms par filière

  // Boucle sur chaque ligne étudiante
  for (const row of rows) {
    const cols = row.trim().split(',');

    // Vérification que la ligne a bien assez de colonnes
    if (cols.length >= header.length) {
      const firstname = cols[idxFirst].trim();
      const field = cols[idxField].trim();

      // Incrément du total
      total += 1;

      // Initialisation du tableau si la filière n’existe pas encore
      if (!groups[field]) {
        groups[field] = [];
      }

      // Ajout du prénom dans le groupe correspondant
      groups[field].push(firstname);
    }
  }

  // Affichage du total
  console.log(`Number of students: ${total}`);

  // Affichage des détails par filière
  for (const field of Object.keys(groups)) {
    console.log(
      `Number of students in ${field}: ${groups[field].length}. List: ${groups[field].join(', ')}`,
    );
  }
}

module.exports = countStudents;
