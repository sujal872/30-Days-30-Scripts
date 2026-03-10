# Python Port Scanner Script 

## 📌 Description
This is a simple yet powerful Python Port Scanner built using the socket module.

This project is part of my **30 Days – 30 Scripts of Python Challenge**.

It allows:
- Scanning a single port
- Scanning a range of ports
- Resolving domain names to IP addresses
- Detecting running services on open ports
- Showing total open and closed ports

---

## 🚀 Features

✔ Domain to IP resolution  
✔ Single port scanning  
✔ Port range scanning  
✔ Service detection  
✔ Scan summary report  

---

## 🛠 Requirements

- Python 3.x

No external libraries required.

---

## ▶ Usage

Run the script : python port_scanner.py

Then enter:

1. Target IP or Domain
2. Choose scan type (Single or Range)
3. Enter port details

---

## 🧠 How It Works

- Uses `socket.gethostbyname()` for DNS resolution
- Uses `socket.connect_ex()` to test port connectivity
- Uses `socket.getservbyport()` to detect service name

---

## ⚠ Disclaimer

This tool is for educational purposes only.
Do not scan systems without proper authorization.

---

## 👨‍💻 Author

Sujal Karnwal

Cybersecurity Enthusiast | Python Learner  

---

⭐ If you like this project, consider giving it a star!