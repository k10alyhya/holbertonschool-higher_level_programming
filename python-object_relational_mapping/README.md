# Python - Object-relational mapping

This project links **Python** and **MySQL** in two ways:

1. **MySQLdb**: writing raw SQL queries from a Python script.
2. **SQLAlchemy (ORM)**: working with Python classes and objects instead of SQL.

## Learning Objectives

- How to connect to a MySQL database from a Python script
- How to `SELECT`, `INSERT`, `UPDATE` and `DELETE` rows from Python
- What an ORM is and why it is useful
- How to map a Python class to a MySQL table
- How to prevent SQL injection with parameterized queries

## Requirements

- Ubuntu 20.04 LTS, Python 3.8
- MySQL 8.0
- MySQLdb (`mysqlclient`) 2.0.x
- SQLAlchemy 1.4.x
- Code style: `pycodestyle` 2.7
- All files are executable and start with `#!/usr/bin/python3`

## Setup

```bash
sudo apt install mysql-server python3-dev default-libmysqlclient-dev build-essential pkg-config
pip3 install mysqlclient "SQLAlchemy>=1.4,<2.0"
```

Every script takes the MySQL credentials and database name as arguments:

```bash
./script.py <mysql_username> <mysql_password> <database_name>
```

## MySQLdb vs SQLAlchemy

| | MySQLdb | SQLAlchemy ORM |
|---|---|---|
| Connection | `MySQLdb.connect(...)` | `create_engine(...)` |
| Work unit | `cursor()` | `Session(engine)` |
| Query | `cur.execute("SELECT * FROM states")` | `session.query(State).all()` |
| Result | tuple: `row[1]` | object: `state.name` |
| Writing SQL | Yes | No |

## Tasks

### Part 1: MySQLdb

| # | File | Description | Key concept |
|---|---|---|---|
| 0 | `0-select_states.py` | Lists all states sorted by `id` | `connect`, `cursor`, `execute`, `fetchall` |
| 1 | `1-filter_states.py` | Lists states whose name starts with `N` | `LIKE BINARY 'N%'` (case sensitive) |
| 2 | `2-my_filter_states.py` | Displays states matching a user argument | `format()` (vulnerable to SQL injection) |
| 3 | `3-my_safe_filter_states.py` | Same as task 2, safe from SQL injection | Parameterized query: `execute(sql, (value,))` |
| 4 | `4-cities_by_state.py` | Lists all cities with their state name | `INNER JOIN`, one `execute()` only |
| 5 | `5-filter_cities.py` | Lists all cities of a given state | `JOIN` + safe parameter + `", ".join()` |

### Part 2: SQLAlchemy ORM

| # | File | Description | Key concept |
|---|---|---|---|
| 6 | `model_state.py` | `State` class mapped to table `states` | `declarative_base`, `Column`, `__tablename__` |
| 7 | `7-model_state_fetch_all.py` | Lists all `State` objects | `session.query(State).order_by(State.id).all()` |
| 8 | `8-model_state_fetch_first.py` | Prints the first `State` or `Nothing` | `.first()` returns an object or `None` |
| 9 | `9-model_state_filter_a.py` | Lists states containing the letter `a` | `.filter(State.name.like('%a%'))` |
| 10 | `10-model_state_my_get.py` | Prints the `id` of a state by name or `Not found` | `.filter(State.name == arg)` (injection safe) |
| 11 | `11-model_state_insert.py` | Adds the state `Louisiana` and prints its `id` | `session.add()` + `session.commit()` |
| 12 | `12-model_state_update_id_2.py` | Renames the state with `id = 2` to `New Mexico` | Modify attribute + `commit()` |
| 13 | `13-model_state_delete_a.py` | Deletes all states containing the letter `a` | `session.delete()` + one `commit()` |
| 14 | `model_city.py`, `14-model_city_fetch_by_state.py` | `City` class and list of cities with their state | `ForeignKey('states.id')`, `query(City, State)` |

## Key Lessons

- **SQL injection**: never build SQL with `format()` from user input. Use placeholders (`%s`) with MySQLdb, or the ORM, which escapes values automatically.
- **Class vs object**: use the class (`State.id`) inside `query`, `filter` and `order_by`, and the object (`state.id`) to read values.
- **`commit()`**: `add`, update and `delete` are only saved to the database after `session.commit()`.
- **Shared `Base`**: all models must inherit from the same `Base` so SQLAlchemy can resolve foreign keys.

## Author

Khaled Al-Yahya: [GitHub](https://github.com/k10alyhya)
