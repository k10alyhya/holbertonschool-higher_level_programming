# Python - Server-Side Rendering

This project covers server-side rendering (SSR) with Python, Flask and the Jinja templating engine.
Pages are built on the server and sent to the browser as complete HTML, using data from JSON, CSV and SQLite sources.

## Learning Objectives

- Understand server-side rendering and how it differs from client-side rendering
- Learn the benefits of server-side rendering
- Implement SSR in Python using Flask
- Use Jinja to generate HTML pages dynamically
- Read and display data from JSON, CSV and SQLite
- Handle dynamic content and user inputs

## Requirements

- Python 3
- Flask (`pip install Flask`)
- Code follows PEP 8 (pycodestyle)

## Tasks

| Task | File | Description |
|------|------|-------------|
| 0 | `task_00_intro.py` | Generates personalized invitation files (`output_X.txt`) from a template, with error handling for empty or invalid inputs and `N/A` for missing data |
| 1 | `task_01_jinja.py` | Basic Flask app rendering `index.html`, `about.html` and `contact.html` with a shared header and footer using `{% include %}` |
| 2 | `task_02_logic.py` | `/items` route that reads `items.json` and displays the items with Jinja loops and conditions |
| 3 | `task_03_files.py` | `/products` route that displays products from JSON or CSV using `?source=json\|csv` and an optional `&id=` filter |
| 4 | `task_04_db.py` | Extends task 3 with a SQLite source (`?source=sql`) and database error handling |

## Data Files

- `template.txt`: invitation template
- `items.json`: items list for task 2
- `products.json` and `products.csv`: product data for tasks 3 and 4
- `products.db`: SQLite database, created by `create_database.py`

## Usage

```bash
python3 create_database.py
python3 task_04_db.py
```

Then open:

- `http://localhost:5000/products?source=json`
- `http://localhost:5000/products?source=csv`
- `http://localhost:5000/products?source=sql&id=1`

## Author

Khaled Al-Yahya
