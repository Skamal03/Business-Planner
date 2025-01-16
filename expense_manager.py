
class BudgetManager:
    def __init__(self):
        self.budgets = {}

    def add_budget(self, name, amount, category, description):

        self.budgets[name] = {"category": category,"amount": amount,
            "description":description,"status": False}

        print(f"Budget for {name} added successfully!")

    def view_budgets(self):
        if not self.budgets:
            print("No budgets available.")
            return False

        budget_list = []
        for name, details in self.budgets.items():
            if details["status"] == "Approved":
                status = "Approved"
            elif details["status"] == "Disapproved":
                status="Disapproved"
            else:
                status="Pending"

            budget_details = (name,  details['amount'],details['category'],  details['description'], status )
            budget_list.append(budget_details)

        return budget_list

    def approve_budget(self, name):
        if name in self.budgets:
            self.budgets[name]["status"] = "Approved"
            print(f"Budget for {name} approved.")
        else:
            print(f"No budget found with name {name}.")

    def disapprove_budget(self, name):
        if name in self.budgets:
            self.budgets[name]["status"] = "Disapproved"
            print(f"Budget for {name} has been marked as disapproved.")
        else:
            print(f"No budget found with name {name}.")
