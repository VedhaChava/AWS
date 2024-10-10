from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

# Get the absolute path to the current directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, 'users.db')

# Function to initialize the SQLite database
def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT NOT NULL
            )
        ''')
        conn.commit()

@app.route('/')
def home():
    return redirect(url_for('register'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']

        try:
            with sqlite3.connect(DATABASE) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO users (username, password, first_name, last_name, email)
                    VALUES (?, ?, ?, ?, ?)
                ''', (username, password, first_name, last_name, email))
                conn.commit()
            return redirect(url_for('retrieve'))
        except sqlite3.Error as e:
            return f"An error occurred: {e}"

    return render_template('register.html')

@app.route('/retrieve', methods=['GET', 'POST'])
def retrieve():
    user_info = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        try:
            with sqlite3.connect(DATABASE) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT first_name, last_name, email FROM users WHERE username=? AND password=?', (username, password))
                user_info = cursor.fetchone()
        except sqlite3.Error as e:
            return f"An error occurred: {e}"

    return render_template('retrieve.html', user_info=user_info)

@app.route('/display')
def display():
    return render_template('display.html')

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=80)
