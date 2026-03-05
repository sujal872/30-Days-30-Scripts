import json
import re
import os

FILE_NAME = "contacts.json"

# Load contacts from JSON
def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}

# Save contacts to JSON
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


# Validation functions
def validate_phone(phone):
    return phone.isdigit() and len(phone) == 10


def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)


# Add Contact
def add_contact(contacts):
    print("\n📌 Add Contact")

    name = input("Enter Name: ").strip().lower()

    if name in contacts:
        print("❌ Contact already exists!")
        return

    phone = input("Enter Phone Number: ")
    if not validate_phone(phone):
        print("❌ Invalid phone number (must be 10 digits)")
        return

    email = input("Enter Email: ")
    if not validate_email(email):
        print("❌ Invalid email format")
        return

    contacts[name] = {
        "phone": phone,
        "email": email
    }

    save_contacts(contacts)

    print("✅ Contact Added Successfully")


# Search Contact
def search_contact(contacts):
    print("\n🔎 Search Contact")

    name = input("Enter Name: ").strip().lower()

    if name in contacts:
        print("Name :", name.title())
        print("Phone :", contacts[name]["phone"])
        print("Email :", contacts[name]["email"])
    else:
        print("❌ Contact not found")


# Update Contact
def update_contact(contacts):
    print("\n✏️ Update Contact")

    name = input("Enter Name: ").strip().lower()

    if name not in contacts:
        print("❌ Contact not found")
        return

    phone = input("Enter New Phone Number: ")

    if not validate_phone(phone):
        print("❌ Invalid phone number")
        return

    email = input("Enter New Email: ")

    if not validate_email(email):
        print("❌ Invalid email format")
        return

    contacts[name]["phone"] = phone
    contacts[name]["email"] = email

    save_contacts(contacts)

    print("✅ Contact Updated Successfully")


# Delete Contact
def delete_contact(contacts):
    print("\n🗑 Delete Contact")

    name = input("Enter Name: ").strip().lower()

    if name in contacts:
        contacts.pop(name)
        save_contacts(contacts)
        print("✅ Contact Deleted")
    else:
        print("❌ Contact not found")


# Show All Contacts
def show_contacts(contacts):
    print("\n📒 All Contacts")

    if not contacts:
        print("No contacts found.")
        return

    for name, info in contacts.items():
        print("-----------------------")
        print("Name :", name.title())
        print("Phone:", info["phone"])
        print("Email:", info["email"])


# Main Menu
def main():

    contacts = load_contacts()

    while True:

        print("\n====== Contact Book ======")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Show All Contacts")
        print("6. Exit")

        choice = input("Choose Option: ")

        if choice == "1":
            add_contact(contacts)

        elif choice == "2":
            search_contact(contacts)

        elif choice == "3":
            update_contact(contacts)

        elif choice == "4":
            delete_contact(contacts)

        elif choice == "5":
            show_contacts(contacts)

        elif choice == "6":
            print("👋 Exiting Program...")
            break

        else:
            print("❌ Invalid Choice")


if __name__ == "__main__":
    main()