from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS menu (id INTEGER PRIMARY KEY, name TEXT, price REAL)')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM menu')
    items = c.fetchall()
    conn.close()
    return render_template('index.html', items=items)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('INSERT INTO menu (name, price) VALUES (?, ?)', (name, price))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add.html')