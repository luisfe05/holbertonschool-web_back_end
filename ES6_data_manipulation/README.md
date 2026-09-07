# ES6 Data Manipulation

## Description
This project covers ES6 data manipulation: `map`/`filter`/`reduce` on arrays, typed arrays and `ArrayBuffer`/`DataView`, and the `Set`/`Map`/`WeakMap` data structures.

## Tasks

| Task | Description | File |
| :--- | :--- | :--- |
| **0. Basic list of objects** | `getListStudents` returns an array of student objects (`id`, `firstName`, `location`). | `0-get_list_students.js` |
| **1. More mapping** | `getListStudentIds` uses `map` to extract just the `id` of each student; returns `[]` if not given an array. | `1-get_list_student_ids.js` |
| **2. Filter** | `getStudentsByLocation` uses `filter` to return only students in a given city. | `2-get_students_by_loc.js` |
| **3. Reduce** | `getStudentIdsSum` uses `reduce` to sum every student's `id`. | `3-get_ids_sum.js` |
| **4. Combine** | `updateStudentGradeByCity` chains `filter` + `map` to attach a grade (or `'N/A'`) to students in a given city. | `4-update_grade_by_city.js` |
| **5. Typed Arrays** | `createInt8TypedArray` writes an Int8 value into an `ArrayBuffer` via `DataView`, throwing if the position is out of range. | `5-typed_arrays.js` |
| **6. Set data structure** | `setFromArray` builds a `Set` from an array, deduplicating values. | `6-set.js` |
| **7. More set data structure** | `hasValuesFromArray` returns whether every element of an array is present in a `Set`. | `7-has_array_values.js` |
| **8. Clean set** | `cleanSet` joins every set value that starts with `startString` (prefix stripped) with `-`; empty for a falsy `startString`. | `8-clean_set.js` |
| **9. Map data structure** | `groceriesList` returns a `Map` of grocery items to quantities. | `9-groceries_list.js` |
| **10. More map data structure** | `updateUniqueItems` sets every entry with quantity `1` to `100`, mutating the map in place; throws if not given a `Map`. | `10-update_uniq_items.js` |

## Author
* **Luis Gonzalez** - Holberton School
