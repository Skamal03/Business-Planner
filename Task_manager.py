import csv
from datetime import datetime
from tkinter import messagebox

class TaskNode:
    def __init__(self, task_id, description, priority, deadline, status="pending"):
        self.task_id=task_id
        self.description=description
        self.priority=priority
        self.deadline=deadline
        self.status=status
        self.next=None

class TaskManager:
    def __init__(self, filename="tasks.csv"):
        self.head=None
        self.filename=filename
        self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:
                        task_id=int(row[0])
                        description=row[1]
                        priority=int(row[2])
                        deadline=datetime.strptime(row[3], "%Y-%m-%d %H:%M")
                        status = row[4]
                        self.add_task_from_csv(task_id, description, priority, deadline, status)
        except FileNotFoundError:
            pass

    def save_tasks(self):
        try:
            with open(self.filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                current = self.head
                while current:
                    writer.writerow([current.task_id, current.description, current.priority, current.deadline.strftime("%Y-%m-%d %H:%M"), current.status])
                    current = current.next
        except Exception as e:
            messagebox.showerror("Error", f"Could not save tasks to CSV: {e}")

    def add_task(self, description, priority, deadline):
        try:
            task_id = self.generate_task_id()
            deadline = datetime.strptime(deadline, "%Y-%m-%d %H:%M")
            new_task = TaskNode(task_id, description, priority, deadline)


            if not self.head or priority < self.head.priority:
                new_task.next = self.head
                self.head = new_task
            else:
                current = self.head
                while current.next and current.next.priority <= priority:
                    current = current.next
                new_task.next = current.next
                current.next = new_task

            self.save_tasks()
            messagebox.showinfo("Success", "Task added successfully")
            return task_id
        except Exception as e:
            messagebox.showerror("Error", f"Could not add task: {e}")

    def add_task_from_csv(self, task_id, description, priority, deadline, status):
        new_task = TaskNode(task_id, description, priority, deadline, status)

        if not self.head or priority < self.head.priority:
            new_task.next = self.head
            self.head = new_task
        else:
            current = self.head
            while current.next and current.next.priority <= priority:
                current = current.next
            new_task.next = current.next
            current.next = new_task

    def generate_task_id(self):
        if not self.head:
            return 1
        return self.head.task_id + 1

    def remove_task(self, task_id):
        if not self.head:
            return False

        if self.head.task_id == task_id:
            self.head = self.head.next
            self.save_tasks()
            return True

        current = self.head
        while current.next and current.next.task_id != task_id:
            current = current.next

        if current.next and current.next.task_id == task_id:
            current.next = current.next.next
            self.save_tasks()
            return True

        return False

    def view_tasks(self):
        tasks = []
        current = self.head
        while current:
            tasks.append((
                current.task_id,
                current.description,
                current.priority,
                current.deadline.strftime("%Y-%m-%d %H:%M"),
                current.status
            ))
            current = current.next
        return tasks

    def remove_past_tasks(self):
        current = self.head
        previous = None
        current_time = datetime.now()

        while current:

            if current.deadline < current_time:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                current = current.next
            else:
                previous = current
                current = current.next

        self.save_tasks()

    def mark_task_as_done(self, task_id):
        current = self.head
        while current:
            if current.task_id == task_id:
                current.status = "done"
                self.save_tasks()
                messagebox.showinfo("Success", f"Task {task_id} marked as done")
                return True
            current = current.next
        messagebox.showerror("Error", f"Task {task_id} not found")
        return False

    def mark_task_as_pending(self, task_id):
        current = self.head
        while current:
            if current.task_id == task_id:
                current.status = "pending"
                self.save_tasks()
                messagebox.showinfo("Success", f"Task {task_id} marked as pending")
                return True
            current = current.next
        messagebox.showerror("Error", f"Task {task_id} not found")
        return False
