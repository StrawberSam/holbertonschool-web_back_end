const fs = require('fs');

function countStudents(path) {
  let content;
  try {
    // Lecture du fichier CSV en mode synchrone
    // 'utf-8' permet de récupérer une chaîne directement
    content = fs.readFileSync(path, 'utf-8');
  } catch (e) {
    // Si le fichier n’existe pas ou est inaccessible,
    // on lève une erreur avec le message exact demandé
    throw new Error('Cannot load the database');
  }

  // On découpe le contenu du fichier en lignes
  // .trim() supprime les espaces et les retours Windows \r
  // .filter() supprime les lignes vides (par ex. en fin de fichier)
  const lines = content
    .split('\n')
    .map((line) => line.trim())
    .filter((line) => line.length > 0);

  // Si le fichier est vide (aucune ligne), on affiche "0 étudiants"
  if (lines.length === 0) {
    console.log('Number of students: 0');
    return;
  }

  // On récupère l'entête (première ligne du CSV)
  const header = lines[0].split(',').map((h) => h.trim());

  // On repère dynamiquement l’index des colonnes "firstname" et "field"
  const firstIdx = header.indexOf('firstname');
  const fieldIdx = header.indexOf('field');

  // Tableau qui contiendra les étudiants valides
  const students = [];

  // On parcourt toutes les lignes sauf l’entête
  for (const line of lines.slice(1)) {
    const cols = line.split(',').map((c) => c.trim());

    // On vérifie que la ligne contient bien assez de colonnes
    if (cols.length <= Math.max(firstIdx, fieldIdx)) {
      const firstname = cols[firstIdx];
      const field = cols[fieldIdx];

      if (firstname && field) {
        students.push({ firstname, field });
      }
    }
  }

  // Nombre total d’étudiants valides
  const total = students.length;

  // Objet qui regroupera les étudiants par filière
  const groups = {};
  // Tableau pour garder l’ordre d’apparition des filières
  const order = [];

  // Affiche le nombre total d’étudiants
  console.log(`Number of students: ${total}`);

  // On parcourt tous les étudiants pour les classer par field
  for (const s of students) {
    const f = s.field;

    // Si c’est la première fois qu’on rencontre cette filière
    if (!groups[f]) {
      groups[f] = [];
      order.push(f); // on garde l’ordre d’apparition
    }
    // On ajoute le prénom de l’étudiant dans la bonne filière
    groups[f].push(s.firstname);
  }

  // Pour chaque filière dans l’ordre, on affiche le format demandé
  for (const f of order) {
    const list = groups[f].join(', ');
    console.log(
      `Number of students in ${f}: ${groups[f].length}. List: ${list}`,
    );
  }
}

// On exporte la fonction pour pouvoir l’utiliser dans un autre fichier
module.exports = countStudents;
