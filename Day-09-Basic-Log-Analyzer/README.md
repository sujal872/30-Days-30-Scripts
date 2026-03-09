# 🔍 Python Log Analyzer

A simple **Cybersecurity Log Analyzer** built with Python that scans log files and detects suspicious login activity such as repeated failed login attempts.

This project simulates how **SOC (Security Operations Center) analysts** monitor system logs to detect possible attacks like **brute force login attempts**.

This project is part of my **#30Days30Scripts Python Challenge**.
---

# 📌 Features

* 📂 Reads log files automatically
* 🔎 Detects **failed login attempts**
* 🌐 Identifies **suspicious IP addresses**
* ⚠ Alerts for **possible brute force attacks**
* 📊 Generates a simple **security report**

---

# 🛠 Technologies Used

* Python
* File Handling
* Collections Module
* Basic Cybersecurity Concepts

---

# 📁 Project Structure

```
log-analyzer
│
├── log_analyzer.py     # Main Python script
├── server.log          # Sample log file
└── README.md           # Project documentation
```

---

# 📄 Sample Log File

Example of `server.log`:

```
192.168.1.10 - Failed login
192.168.1.11 - Successful login
192.168.1.10 - Failed login
192.168.1.12 - Successful login
192.168.1.10 - Failed login
192.168.1.13 - Failed login
192.168.1.13 - Failed login
```

---

# ▶ How to Run

1️⃣ Clone the repository

```
git clone https://github.com/sujal872/30-Days-30-Scripts.git
```

2️⃣ Go to project folder

```
cd log-analyzer
```

3️⃣ Run the script

```
python log_analyzer.py
```

---

# 📊 Example Output

```
===== Log Analysis Report =====

IP Address: 192.168.1.10
Failed Attempts: 3
Possible Brute Force Attack
---------------------------

IP Address: 192.168.1.13
Failed Attempts: 2
---------------------------
```

---

# 🎯 Learning Objectives

This project helps understand:

* How **log files work**
* How **security monitoring systems detect attacks**
* Basic **log analysis automation using Python**

---

# 🚀 Future Improvements

* Detect suspicious IP automatically
* Export report to **CSV or JSON**
* Add **real-time log monitoring**
* Build a **GUI dashboard**

---

# 👨‍💻 Author

**Sujal Karnwal**

---

⭐ If you like this project, consider giving it a **star on GitHub**.
