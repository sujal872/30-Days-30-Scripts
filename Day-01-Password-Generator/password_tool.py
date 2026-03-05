import random
import string


# ---------------- PASSWORD STRENGTH CHECKER ---------------- #

def check_password_strength(password):
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in string.punctuation:
            has_special = True

    if len(password) < 8:
        return "Weak ❌ (Too Short)"

    score = sum([has_upper, has_lower, has_digit, has_special])

    if score == 4 and len(password) >= 12:
        return "Very Strong 🔥"
    elif score >= 3:
        return "Strong ✅"
    else:
        return "Medium ⚠"


# ---------------- PASSWORD GENERATOR ---------------- #

def generate_passwords():
    print("\n--- PASSWORD GENERATOR ---")

    length = int(input("Enter password length (8 - 16): "))
    if length < 8 or length > 16:
        print("Length must be between 8 and 16.")
        return

    name_part = input("Enter your name or word: ")
    number_part = input("Enter numbers you like: ")
    special_part = input("Enter special characters you like: ")

    base_string = name_part + number_part + special_part

    if not base_string:
        print("You must enter at least one character.")
        return

    print("\nGenerated Passwords:\n")

    for i in range(4):
        random_part = ''.join(random.choices(
            string.ascii_letters + string.digits + string.punctuation,
            k=length - len(base_string)
        ))

        password_list = list(base_string + random_part)
        random.shuffle(password_list)
        final_password = ''.join(password_list)

        print(f"{i+1}. {final_password}")


# ---------------- MAIN MENU ---------------- #

def main():
    while True:
        print("\n====== PASSWORD TOOL ======")
        print("1. Password Strength Checker")
        print("2. Password Generator")
        print("3. Exit")

        choice = input("Choose option (1-3): ")

        if choice == "1":
            pwd = input("Enter password to check: ")
            result = check_password_strength(pwd)
            print("Result:", result)

        elif choice == "2":
            generate_passwords()

        elif choice == "3":
            print("Exiting program...")
            break

        else:
            print("Invalid choice ❌")


# Run Program
main()