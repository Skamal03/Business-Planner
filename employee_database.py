import csv

class Node:
    def __init__(self, personal_info, contact_info, job_details):
        self.personal_info = personal_info
        self.contact_info = contact_info
        self.job_details = job_details
        self.next = None

class EmployeeDatabase:
    def __init__(self, filename="employees.csv"):
        self.filename = filename
        self.head = None
        self.employee_id_counter = 1
        self.load_employees()

    def load_employees(self):
        try:
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:
                        employee_id = row[0]
                        fullname = row[1]
                        fathername = row[2]
                        gender = row[3]
                        marital_status = row[4]
                        phone = row[5]
                        email = row[6]
                        address = row[7]
                        department = row[8]
                        position = row[9]
                        hours_per_week = int(row[10])
                        salary = float(row[11])

                        personal_info = {
                            "employee_id": employee_id, "fullname": fullname,
                            "fathername": fathername,
                            "gender": gender, "marital_status": marital_status
                        }
                        contact_info = {"phone": phone, "email": email, "address": address}
                        job_details = {"department": department, "position": position, "hours_per_week": hours_per_week, "salary": salary}

                        self.add_employee_from_csv(personal_info, contact_info, job_details)


                        self.employee_id_counter = max(self.employee_id_counter, int(employee_id[3:]) + 1)
        except FileNotFoundError:
            pass

    def save_employees(self):
        try:
            with open(self.filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                current = self.head
                while current:
                    writer.writerow([current.personal_info["employee_id"], current.personal_info["fullname"],
                                     current.personal_info["fathername"], current.personal_info["gender"],
                                     current.personal_info["marital_status"], current.contact_info["phone"],
                                     current.contact_info["email"], current.contact_info["address"],
                                     current.job_details["department"], current.job_details["position"],
                                     current.job_details["hours_per_week"], current.job_details["salary"]])
                    current = current.next
        except Exception as e:
            print(f"Error saving employees: {e}")

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
        self.save_employees()
        print(f"Employee {personal_info['fullname']} added successfully with ID {employee_id}!")

    def add_employee_from_csv(self, personal_info, contact_info, job_details):
        new_node = Node(personal_info, contact_info, job_details)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display_employees(self):
        if self.head is None:
            print("No employees in the database.")
            return []
        employees = []
        current = self.head
        while current:
            employee_data = [current.personal_info.get("employee_id"), current.personal_info.get("fullname"),
                             current.job_details.get("department"),
                             current.job_details.get("salary"),
                             current.job_details.get("hours_per_week")]
            employees.append(employee_data)
            current = current.next
        return employees

    def search_employee(self, employee_id):
        current = self.head
        while current:
            if current.personal_info["employee_id"] == employee_id:
                employee_data = {**current.personal_info, **current.contact_info, **current.job_details}
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
                    self.save_employees()  # Save employees after removal
                    print(f"Employee with ID {employee_id} removed successfully.")
                    return True
                prev = current
                current = current.next
            print(f"Employee with ID {employee_id} not found.")
            return False
        except Exception as e:
            print(f"Error occurred while removing employee: {e}")
            return False
