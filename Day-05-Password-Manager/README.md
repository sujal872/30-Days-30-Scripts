# 🔐 Day 5 – Password Manager (Basic)

A simple command-line Password Manager built in Python.

This project is part of the **30 Days – 30  Scripts of Python Challenge**.

---

## 🚀 Features

- Master Password authentication
- Save website credentials
- View stored passwords
- Password input masking
- Basic password encryption
- JSON file storage
- CLI Menu system

---

## 📂 Project Structure

Day-05-Password-Manager

1. password_manager.py  
2. passwords.json  
3. master.key  
4. README.md

---

## ⚙️ Requirements

Python 3.x

No external libraries required.

---

## ▶️ Run the Program

```bash
python password_manager.py

```
---
---
## 🔑 How it Works
1. Master Password

When the program runs for the first time, it will ask you to create a Master Password.

This password is stored as a SHA256 hash.

2. Encryption

Passwords are encoded using Base64 encoding before storing them in the JSON file.

Example stored data:
{
  "github.com": {
    "username": "user123",
    "password": "cGFzc3dvcmQxMjM="
  }
}

3. Menu Options

1. Add Password
2. View Passwords
3. Exit
---

---
⚠️ Disclaimer

This project uses basic encryption and is intended only for learning purposes.

Do NOT use it to store real sensitive passwords.

👨‍💻 Author

Sujal Karnwal


