# Python - Serialization

This project explores **serialization** and **marshaling**: transforming
in-memory Python objects into formats that can be stored or transmitted,
then reconstructing them in an identical state. It covers three formats:
JSON, pickle (binary) and XML, plus converting data from CSV to JSON.

## Learning Objectives

- Articulate the differences and similarities between marshaling and serialization
- Implement serialization in a practical programming task
- Understand how serialized data is used in web applications, databases and network communications
- Evaluate the performance implications of different formats: JSON, XML and binary

## Requirements

- Ubuntu 20.04 LTS, Python 3
- First line of every file: `#!/usr/bin/env python3`
- All files end with a new line and are executable
- Code follows `pycodestyle`

## Files

| File | Description |
|------|-------------|
| `task_00_basic_serialization.py` | `serialize_and_save_to_file(data, filename)` saves a dictionary to a JSON file (overwriting it if it exists); `load_and_deserialize(filename)` loads a JSON file and returns a dictionary |
| `task_01_pickle.py` | `CustomObject` class (`name`, `age`, `is_student`) with `display()`, `serialize(filename)` and the class method `deserialize(filename)` using `pickle`; returns `None` for missing or malformed files |
| `task_02_csv.py` | `convert_csv_to_json(csv_filename)` reads a CSV file with `csv.DictReader` and writes the rows to `data.json`; returns `True` on success, `False` on failure |
| `task_03_xml.py` | `serialize_to_xml(dictionary, filename)` writes a dictionary as XML under a `<data>` root; `deserialize_from_xml(filename)` parses the XML back into a dictionary |

## Format Comparison

| Format | Output | Human-readable | Cross-language | Safe with untrusted data |
|--------|--------|----------------|----------------|--------------------------|
| JSON | Text | Yes | Yes | Yes |
| XML | Text | Yes | Yes | Yes |
| pickle | Binary | No | Python only | No |

## Author

Khaled Al-Yahya
