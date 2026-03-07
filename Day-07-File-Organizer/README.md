# 📂 Python File Organizer

A simple yet powerful **Python automation project** that organizes files in a directory automatically.

This project contains **two file organizer scripts**:

* **Basic File Organizer** → Sorts files into folders based on specific extensions
* **Smart File Organizer** → Automatically detects file extensions and creates folders dynamically

This helps keep folders like **Downloads, Desktop, or Projects clean and organized.**

This project is part of my **#30Days30Scripts Python Challenge**.
---

# 🚀 Features

## Basic File Organizer

* Organizes files by predefined extensions
* Automatically creates folders if they do not exist
* Moves files to their respective folders
* Beginner-friendly Python project

Supported file types:

* `.txt`
* `.pdf`
* `.zip`
* `.html`
* `.cpp`

---

## Smart File Organizer

* Automatically detects file extensions
* Dynamically creates folders for each file type
* Supports **any file extension**
* Moves files into categorized folders automatically

Example:

```
file.txt  → TXT_FILES/
image.png → PNG_FILES/
video.mp4 → MP4_FILES/
code.py   → PY_FILES/
```

---

# 📁 Project Structure

```
python-file-organizer/

file_org.py
smart_file_org.py
README.md
```

---

# 📸 Example

### Before Running

```
project/

file1.txt
file2.pdf
file3.zip
index.html
program.cpp
image.png
video.mp4
```

---

### After Running (Smart Organizer)

```
project/

TXT_FILES/
file1.txt

PDF_FILES/
file2.pdf

ZIP_FILES/
file3.zip

HTML_FILES/
index.html

CPP_FILES/
program.cpp

PNG_FILES/
image.png

MP4_FILES/
video.mp4
```

---

# 🛠 Requirements

* Python **3.x**
* No external libraries required

Modules used:

* `os`
* `shutil`

---

# ▶️ How to Run

### Run Basic Organizer

```
python file_org.py
```

This script sorts files based on **predefined extensions**.

---

### Run Smart Organizer

```
python smart_file_org.py
```

This script automatically detects **any file extension** and organizes files accordingly.

---

# 📚 Concepts Used

* Python Automation
* File Handling
* Directory Traversal (`os.walk`)
* File Extensions
* Functions
* Conditional Statements

---

# 💡 Future Improvements

* Add CLI commands
* Add duplicate file detection
* Add large file cleaner
* Add GUI version
* AI based file categorization

---

# 👨‍💻 Author

**Sujal Karnwal**

---

⭐ If you found this project useful, consider giving it a **star on GitHub**.
