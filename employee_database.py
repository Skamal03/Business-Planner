class Node:
    def __init__(self, personal_info, contact_info, job_details):
        self.personal_info = personal_info
        self.contact_info = contact_info
        self.job_details = job_details
        self.next = None


class EmployeeDatabase:
    def __init__(self):
        self.head = None

    def add_employee(self, personal_info, contact_info, job_details):
        new_node = Node(personal_info, contact_info, job_details)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

        print(f"Employee {personal_info['name']} added successfully!")

    def display_employees(self):

        if self.head is None:
            print("No employees in the database.")
            return

        current = self.head
        while current:
            print("Personal Information:")
            for key, value in current.personal_info.items():
                print(f"{key}: {value}")
            print("Contact Information:")
            for key, value in current.contact_info.items():
                print(f"{key}: {value}")
            print("Job Details:")
            for key, value in current.job_details.items():
                print(f"{key}: {value}")
            print("-" * 50)
            current = current.next

    def search_employee(self, employee_id):

        current = self.head

        while current:
            if current.personal_info['employee_id'] == employee_id:
                print("Employee Found!")
                print("Personal Information:", current.personal_info)
                print("Contact Information:", current.contact_info)
                print("Job Details:", current.job_details)
                return
            current = current.next
        print(f"Employee with ID {employee_id} not found.")

    def remove_employee(self, employee_id):

        current = self.head
        prev = None

        while current:
            if current.personal_info['employee_id'] == employee_id:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                print(f"Employee with ID {employee_id} removed successfully.")
                return
            prev = current
            current = current.next

        print(f"Employee with ID {employee_id} not found.")


# command line
def command_line():
    database = EmployeeDatabase()

    while True:
        print("\nEmployee Database CLI")
        print("1. Add Employee")
        print("2. Display Employees")
        print("3. Search Employee")
        print("4. Remove Employee")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("Enter personal information:")
            employee_id = input("Employee ID: ").strip()
            name = input("Name: ").strip()
            age = input("Age: ").strip()

            print("Enter contact information:")
            email = input("Email: ").strip()
            phone = input("Phone: ").strip()

            print("Enter job details:")
            position = input("Position: ").strip()
            salary = input("Salary: ").strip()

            personal_info = {
                "employee_id": employee_id,
                "name": name,
                "age": age,
            }
            contact_info = {
                "email": email,
                "phone": phone,
            }
            job_details = {
                "position": position,
                "salary": salary,
            }

            database.add_employee(personal_info, contact_info, job_details)

        elif choice == "2":
            database.display_employees()

        elif choice == "3":
            employee_id = input("Enter the Employee ID to search: ").strip()
            database.search_employee(employee_id)

        elif choice == "4":
            employee_id = input("Enter the Employee ID to remove: ").strip()
            database.remove_employee(employee_id)

        elif choice == "5":
            print("Exiting Employee Database. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    command_line()
