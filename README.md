🔐 Web Security Lab – SQL Injection & Hardening (Flask)
🚀 Project Overview

This project demonstrates the identification, exploitation, and mitigation of a SQL Injection vulnerability in a Flask web application.

It contains:

🔴 A deliberately vulnerable version

🟢 A hardened secure version

📄 Professional vulnerability & hardening documentation

📸 Visual proof of exploitation and mitigation

This project was developed for educational and portfolio purposes to demonstrate secure coding practices and web security concepts.

🧱 Project Structure
web-security-hardening/
│
├── vulnerable_app/          # Intentionally vulnerable Flask app
│   └── app.py
│
├── hardened_app/            # Secure version with mitigations
│   └── app.py
│
├── docs/
│   ├── vulnerability_report.md
│   ├── hardening_report.md
│   └── screenshots/
│
└── README.md
🔴 Vulnerable Application
Identified Vulnerabilities

SQL Injection (string concatenation in SQL queries)

Hardcoded credentials

Debug mode enabled

No input validation

Plaintext password storage

SQL Injection Demonstration
Injection Payload Used:
Username: ' OR 1=1 --
Password: anything
Result:

✅ Login successful without valid credentials

The injected query becomes:

SELECT * FROM users 
WHERE username = '' OR 1=1 --' 
AND password = 'anything'

Because 1=1 is always TRUE, authentication is bypassed.

🟢 Hardened Application
Security Improvements Applied

Parameterized queries (prepared statements)

Password hashing with bcrypt

Debug mode disabled

Input validation

Removal of hardcoded credentials

Basic access control

Same Injection Attempt
Username: ' OR 1=1 --
Password: anything
Result:

❌ Login failed

Why?

The query uses parameterized statements (?)

User input is treated as literal text

SQL logic is not altered

Password verification uses bcrypt

The injection is safely neutralized.

📸 Visual Demonstration
🔴 Vulnerable – Authentication Bypass

→ Login successful using SQL Injection.

🟢 Hardened – Injection Blocked

→ Same payload rejected.

🎮 How to Run
Install dependencies
python -m pip install flask bcrypt
Run Vulnerable Version
cd vulnerable_app
python app.py

Open:

http://127.0.0.1:5000
Run Hardened Version
cd hardened_app
python app.py

Open:

http://127.0.0.1:5000
📚 Skills Demonstrated

SQL Injection exploitation

Secure coding in Flask

Parameterized query implementation

Password hashing with bcrypt

Input validation techniques

Security documentation & risk assessment

Practical before/after mitigation demonstration

🎯 Learning Outcome

This project demonstrates:

How SQL Injection works

How authentication bypass occurs

How to properly mitigate SQL Injection

The importance of secure development practices

⚠️ Disclaimer

This project is for educational purposes only.
The vulnerable application is intentionally insecure and should never be used in production environments.