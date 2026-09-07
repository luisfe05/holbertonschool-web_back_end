# ES6 Classes

## Description
This project covers ES6 classes: defining a class, constructors, getters/setters with type validation, static methods, extending a class (inheritance), abstract-style base classes, `toString`/primitive coercion via `Symbol.toPrimitive`, hoisting pitfalls with classes, and cloning objects with `Object.assign`/`Symbol`.

## Tasks

| Task | Description | File |
| :--- | :--- | :--- |
| **0. You used to attend a place like this at some point** | `ClassRoom` stores `maxStudentsSize` as `_maxStudentsSize`. | `0-classroom.js` |
| **1. Let's make some classrooms** | `initializeRooms` returns an array of 3 `ClassRoom` instances (sizes 19, 20, 34). | `1-make_classrooms.js` |
| **2. A Course, Getters, and Setters** | `HolbertonCourse` validates `name`/`length`/`students` types via getters/setters used both at construction and on later assignment. | `2-hbtn_course.js` |
| **3. Methods, static methods, computed methods names..... MONEY** | `Currency` has `code`/`name` getters/setters and a `displayFullCurrency` method (`name (code)`). | `3-currency.js` |
| **4. Pricing** | `Pricing` has `displayFullPrice` and a static `convertPrice(amount, conversionRate)` method; `currency` setter validates it's a `Currency` instance. | `4-pricing.js` |
| **5. A Building** | `Building` acts as an abstract base class, throwing in its constructor if a subclass doesn't override `evacuationWarningMessage`. | `5-building.js` |
| **6. Inheritance** | `SkyHighBuilding` extends `Building`, calling `super(sqft)` and overriding `evacuationWarningMessage`. | `6-sky_high.js` |
| **7. Airport** | `Airport` uses `Symbol.toStringTag` so its default string description is the airport code. | `7-airport.js` |
| **8. Primitive - Holberton Class** | `HolbertonClass` uses `Symbol.toPrimitive` so `Number(hc)` returns `size` and `String(hc)` returns `location`. | `8-hbtn_class.js` |
| **9. Hoisting** | Fixes 5 bugs in broken class-ordering/`this`/constructor code so `listOfStudents` builds and describes correctly. | `9-hoisting.js` |
| **10. Vroom** | `Car.cloneCar()` uses `Symbol.species` to return a blank new instance of whatever class actually built `this` (even a subclass). | `10-car.js` |

## Author
* **Luis Gonzalez** - Holberton School
