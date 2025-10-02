const express = require('express');
const fs = require('fs');
const app = express();

const student = process.env.STUDENT_NAME || "Anon";
const hood = process.env.BARRIO || "Unknown";

app.get('/', (req, res) => {
  const msg = `Hola, I am ${student} and I live in ${hood}`;
  fs.appendFileSync('/var/log/app/visitas.log', msg + '\n');
  res.type('text/plain').send(msg);
});

app.get('/health', (req, res) => res.json({ ok: true }));

app.listen(8080, () => console.log("Server running on 8080"));
