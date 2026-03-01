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

@app.route('/about')
def about(): return render_template('page.html', title="About Us")
@app.route('/contact')
def contact(): return render_template('page.html', title="Contact")
@app.route('/location')
def location(): return render_template('page.html', title="Location")
@app.route('/faq')
def faq(): return render_template('page.html', title="FAQ")
@app.route('/gallery')
def gallery(): return render_template('page.html', title="Gallery")
@app.route('/promotions')
def promotions(): return render_template('page.html', title="Promotions")
@app.route('/events')
def events(): return render_template('page.html', title="Events")
@app.route('/reviews')
def reviews(): return render_template('page.html', title="Reviews")