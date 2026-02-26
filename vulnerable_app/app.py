from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)
app.config['DEBUG'] = True  # Mantenemos debug activado para demostrar vulnerabilidad

# In-memory SQLite database
conn = sqlite3.connect(':memory:', check_same_thread=False)
cursor = conn.cursor()

# Create users table
cursor.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
''')
conn.commit()

# Insert admin user (plaintext password)
cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'password123')")
conn.commit()

# HTML template
login_page = '''
<!doctype html>
<title>Vulnerable Login</title>
<h2>Login (Vulnerable)</h2>
<form method="POST">
  Username: <input type="text" name="username"><br>
  Password: <input type="text" name="password"><br>
  <input type="submit" value="Login">
</form>
<p>{{ message }}</p>
'''

@app.route('/', methods=['GET', 'POST'])
def login():
    message = ""
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')

        # ❌ VULNERABLE: input concatenado directamente
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        print("Executing query:", query)  # para ver la inyección en consola

        try:
            cursor.execute(query)
            result = cursor.fetchone()
            if result:
                message = "Login successful!"
            else:
                message = "Login failed!"
        except Exception as e:
            message = f"SQL Error: {e}"

    return render_template_string(login_page, message=message)

if __name__ == '__main__':
    app.run()