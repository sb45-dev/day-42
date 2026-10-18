import csv
from datetime import datetime

FILE_NAME = "expenses.csv"

def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")

    category = input("Enter expense category: ")
    description = input("Enter expense description: ")
    amount = float(input("Enter expense amount: ₹"))

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])

    print("Expense added successfully!")

def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            print("\n--- Expense Records ---")
            total = 0

            for row in reader:
                if len(row) == 4:
                    print(
                        f"Date: {row[0]} | "
                        f"Category: {row[1]} | "
                        f"Description: {row[2]} | "
                        f"Amount: ₹{row[3]}"
                    )
                    total += float(row[3])

            print(f"\nTotal Expenses: ₹{total:.2f}")

    except FileNotFoundError:
        print("No expense records found.")

def category_summary():
    expenses = {}

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if len(row) == 4:
                    category = row[1]
                    amount = float(row[3])

                    expenses[category] = (
                        expenses.get(category, 0) + amount
                    )

        print("\n--- Category-wise Summary ---")

        if not expenses:
            print("No expenses available.")
        else:
            for category, amount in expenses.items():
                print(f"{category}: ₹{amount:.2f}")

    except FileNotFoundError:
        print("No expense records found.")

def set_budget():
    budget = float(input("Enter your monthly budget: ₹"))
    print(f"Monthly budget set to ₹{budget:.2f}")

    total = 0

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            current_month = datetime.now().strftime("%Y-%m")

            for row in reader:
                if len(row) == 4 and row[0].startswith(current_month):
                    total += float(row[3])

        print(f"Expenses this month: ₹{total:.2f}")
        print(f"Remaining budget: ₹{budget - total:.2f}")

        if total > budget:
            print("Warning! You have exceeded your budget.")

    except FileNotFoundError:
        print("No expenses recorded yet.")

def main():
    while True:
        print("\n===== PERSONAL EXPENSE & BUDGET TRACKER =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Category-wise Summary")
        print("4. Set Monthly Budget")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        try:
            if choice == "1":
                add_expense()
            elif choice == "2":
                view_expenses()
            elif choice == "3":
                category_summary()
            elif choice == "4":
                set_budget()
            elif choice == "5":
                print("Thank you for using Expense Tracker!")
                break
            else:
                print("Invalid choice. Please try again.")

        except ValueError:
            print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    main()