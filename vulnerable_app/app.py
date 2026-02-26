from flask import Flask, request
import sqlite3

app = Flask(__name__)
app.config['DEBUG'] = True  # Debug activado (vulnerable)

# Hardcoded credentials (vulnerable)
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password123"

def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT
        )
    ''')
    cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'password123')")
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return '''
        <h2>Login</h2>
        <form method="POST" action="/login">
            Username: <input type="text" name="username"><br>
            Password: <input type="text" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # 🚨 VULNERABLE SQL QUERY (SQL Injection possible)
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    result = cursor.execute(query).fetchone()

    conn.close()

    if result:
        return "Login successful!"
    else:
        return "Login failed."

if __name__ == '__main__':
    init_db()
    app.run()