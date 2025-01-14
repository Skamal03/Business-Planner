class BudgetManager:
    def __init__(self):
        self.budgets = {}

    def add_budget(self, name, amount, category, description):
                                                                        
        self.budgets[name] = {'category': category,'amount': amount,
            'description' : description,'approved': False}
        
        print(f"Budget for {name} added successfully!")

    def view_budgets(self):
        if not self.budgets:
            print("No budgets available.")
            return

        for name, details in self.budgets.items():

            if details['approved']:
                status = "Approved"
            else:
                status = "Pending"


            amount = details['amount']
            category = details['category']
            description = details['description']


            print(f"Budget Name: {name}")
            print(f"Amount: Rs {amount}")
            print(f"Category: {category}")
            print(f"Description: {description}")
            print(f"Status: {status}")
            print("-" * 30)  


    def approve_budget(self, name):
        if name in self.budgets:
            self.budgets[name]['approved'] = True
            print(f"Budget for {name} approved.")
        else:
            print(f"No budget found with name {name}.")

    def disapprove_budget(self, name):
        if name in self.budgets:
            self.budgets[name]['approved'] = False
            print(f"Budget for {name} disapproved.")
        else:
            print(f"No budget found with name {name}.")



def command_line():
    budget_manager = BudgetManager()

    while True:
        print("\nBudget Manager CLI")
        print("1. Add Budget")
        print("2. View Budgets")
        print("3. Approve Budget")
        print("4. Disapprove Budget")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":  # Add Budget
            name = input("Enter budget name: ").strip()
            try:
                amount = float(input("Enter budget amount (e.g., 5000): "))
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
                continue

            category = input("Enter budget category (e.g., Marketing, HR): ").strip()
            description = input("Enter a brief description: ").strip()

            budget_manager.add_budget(name, amount, category, description)

        elif choice == "2":
            budget_manager.view_budgets()

        elif choice == "3":
            name = input("Enter the budget name to approve: ").strip()
            budget_manager.approve_budget(name)

        elif choice == "4":
            name = input("Enter the budget name to disapprove: ").strip()
            budget_manager.disapprove_budget(name)

        elif choice == "5":
            print("Exiting Budget Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    command_line()






