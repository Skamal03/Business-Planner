import tkinter as tk
from tkinter import messagebox
from Task_manager import TaskManager
from event_scheduler import EventScheduler

class TaskManagerGUI:
    def __init__(self, root, task_manager):
        self.root = root
        self.task_manager = task_manager
        self.root.title("Task Manager")
        self.root.geometry("600x400")

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Add task frame
        self.add_task_frame = tk.Frame(self.root)
        self.add_task_frame.pack(pady=10)

        self.description_label = tk.Label(self.add_task_frame, text="Description:")
        self.description_label.grid(row=0, column=0)
        self.description_entry = tk.Entry(self.add_task_frame)
        self.description_entry.grid(row=0, column=1)

        self.priority_label = tk.Label(self.add_task_frame, text="Priority (lower is higher):")
        self.priority_label.grid(row=1, column=0)
        self.priority_entry = tk.Entry(self.add_task_frame)
        self.priority_entry.grid(row=1, column=1)

        self.deadline_label = tk.Label(self.add_task_frame, text="Deadline (YYYY-MM-DD HH:MM):")
        self.deadline_label.grid(row=2, column=0)
        self.deadline_entry = tk.Entry(self.add_task_frame)
        self.deadline_entry.grid(row=2, column=1)

        self.add_button = tk.Button(self.add_task_frame, text="Add Task", command=self.add_task)
        self.add_button.grid(row=3, column=0, columnspan=2)

        # Remove task frame
        self.remove_task_frame = tk.Frame(self.root)
        self.remove_task_frame.pack(pady=10)

        self.task_id_label = tk.Label(self.remove_task_frame, text="Task ID to remove:")
        self.task_id_label.grid(row=0, column=0)
        self.task_id_entry = tk.Entry(self.remove_task_frame)
        self.task_id_entry.grid(row=0, column=1)

        self.remove_button = tk.Button(self.remove_task_frame, text="Remove Task", command=self.remove_task)
        self.remove_button.grid(row=1, column=0, columnspan=2)

        # View tasks button
        self.view_button = tk.Button(self.root, text="View All Tasks", command=self.view_tasks)
        self.view_button.pack(pady=5)

        # Remove past tasks button
        self.remove_past_button = tk.Button(self.root, text="Remove Past Tasks", command=self.remove_past_tasks)
        self.remove_past_button.pack(pady=5)

        # Output display area
        self.output_text = tk.Text(self.root, height=10, width=70)
        self.output_text.pack(pady=10)

    def add_task(self):
        description = self.description_entry.get()
        priority = self.priority_entry.get()
        deadline = self.deadline_entry.get()

        if not description or not priority or not deadline:
            messagebox.showerror("Input Error", "All fields must be filled out!")
            return

        try:
            priority = int(priority)
        except ValueError:
            messagebox.showerror("Input Error", "Priority must be an integer!")
            return

        result = self.task_manager.add_task(description, priority, deadline)
        self.clear_entries()
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, f"Task added with ID {result}")

    def remove_task(self):
        task_id = self.task_id_entry.get()

        if not task_id:
            messagebox.showerror("Input Error", "Please enter a task ID to remove!")
            return

        try:
            task_id = int(task_id)
        except ValueError:
            messagebox.showerror("Input Error", "Task ID must be an integer!")
            return

        result = self.task_manager.remove_task(task_id)
        self.output_text.delete(1.0, tk.END)
        if result:
            self.output_text.insert(tk.END, f"Task {task_id} removed successfully.")
        else:
            self.output_text.insert(tk.END, f"Task {task_id} not found.")

    def view_tasks(self):
        tasks = self.task_manager.view_tasks()
        self.output_text.delete(1.0, tk.END)
        if not tasks:
            self.output_text.insert(tk.END, "No tasks to display.")
        else:
            for task in tasks:
                self.output_text.insert(tk.END, f"ID {task[0]}: {task[1]}, Priority: {task[2]}, Deadline: {task[3]}\n")

    def remove_past_tasks(self):
        self.task_manager.remove_past_tasks()
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, "Past tasks removed.")

    def clear_entries(self):
        self.description_entry.delete(0, tk.END)
        self.priority_entry.delete(0, tk.END)
        self.deadline_entry.delete(0, tk.END)
        self.task_id_entry.delete(0, tk.END)


# Main application
if __name__ == "__main__":
    root = tk.Tk()
    task_manager = TaskManager()
    gui = TaskManagerGUI(root, task_manager)
    root.mainloop()


class EventSchedulerGUI:
    def __init__(self, root, scheduler):
        self.root = root
        self.scheduler = scheduler
        self.root.title("Event Scheduler")
        self.root.geometry("500x400")

        # Adding components
        self.create_widgets()

    def create_widgets(self):
        # Add event frame
        self.add_event_frame = tk.Frame(self.root)
        self.add_event_frame.pack(pady=10)

        self.date_time_label = tk.Label(self.add_event_frame, text="Date and Time (YYYY-MM-DD HH:MM):")
        self.date_time_label.grid(row=0, column=0)
        self.date_time_entry = tk.Entry(self.add_event_frame)
        self.date_time_entry.grid(row=0, column=1)

        self.description_label = tk.Label(self.add_event_frame, text="Event Description:")
        self.description_label.grid(row=1, column=0)
        self.description_entry = tk.Entry(self.add_event_frame)
        self.description_entry.grid(row=1, column=1)

        self.add_button = tk.Button(self.add_event_frame, text="Add Event", command=self.add_event)
        self.add_button.grid(row=2, column=0, columnspan=2)

        # View events
        self.view_button = tk.Button(self.root, text="View All Events", command=self.view_events)
        self.view_button.pack(pady=5)

        # Remove past events
        self.remove_past_button = tk.Button(self.root, text="Remove Past Events", command=self.remove_past_events)
        self.remove_past_button.pack(pady=5)

        # Output display
        self.output_text = tk.Text(self.root, height=10, width=50)
        self.output_text.pack(pady=10)

    def add_event(self):
        date_time = self.date_time_entry.get()
        description = self.description_entry.get()
        result = self.scheduler.add_event(date_time, description)
        self.clear_entries()
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, result)

    def view_events(self):
        events = self.scheduler.view_events()
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, events)

    def remove_past_events(self):
        result = self.scheduler.remove_past_events()
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, result)

    def clear_entries(self):
        self.date_time_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)


# Main application
if __name__ == "__main__":
    root = tk.Tk()
    scheduler = EventScheduler()
    gui = EventSchedulerGUI(root, scheduler)
    root.mainloop()