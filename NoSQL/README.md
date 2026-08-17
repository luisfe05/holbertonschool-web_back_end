# NoSQL

## Description
This project covers NoSQL concepts using MongoDB: querying, inserting, updating, and deleting documents via the mongo shell, plus equivalent operations in Python with PyMongo. Every shell script starts with a `//` comment, every Python module/function is documented, and Python code follows pycodestyle.

## Tasks

| Task | Description | File |
| :--- | :--- | :--- |
| **0. List all databases** | Lists all databases in MongoDB. | `0-list_databases` |
| **1. Create a database** | Switches to (and lazily creates) the database `my_db`. | `1-use_or_create_database` |
| **2. Insert document** | Inserts a document (`name: "Holberton school"`) into the `school` collection. | `2-insert` |
| **3. All documents** | Lists every document in the `school` collection. | `3-all` |
| **4. All matches** | Lists documents in `school` where `name` equals `"Holberton school"`. | `4-match` |
| **5. Count** | Displays the number of documents in the `school` collection. | `5-count` |
| **6. Update** | Adds an `address` field to every document in `school` with `name` equal to `"Holberton school"`. | `6-update` |
| **7. Delete by match** | Deletes every document in `school` with `name` equal to `"Holberton school"`. | `7-delete` |
| **8. List all documents in Python** | `list_all(mongo_collection)` returns every document in a collection as a list, or `[]` if empty. | `8-all.py` |
| **9. Insert a document in Python** | `insert_school(mongo_collection, **kwargs)` inserts a document built from keyword arguments and returns its new `_id`. | `9-insert_school.py` |
| **10. Change school topics** | `update_topics(mongo_collection, name, topics)` sets the `topics` list on every document matching `name`. | `10-update_topics.py` |
| **11. Where can I learn Python?** | `schools_by_topic(mongo_collection, topic)` returns the list of schools whose `topics` include the given topic. | `11-schools_by_topic.py` |
| **12. Log stats** | Prints stats (total count, counts per HTTP method, GET `/status` count) for the `logs.nginx` collection. | `12-log_stats.py` |

## Author
* **Luis Gonzalez** - Holberton School
