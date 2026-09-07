# Node JS Basics

## Description
This project covers core Node.js: running JavaScript with `node`, reading files synchronously and asynchronously, using `process` for stdin/args, building HTTP servers with the raw `http` module and with Express, and organizing a larger Express app into controllers/routes with Babel/ES6 (`full_server`).

## Tasks

| Task | Description | File |
| :--- | :--- | :--- |
| **0. Executing basic javascript with Node JS** | `displayMessage` prints a string argument to STDOUT. | `0-console.js` |
| **1. Using Process stdin** | Reads a name from `process.stdin` and prints a welcome/goodbye flow. | `1-stdin.js` |
| **2. Reading a file synchronously** | `countStudents` reads `database.csv` synchronously and logs student counts grouped by field. | `2-read_file.js` |
| **3. Reading a file asynchronously** | Same as task 2, but returns a Promise and reads the file asynchronously. | `3-read_file_async.js` |
| **4. Create a small HTTP server using Node's HTTP module** | Raw `http` server on port 1245; every endpoint returns `Hello Holberton School!`. | `4-http.js` |
| **5. Create a more complex HTTP server using Node's HTTP module** | Raw `http` server: `/` returns a greeting, `/students` returns the student count report from `database.csv`. | `5-http.js` |

## Author
* **Luis Gonzalez** - Holberton School
