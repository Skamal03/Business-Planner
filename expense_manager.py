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


# Example Usage
tracker = ExpenseTracker()
tracker.set_budget('Marketing', 5000)
tracker.set_budget('Development', 10000)

tracker.add_expense('Marketing', 1500, 'Social media ads')
tracker.add_expense('Development', 2000, 'Software tools')

# Approving the first expense
tracker.approve_expense(0)

# Disapproving the second expense
tracker.disapprove_expense(1)

# Displaying all expenses
print("All Expenses:", tracker.get_expenses())
