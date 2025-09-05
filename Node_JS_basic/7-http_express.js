// 7-http_express.js
const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const PORT = 1245;

app.get('/', (req, res) => {
  res.set('Content-Type', 'text/plain; charset=utf-8');
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  res.set('Content-Type', 'text/plain; charset=utf-8');

  const dbPath = process.argv[2];
  let body = 'This is the list of our students\n';

  // Capture console.log SANS réécrire dans la console
  const originalLog = console.log;
  const logs = [];
  console.log = (...args) => {
    logs.push(args.join(' '));
    // pas de originalLog(...args)
  };

  try {
    await countStudents(dbPath);
    body += logs.join('\n');
  } catch {
    body += 'Cannot load the database';
  } finally {
    console.log = originalLog; // toujours restaurer
  }

  res.send(body);
});

app.listen(PORT);
module.exports = app;
