#expenses tracker
from datetime import datetime 
def add_expense(expenses):
    while True:
        try:
            amount=float(input("enter a amount="))
            if amount<=0:
                print("amount should be greater than zero")
                continue
            else:
                print("valid amount")
            break
        except ValueError:
            print("input should be valid number.")
    while True:
        category=input("enter a category=").strip()
        if category:
            break
        print("category cannot be empty")
        
    while True:
        date=input("enter a date (yyyy-mm-dd)=")
        try:
            datetime.strptime(date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date. Use YYYY-MM-DD.")
    expense={
        "amount":amount,
        "category":category,
        "date":date
        }
    expenses.append(expense)
    print("expenses added successfully")

def view_expenses(expenses):
    if len(expenses) == 0:
        print("No expenses recorded yet.")
    else:
        print("\n===== All Expenses =====")

        for expense in expenses:
            print("Amount:", expense["amount"])
            print("Category:", expense["category"])
            print("Date:", expense["date"])
            print("-------------------")

def show_total(expenses):
    if len(expenses)==0:
        print(" no expenses recorded yet.")
        return
    total=0
    for expense in expenses:
        total+=expense["amount"]
    print(f"Total spending: ₹{total:.2f}")



        
def main():
    expenses = []

    while True:
        print("\n===== Personal Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total Spending")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            show_total(expenses)

        elif choice == "4":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()

    
        
            
               
               

    
        
            
    
    
    
    
