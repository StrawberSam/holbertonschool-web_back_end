// 5-http.js
const http = require('http');
const countStudents = require('./3-read_file_async');

const PORT = 1245;

const app = http.createServer(async (req, res) => {
  res.setHeader('Content-Type', 'text/plain; charset=utf-8');

  if (req.url === '/') {
    res.statusCode = 200;
    res.end('Hello Holberton School!');
    return;
  }

  if (req.url === '/students') {
    res.statusCode = 200;
    const dbPath = process.argv[2];

    let body = 'This is the list of our students\n';

    // On capture temporairement console.log pour récupérer exactement
    // les lignes que ton 3-read_file_async.js affiche.
    const originalLog = console.log;
    const logs = [];
    console.log = (...args) => {
      const line = args.join(' ');
      logs.push(line);
      originalLog(...args); // on continue d'afficher en console (optionnel)
    };

    try {
      await countStudents(dbPath); // ta fonction ne retourne rien mais logge tout
      console.log = originalLog; // on restaure
      body += logs.join('\n'); // on renvoie les mêmes lignes dans la réponse HTTP
    } catch (e) {
      console.log = originalLog; // on restaure même en cas d'erreur
      body += 'Cannot load the database';
    }

    res.end(body);
    return;
  }

  // Optionnel
  res.statusCode = 404;
  res.end('Not found');
});

app.listen(PORT);
module.exports = app;
