class ExpenseTracker:
    def __init__(self):
        self.budget = {}  # Stores budgets by category
        self.expenses = []  # Stores individual expenses
        self.approved_expenses = []  # Stores approved expenses

    def set_budget(self, category, amount):
        self.budget[category] = amount

    def add_expense(self, category, amount, description):
        if category not in self.budget:
            print(f"Error: No budget set for {category}.")
            return
        expense = {
            'category': category,
            'amount': amount,
            'description': description,
            'status': 'Pending'
        }
        self.expenses.append(expense)

    def approve_expense(self, expense_index):
        if 0 <= expense_index < len(self.expenses):
            expense = self.expenses[expense_index]
            if expense['status'] == 'Pending':
                # Check if the expense exceeds the budget
                if expense['amount'] <= self.budget[expense['category']]:
                    expense['status'] = 'Approved'
                    self.approved_expenses.append(expense)
                    print(f"Expense approved: {expense}")
                else:
                    print("Error: Expense exceeds budget.")
            else:
                print("Error: Expense already approved.")
        else:
            print("Error: Invalid expense index.")

    def disapprove_expense(self, expense_index):
        if 0 <= expense_index < len(self.expenses):
            expense = self.expenses[expense_index]
            if expense['status'] == 'Pending':
                expense['status'] = 'Disapproved'
                print(f"Expense disapproved: {expense}")
            else:
                print("Error: Expense cannot be disapproved (already approved or disapproved).")
        else:
            print("Error: Invalid expense index.")

    def get_expenses(self):
        return self.expenses

    def get_approved_expenses(self):
        return self.approved_expenses

    def get_budget(self):
        return self.budget


# Just for the command line interface
def CLI():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker CLI")
        print("1. Set Budget")
        print("2. Add Expense")
        print("3. Approve Expense")
        print("4. Disapprove Expense")
        print("5. View All Expenses")
        print("6. View Approved Expenses")
        print("7. View Budgets")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            category = input("Enter category: ")
            try:
                amount = float(input("Enter budget amount: "))
                tracker.set_budget(category, amount)
                print(f"Budget set for {category}: {amount}")
            except ValueError:
                print("Invalid amount. Please enter a number.")

        elif choice == "2":
            category = input("Enter category: ")
            try:
                amount = float(input("Enter expense amount: "))
                description = input("Enter description: ")
                tracker.add_expense(category, amount, description)
                print(f"Expense added for category {category}: {amount} - {description}")
            except ValueError:
                print("Invalid amount. Please enter a number.")

        elif choice == "3":
            try:
                expense_index = int(input("Enter expense index to approve: "))
                tracker.approve_expense(expense_index)
            except ValueError:
                print("Invalid index. Please enter a number.")

        elif choice == "4":
            try:
                expense_index = int(input("Enter expense index to disapprove: "))
                tracker.disapprove_expense(expense_index)
            except ValueError:
                print("Invalid index. Please enter a number.")

        elif choice == "5":
            expenses = tracker.get_expenses()
            if expenses:
                print("\nAll Expenses:")
                for idx, expense in enumerate(expenses):
                    print(f"Index {idx}: {expense}")
            else:
                print("No expenses recorded.")

        elif choice == "6":
            approved_expenses = tracker.get_approved_expenses()
            if approved_expenses:
                print("\nApproved Expenses:")
                for expense in approved_expenses:
                    print(expense)
            else:
                print("No approved expenses.")

        elif choice == "7":
            budget = tracker.get_budget()
            if budget:
                print("\nBudgets:")
                for category, amount in budget.items():
                    print(f"{category}: {amount}")
            else:
                print("No budgets set.")

        elif choice == "8":
            print("Exiting Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    CLI()



