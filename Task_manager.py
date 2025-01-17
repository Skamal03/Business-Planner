from datetime import datetime
from tkinter import messagebox

class TaskNode:
    def __init__(self, task_id, description, priority, deadline, status="pending"):
        self.task_id = task_id
        self.description = description
        self.priority = priority
        self.deadline = deadline
        self.status = status
        self.next = None

class TaskManager:
    def __init__(self):
        self.head = None
        self.id = 0

    def add_task(self, description, priority, deadline):
        try:
            task_id = self.id
            self.id += 1

            deadline = datetime.strptime(deadline, "%Y-%m-%d %H:%M")
            new_task = TaskNode(task_id, description, priority, deadline)

            # Traverse and sort tasks by priority
            if not self.head or priority < self.head.priority:
                new_task.next = self.head
                self.head = new_task
            else:
                current = self.head
                while current.next and current.next.priority <= priority:
                    current = current.next
                new_task.next = current.next
                current.next = new_task

            messagebox.showinfo("Success", "Task added successfully")
            return task_id

        except:
            messagebox.showerror("Error", "Enter the correct date and time format (%Y-%m-%d %H:%M)")

    def remove_task(self, task_id):
        if not self.head:
            return False

        if self.head.task_id == task_id:
            self.head = self.head.next
            return True

        current = self.head
        while current.next and current.next.task_id != task_id:
            current = current.next

        if current.next and current.next.task_id == task_id:
            current.next = current.next.next
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
            # Checking current node's deadline
            if current.deadline < current_time:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                current = current.next
            else:
                previous = current
                current = current.next

    def mark_task_as_done(self, task_id):
        current = self.head
        while current:
            if current.task_id == task_id:
                current.status = "done"
                messagebox.showinfo("Success", f"Task {task_id} marked as done")
                return True
            current = current.next
        messagebox.showerror("Error", f"Task {task_id} not found")
        return False

    def mark_task_as_pending(self, task_id):
        current = self.head
        while current:
            if current.task_id == task_id:
                current.status = "pending"  # Update status to "pending"
                messagebox.showinfo("Success", f"Task {task_id} marked as pending")
                return True
            current = current.next
        messagebox.showerror("Error", f"Task {task_id} not found")
        return False
