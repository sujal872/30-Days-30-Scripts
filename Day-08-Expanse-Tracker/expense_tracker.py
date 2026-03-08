import csv
from datetime import datetime

FILE_NAME = "Expenses.csv"


# ---------------- Add Expense ----------------
def add_Expense():

    cat_list = ['Food','Bills','Travel','Shopping']
    print("Categories:", cat_list)

    category = input("Category : ")
    item = input("Item : ")

    try:
        expense = float(input("Expense : "))
    except:
        print("Invalid amount")
        return

    date = datetime.now().strftime("%Y-%m-%d")

    row = [date, category, item, expense]

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(row)

    print("✅ Expense Added")


# ---------------- View Expense ----------------
def view_Expense():

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            print("\n+------------+-----------+-----------+-----------+")
            print("| Date       | Category  | Item      | Expense   |")
            print("+------------+-----------+-----------+-----------+")

            for row in reader:
                print(f"| {row[0]:<10} | {row[1]:<9} | {row[2]:<9} | {row[3]:<9} |")

            print("+------------+-----------+-----------+-----------+")

    except FileNotFoundError:
        print("No expenses found.")


# ---------------- Monthly Total ----------------
def monthly_Total():

    month_total = {}

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                date = row[0]
                expense = float(row[3])

                month = date[:7]   # YYYY-MM

                if month in month_total:
                    month_total[month] += expense
                else:
                    month_total[month] = expense

        print("\nMonthly Expense Summary")
        print("------------------------")

        for m, total in month_total.items():
            print(m, ":", total)

    except:
        print("No data found")


# ---------------- Category Wise ----------------
def category_wise_Total():

    cat_total = {}

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                category = row[1]
                expense = float(row[3])

                if category in cat_total:
                    cat_total[category] += expense
                else:
                    cat_total[category] = expense

        print("\nCategory Wise Expense")
        print("----------------------")

        for c, total in cat_total.items():
            print(c, ":", total)

    except:
        print("No data found")


# ---------------- Edit Expense ----------------
def edit_Expense():

    rows = []

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            rows = list(reader)

    except:
        print("No data to edit")
        return

    for i, r in enumerate(rows):
        print(i + 1, r)

    try:
        num = int(input("Select expense number to edit: ")) - 1
    except:
        print("Invalid")
        return

    if num < 0 or num >= len(rows):
        print("Invalid selection")
        return

    new_amount = input("New expense amount: ")

    rows[num][3] = new_amount

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print("✅ Expense Updated")


# ---------------- Main Menu ----------------
def main():

    while True:

        print('\n======= Simple Expense Tracker =======\n')
        print("1.Add Expense")
        print("2.View Expense")
        print("3.Monthly Total Expense")
        print("4.Category Wise Total Expense")
        print("5.Edit Expense")
        print("6.Exit")

        try:
            choice = int(input("Choose Option: "))
        except:
            print("❌ Invalid Input")
            continue

        if choice == 1:
            add_Expense()

        elif choice == 2:
            view_Expense()

        elif choice == 3:
            monthly_Total()

        elif choice == 4:
            category_wise_Total()

        elif choice == 5:
            edit_Expense()

        elif choice == 6:
            print("👋 Exiting...")
            break

        else:
            print("❌ Invalid Option")


if __name__ == '__main__':
    main()