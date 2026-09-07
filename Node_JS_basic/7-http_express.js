const express = require('express');
const fs = require('fs');

const app = express();
const PORT = 1245;
const DB_FILE = process.argv[2];

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf-8', (err, fileContent) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = fileContent.split('\n').filter((line) => line.trim() !== '');
      const studentLines = lines.slice(1);

      const fields = {};
      let total = 0;

      studentLines.forEach((line) => {
        const [firstname, , , field] = line.split(',');
        if (!field) {
          return;
        }
        total += 1;
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstname);
      });

      const output = [`Number of students: ${total}`];
      Object.keys(fields).forEach((field) => {
        const names = fields[field];
        output.push(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
      });

      resolve(output.join('\n'));
    });
  });
}

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  countStudents(DB_FILE)
    .then((report) => {
      res.send(`This is the list of our students\n${report}`);
    })
    .catch((err) => {
      res.send(`This is the list of our students\n${err.message}`);
    });
});

app.listen(PORT);

module.exports = app;
