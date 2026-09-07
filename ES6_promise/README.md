# ES6 Promises

## Description
This project covers ES6 Promises: creating and resolving/rejecting them, chaining with `then`/`catch`, combining multiple promises (`Promise.all`, `Promise.allSettled`, `Promise.race`), and `async`/`await` with `try`/`catch` error handling.

## Tasks

| Task | Description | File |
| :--- | :--- | :--- |
| **0. Keep every promise you make and only make promises you can keep** | `getResponseFromAPI` returns a `Promise` instance. | `0-promise.js` |
| **1. Don't make a promise...if you know you can't keep it** | `getFullResponseFromAPI(success)` resolves with `{status, body}` or rejects with an `Error`, based on the boolean argument. | `1-promise.js` |
| **2. Catch me if you can!** | `handleResponseFromAPI` chains `.then()`, `.catch()`, and `.finally()` to normalize the result and always log a message. | `2-then.js` |
| **3. Handle multiple successful promises** | `handleProfileSignup` uses `Promise.all` to combine `uploadPhoto` and `createUser`. | `3-all.js` |
| **4. Simple promise** | `signUpUser(firstName, lastName)` returns a promise resolved with `{firstName, lastName}`. | `4-user-promise.js` |
| **5. Reject the promises** | `uploadPhoto(filename)` returns a promise rejected with `` `${filename} cannot be processed` ``. | `5-photo-reject.js` |
| **6. Handle multiple promises** | `handleProfileSignup` uses `Promise.allSettled` to combine `signUpUser` and `uploadPhoto`, normalizing both outcomes into `{status, value}`. | `6-final-user.js` |

## Author
* **Luis Gonzalez** - Holberton School
