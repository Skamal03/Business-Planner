import csv

class BudgetManager:
    def __init__(self, filename="budgets.csv"):
        self.filename = filename
        self.budgets = {}
        self.load_budgets()

    def load_budgets(self):
        try:
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:
                        name = row[0]
                        amount = float(row[1])
                        category = row[2]
                        description = row[3]
                        status = row[4]
                        self.budgets[name] = {"category": category, "amount": amount,
                                              "description": description, "status": status}
        except FileNotFoundError:
            pass

    def save_budgets(self):
        try:
            with open(self.filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                for name, details in self.budgets.items():
                    writer.writerow([name, details["amount"], details["category"], details["description"], details["status"]])
        except Exception as e:
            print(f"Error saving budgets: {e}")

    def add_budget(self, name, amount, category, description):
        self.budgets[name] = {"category": category, "amount": amount,
                              "description": description, "status": "Pending"}
        self.save_budgets()
        print(f"Budget for {name} added successfully!")

    def view_budgets(self):
        if not self.budgets:
            print("No budgets available.")
            return False

        budget_list = []
        for name, details in self.budgets.items():
            status = details["status"]
            budget_details = (name, details['amount'], details['category'], details['description'], status)
            budget_list.append(budget_details)

        return budget_list

    def approve_budget(self, name):
        if name in self.budgets:
            self.budgets[name]["status"] = "Approved"
            self.save_budgets()
            print(f"Budget for {name} approved.")
        else:
            print(f"No budget found with name {name}.")

    def disapprove_budget(self, name):
        if name in self.budgets:
            self.budgets[name]["status"] = "Disapproved"
            self.save_budgets()
            print(f"Budget for {name} has been marked as disapproved.")
        else:
            print(f"No budget found with name {name}.")
