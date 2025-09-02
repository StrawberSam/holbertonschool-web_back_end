// Afficher un message au début
console.log('Welcome to Holberton School, what is your name?');

// Ecouter ce que tape l'utilisateur
process.stdin.on('data', (data) => {
  const name = data.toString().trim();
  console.log(`Your name is: ${name}`);
});

// Le message de fermeture
process.stdin.on('end', () => {
  console.log('This important software is now closing');
});

// data = ce que l’utilisateur a écrit (sous forme de Buffer).
// toString() → transforme ce Buffer en texte lisible.
// trim() → enlève les espaces et le retour à la ligne (\n).
