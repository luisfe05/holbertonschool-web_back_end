# ES6 Basics

## Description
This project covers ES6 (ECMAScript 2015+) fundamentals: `const`/`let` vs `var`, block scope, arrow functions, default and rest parameters, spread syntax, template literals, ES6 object property shorthand/computed properties, and iterators/`for...of`. Code is written in `.js`, transpiled with Babel, tested with Jest, and linted with ESLint (Airbnb base config).

## Tasks

| Task | Description | File |
| :--- | :--- | :--- |
| **0. Const or let?** | `taskFirst` uses `const`, `taskNext` uses `let`, replacing `var`. | `0-constants.js` |
| **1. Block Scope** | `taskBlock` uses block-scoped `const` declarations inside the `if` so the outer variables are never touched. | `1-block-scoped.js` |
| **2. Arrow functions** | `getNeighborhoodsList` uses an arrow function for `addNeighborhood`, dropping the `self = this` workaround. | `2-arrow.js` |
| **3. Parameter defaults** | `getSumOfHoods` uses default parameter values instead of manual `undefined` checks, condensed to one line. | `3-default-parameter.js` |
| **4. Rest parameter syntax for functions** | `returnHowManyArguments` uses the rest parameter (`...args`) to count however many arguments it's called with. | `4-rest-parameter.js` |
| **5. The wonders of spread syntax** | `concatArrays` uses spread syntax to concatenate two arrays and a string's characters into one array. | `5-spread-operator.js` |
| **6. Take advantage of template literals** | `getSanFranciscoDescription` rebuilds the return string using a template literal instead of concatenation. | `6-string-interpolation.js` |
| **7. Object property value shorthand syntax** | `getBudgetObject` uses shorthand property names instead of repeating `key: key`. | `7-getBudgetObject.js` |
| **8. No need to create empty objects before adding in properties** | `getBudgetForCurrentYear` uses ES6 computed property names to build keys like `income-<year>` directly in the object literal. | `8-getBudgetCurrentYear.js` |
| **9. ES6 method properties** | `getFullBudgetObject` uses ES6 method shorthand for `getIncomeInDollars`/`getIncomeInEuros` instead of `key: function(...) {}`. | `9-getFullBudget.js` |
| **10. For...of Loops** | `appendToEachArrayValue` uses a `for...of` loop over the array's values instead of `for...in` over indices with `var`. | `10-loops.js` |
| **11. Iterator** | `createEmployeesObject` builds `{ [departmentName]: employees }` using a computed property name. | `11-createEmployeesObject.js` |
| **12. Let's create a report object** | `createReportObject` returns `allEmployees` (spread copy of the input) plus a `getNumberOfDepartments` method property. | `12-createReportObject.js` |

## Author
* **Luis Gonzalez** - Holberton School
