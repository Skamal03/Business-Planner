import random

class Node:
    def __init__(self, personal_info, contact_info, job_details):
        self.personal_info = personal_info
        self.contact_info = contact_info
        self.job_details = job_details
        self.next = None

class EmployeeDatabase:
    def __init__(self):
        self.head = None
        self.employee_id_counter = 1  # Counter for generating unique employee IDs

    def generate_employee_id(self):
        """Generate a unique employee ID."""
        return f"EMP{str(self.employee_id_counter).zfill(3)}"

    def add_employee(self, personal_info, contact_info, job_details):
        """Add a new employee to the database."""
        # Generate a unique employee ID
        employee_id = self.generate_employee_id()

        # Add the ID to the personal information dictionary
        personal_info['employee_id'] = employee_id

        # Create a new employee node
        new_node = Node(personal_info, contact_info, job_details)

        # If the list is empty, this will be the first employee
        if self.head is None:
            self.head = new_node
        else:
            # Otherwise, traverse the list to find the last node and add the new employee
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

        # Increment the employee ID counter for the next employee
        self.employee_id_counter += 1

        print(f"Employee {personal_info['fullname']} added successfully with ID {employee_id}!")

    def display_employees(self):
        """Display all employees in the database."""
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
        """Search for an employee by their ID."""
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
        """Remove an employee from the database."""
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
