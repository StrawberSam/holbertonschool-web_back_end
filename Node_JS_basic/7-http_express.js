// 7-http_express.js
const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const PORT = 1245;

// Plain text pour toutes les réponses de ces routes
app.get('/', (req, res) => {
  res.set('Content-Type', 'text/plain; charset=utf-8');
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  res.set('Content-Type', 'text/plain; charset=utf-8');

  const dbPath = process.argv[2];
  let body = 'This is the list of our students\n';

  // Capture temporaire de console.log pour récupérer exactement
  // ce que 3-read_file_async.js affiche
  const originalLog = console.log;
  const logs = [];
  console.log = (...args) => {
    const line = args.join(' ');
    logs.push(line);
    originalLog(...args); // Optionnel : laisser apparaître dans la console
  };

  try {
    await countStudents(dbPath);
    console.log = originalLog; // restaurer
    body += logs.join('\n');
  } catch (_) {
    console.log = originalLog; // restaurer même en cas d’erreur
    body += 'Cannot load the database';
  }

  res.send(body);
});

// Écoute et export
app.listen(PORT);
module.exports = app;
