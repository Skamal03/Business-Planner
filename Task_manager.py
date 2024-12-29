import tkinter as tk
from tkinter import messagebox
from datetime import datetime


# TaskNode class
class TaskNode:
    def __init__(self, task_id, description, priority, deadline):
        self.task_id = task_id
        self.description = description
        self.priority = priority
        self.deadline = deadline  # deadline should be a datetime object
        self.next = None


# TaskManager class
class TaskManager:
    def __init__(self):
        self.head = None
        self.task_counter = 0

    def add_task(self, description, priority, deadline):
        task_id = self.task_counter
        self.task_counter += 1

        # Assuming deadline is passed as string 'YYYY-MM-DD HH:MM'
        deadline_obj = datetime.strptime(deadline, "%Y-%m-%d %H:%M")
        new_task = TaskNode(task_id, description, priority, deadline_obj)

        if not self.head or priority < self.head.priority:
            new_task.next = self.head
            self.head = new_task
        else:
            current = self.head
            while current.next and current.next.priority <= priority:
                current = current.next
            new_task.next = current.next
            current.next = new_task
        return task_id

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
                current.deadline.strftime("%Y-%m-%d %H:%M")
            ))
            current = current.next
        return tasks

    def remove_past_tasks(self):
        current = self.head
        previous = None
        current_time = datetime.now()

        while current:
            if current.deadline < current_time:  # Task deadline has passed
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                current = current.next
            else:
                previous = current
                current = current.next

