from datetime import datetime

class TaskNode:
    def __init__(self, task_id, description, priority, deadline):
        self.task_id = task_id
        self.description = description
        self.priority = priority
        self.deadline = deadline
        self.next = None

class TaskManager:
    def __init__(self):
        self.head = None
        self.task_counter = 0

    def add_task(self, description, priority, deadline):
        task_id = self.task_counter
        self.task_counter += 1

        # converts the input time into given format
        deadline = datetime.strptime(deadline, "%Y-%m-%d %H:%M")
        new_task = TaskNode(task_id, description, priority, deadline)

        # sorting the nodes based on priority
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

        # adding info to the list
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
            # checking current nodes deadline
            if current.deadline < current_time:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                current = current.next
            else:
                previous = current
                current = current.next


# Just for the command line interface
def CLI():
    task_manager = TaskManager()

    while True:
        print("\nTask Manager CLI")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Remove Past Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            priority = int(input("Enter task priority (lower number = higher priority): "))
            deadline = input("Enter task deadline (YYYY-MM-DD HH:MM): ")

            try:
                task_id = task_manager.add_task(description, priority, deadline)
                print(f"Task added successfully with ID: {task_id}")
            except ValueError:
                print("Invalid deadline format. Please use 'YYYY-MM-DD HH:MM'.")

        elif choice == "2":
            tasks = task_manager.view_tasks()
            if tasks:
                print("\nTasks:")
                for task in tasks:
                    print(f"ID: {task[0]}, Description: {task[1]}, Priority: {task[2]}, Deadline: {task[3]}")
            else:
                print("No tasks available.")

        elif choice == "3":
            task_id = int(input("Enter the task ID to remove: "))
            if task_manager.remove_task(task_id):
                print(f"Task {task_id} removed successfully.")
            else:
                print(f"Task {task_id} not found.")

        elif choice == "4":
            task_manager.remove_past_tasks()
            print("Past tasks removed successfully.")

        elif choice == "5":
            print("Exiting Task Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    CLI()
