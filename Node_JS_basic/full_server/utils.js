import fs from 'fs';

const readDatabase = (path) => new Promise((resolve, reject) => {
  fs.readFile(path, 'utf-8', (err, fileContent) => {
    if (err) {
      reject(new Error('Cannot load the database'));
      return;
    }

    const lines = fileContent.split('\n').filter((line) => line.trim() !== '');
    const studentLines = lines.slice(1);

    const students = {};

    studentLines.forEach((line) => {
      const [firstname, , , field] = line.split(',');
      if (!field) {
        return;
      }
      if (!students[field]) {
        students[field] = [];
      }
      students[field].push(firstname);
    });

    resolve(students);
  });
});

export default readDatabase;
