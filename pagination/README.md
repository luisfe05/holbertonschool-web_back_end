# Pagination

## Description
This project covers pagination techniques for a dataset: computing simple page/page_size index ranges, adding hypermedia metadata (page count, next/previous page) to paginated responses, and paginating in a way that stays correct even if rows are deleted between requests. Data comes from `Popular_Baby_Names.csv`. All functions are type-annotated, and every module/function has a real-sentence docstring.

## Tasks

| Task | Description | File |
| :--- | :--- | :--- |
| **0. Simple helper function** | `index_range(page, page_size)` returns the `(start, end)` index tuple for a 1-indexed page. | `0-simple_helper_function.py` |
| **1. Simple pagination** | `Server.get_page(page, page_size)` returns the correct slice of the dataset for a given page, using `index_range`. Returns an empty list if out of range. | `1-simple_pagination.py` |
| **2. Hypermedia pagination** | `Server.get_hyper(page, page_size)` returns pagination metadata (page, page_size, data, next_page, prev_page, total_pages) built on top of `get_page`. | `2-hypermedia_pagination.py` |
| **3. Deletion-resilient hypermedia pagination** | `Server.get_hyper_index(index, page_size)` returns a page keyed by dataset index that stays correct even if rows are deleted between requests. | `3-hypermedia_del_pagination.py` |

## Author
* **Luis Gonzalez** - Holberton School
