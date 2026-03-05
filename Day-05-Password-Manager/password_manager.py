import json
import os
import base64
import getpass
import hashlib

FILE_NAME = "passwords.json"
MASTER_FILE = "master.key"


# -------------------------------
# Encryption / Decryption
# -------------------------------

def encrypt_password(password):
    encoded = base64.b64encode(password.encode())
    return encoded.decode()


def decrypt_password(password):
    decoded = base64.b64decode(password.encode())
    return decoded.decode()


# -------------------------------
# Master Password Setup
# -------------------------------

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def setup_master_password():

    if os.path.exists(MASTER_FILE):
        return

    print("🔐 Set Master Password")

    master = getpass.getpass("Enter Master Password: ")
    confirm = getpass.getpass("Confirm Master Password: ")

    if master != confirm:
        print("❌ Passwords do not match")
        exit()

    with open(MASTER_FILE, "w") as file:
        file.write(hash_password(master))

    print("✅ Master password set successfully\n")


def verify_master_password():

    with open(MASTER_FILE, "r") as file:
        stored = file.read()

    master = getpass.getpass("Enter Master Password: ")

    if hash_password(master) == stored:
        print("✅ Access Granted\n")
    else:
        print("❌ Wrong Master Password")
        exit()


# -------------------------------
# Load / Save Passwords
# -------------------------------

def load_passwords():

    if not os.path.exists(FILE_NAME):
        return {}

    with open(FILE_NAME, "r") as file:
        try:
            return json.load(file)
        except:
            return {}


def save_passwords(data):

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


# -------------------------------
# Add Credential
# -------------------------------

def add_password(data):

    print("\n➕ Add New Password")

    website = input("Website: ").lower()
    username = input("Username: ")

    password = getpass.getpass("Password: ")

    encrypted = encrypt_password(password)

    data[website] = {
        "username": username,
        "password": encrypted
    }

    save_passwords(data)

    print("✅ Password Saved\n")


# -------------------------------
# View Passwords
# -------------------------------

def view_passwords(data):

    print("\n🔎 Stored Passwords\n")

    if not data:
        print("No passwords saved\n")
        return

    for site, info in data.items():

        decrypted = decrypt_password(info["password"])

        print(f"Website : {site}")
        print(f"Username: {info['username']}")
        print(f"Password: {decrypted}")
        print("-" * 30)


# -------------------------------
# Menu System
# -------------------------------

def main():

    setup_master_password()
    verify_master_password()

    data = load_passwords()

    while True:

        print("====== Password Manager ======")
        print("1. Add Password")
        print("2. View Passwords")
        print("3. Exit")

        try:
            choice = int(input("Choose Option: "))
        except:
            print("❌ Invalid Input\n")
            continue

        if choice == 1:
            add_password(data)

        elif choice == 2:
            view_passwords(data)

        elif choice == 3:
            print("👋 Exiting...")
            break

        else:
            print("❌ Invalid Choice\n")


if __name__ == "__main__":
    main()