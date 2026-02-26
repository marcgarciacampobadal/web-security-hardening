# hardened_app/app.py
from flask import Flask, request, render_template_string
import sqlite3
import bcrypt

app = Flask(__name__)
app.config['DEBUG'] = False  # Debug mode off for production

# In-memory SQLite database for demo
conn = sqlite3.connect(':memory:', check_same_thread=False)
cursor = conn.cursor()

# Create users table
cursor.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL
)
''')
conn.commit()

# Add admin user with hashed password
password_plain = "password123"
password_hash = bcrypt.hashpw(password_plain.encode(), bcrypt.gensalt())
cursor.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)', ('admin', password_hash))
conn.commit()

# Simple HTML template
login_page = '''
<!doctype html>
<title>Hardened Login</title>
<h2>Login</h2>
<form method="POST">
  Username: <input type="text" name="username"><br>
  Password: <input type="password" name="password"><br>
  <input type="submit" value="Login">
</form>
<p>{{ message }}</p>
'''

def validate_input(input_str):
    """Basic input validation to allow only alphanumerics."""
    return input_str.isalnum()

@app.route('/', methods=['GET', 'POST'])
def login():
    message = ""
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')

        # Input validation
        if not validate_input(username) or not validate_input(password):
            message = "Invalid characters detected!"
        else:
            # Parameterized query to prevent SQL injection
            cursor.execute('SELECT password_hash FROM users WHERE username = ?', (username,))
            result = cursor.fetchone()
            if result and bcrypt.checkpw(password.encode(), result[0]):
                message = "Login successful!"
            else:
                message = "Login failed!"
    return render_template_string(login_page, message=message)

if __name__ == '__main__':
    app.run()