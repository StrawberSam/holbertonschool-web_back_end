// Afficher un message au début
process.stdout.write('Welcome to Holberton School, what is your name?\n');

// Ecouter ce que tape l'utilisateur
process.stdin.on('data', (data) => {
  process.stdout.write(`Your name is: ${data}`);
});

// Le message de fermeture
process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing');
});
