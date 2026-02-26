SSH/Web Security Portfolio – Web Vulnerable + Hardening

🚀 Description

A web security project demonstrating how to identify and mitigate vulnerabilities in a Flask application.

The project includes:

A vulnerable app to demonstrate real attacks (SQL Injection, debug mode, hardcoded credentials, etc.)

A hardened secure version with all mitigations applied

Professional documentation of vulnerabilities and hardening

Screenshots and visual evidence of before/after

🧱 Project Structure
web-security-hardening/
│
├── vulnerable_app/          # Insecure app
│   └── app.py
│
├── hardened_app/            # Secure app
│   └── app.py
│
├── docs/                    # Documentation
│   ├── vulnerability_report.md
│   └── hardening_report.md
│
└── README.md                # This file

⚠️ Identified Vulnerabilities

The vulnerable app included:

SQL Injection

Hardcoded credentials

Debug mode enabled

No input validation

Plaintext passwords

Documented in docs/vulnerability_report.md.

🛡️ Hardening / Improvements Applied

The hardened version implements:

Parameterized queries (SQLi mitigated)

Removed hardcoded credentials

Debug mode disabled

Input validation and sanitization

Passwords hashed with bcrypt

Basic access control

Documented in docs/hardening_report.md.

🎮 How to Use

Install dependencies:

python -m pip install flask bcrypt

Run the vulnerable app:

cd vulnerable_app
python app.py

Open your browser:

http://127.0.0.1:5000

To test the hardened version:

cd hardened_app
python app.py
📸 Visual Example

Before / After: Vulnerable vs Hardened App

← replace with real screenshot or GIF of the project

📚 Learning & Skills

- Web vulnerability detection and exploitation
- SQL Injection and mitigation
- Security best practices in Flask
- Professional documentation (vulnerability + hardening reports)
- Portfolio-ready technical project