class Node:
    def __init__(self, personal_info, contact_info, job_details):
        self.personal_info = personal_info
        self.contact_info = contact_info
        self.job_details = job_details
        self.next = None

class EmployeeDatabase:
    def __init__(self):
        self.head = None
        self.employee_id_counter = 1

    def generate_employee_id(self):
        return f"EMP{str(self.employee_id_counter).zfill(3)}"

    def add_employee(self, personal_info, contact_info, job_details):
        employee_id = self.generate_employee_id()
        personal_info['employee_id'] = employee_id
        new_node = Node(personal_info, contact_info, job_details)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.employee_id_counter += 1
        print(f"Employee {personal_info['fullname']} added successfully with ID {employee_id}!")

    def display_employees(self):
        if self.head is None:
            print("No employees in the database.")
            return []
        employees = []
        current = self.head
        while current:
            employee_data = [current.personal_info.get("employee_id"),current.personal_info.get("fullname"),
                            current.job_details.get("department"),current.job_details.get("salary"),
                            current.job_details.get("hours_per_week"),]
            employees.append(employee_data)
            current = current.next
        return employees

    def search_employee(self, employee_id):
        current = self.head
        while current:
            if current.personal_info["employee_id"] == employee_id:
                employee_data = {**current.personal_info,**current.contact_info,**current.job_details,}
                return employee_data
            current = current.next
        return None

    def remove_employee(self, employee_id):
        current = self.head
        prev = None
        try:
            while current:
                if current.personal_info['employee_id'] == employee_id:
                    if prev is None:
                        self.head = current.next
                    else:
                        prev.next = current.next
                    print(f"Employee with ID {employee_id} removed successfully.")
                    return True
                prev = current
                current = current.next
            print(f"Employee with ID {employee_id} not found.")
            return False
        except Exception as e:
            print(f"Error occurred while removing employee: {e}")
            return False

