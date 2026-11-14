#!/usr/bin/python3
"""Flask application displaying products from JSON, CSV or SQLite."""
import csv
import json
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json(filename='products.json'):
    """Read products from a JSON file."""
    with open(filename, 'r') as file:
        return json.load(file)


def read_csv(filename='products.csv'):
    """Read products from a CSV file."""
    products = []
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    return products


def read_sql(db_name='products.db'):
    """Read products from the SQLite database."""
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        return [dict(row) for row in cursor.fetchall()]
    finally:
        conn.close()


@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('contact.html')


@app.route('/items')
def items():
    """Render the items list read from items.json."""
    try:
        with open('items.json', 'r') as file:
            items_list = json.load(file).get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        items_list = []
    return render_template('items.html', items=items_list)


@app.route('/products')
def products():
    """Display products from json, csv or sql, optionally by id."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    try:
        if source == 'json':
            data = read_json()
        elif source == 'csv':
            data = read_csv()
        elif source == 'sql':
            data = read_sql()
        else:
            return render_template('product_display.html',
                                   error="Wrong source")
    except sqlite3.Error as e:
        return render_template('product_display.html',
                               error="Database error: {}".format(e))
    except (OSError, ValueError, KeyError) as e:
        return render_template('product_display.html',
                               error="Error reading data: {}".format(e))

    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template('product_display.html',
                                   error="Product not found")
        data = [p for p in data if int(p['id']) == product_id]
        if not data:
            return render_template('product_display.html',
                                   error="Product not found")

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
