from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Task_manager import TaskManager
from event_scheduler import EventScheduler
from expense_manager import BudgetManager
from employee_database import EmployeeDatabase

task = TaskManager()

root = Tk()
root.title("Business Planner")
root.geometry("850x780")
root.config(bg="white")

def Home_page():
    global  main_label
    main_label = Label(root, text="Business Planner", font=("Bahnschrift SemiBold", 30,"bold"), height=1)
    main_label.pack(pady=7, fill="both")
    main_label.config(fg="steel blue", bg="white")

def HomePageContent():

    global home_frame
    home_frame = Frame(root, bg="steel blue")
    home_frame.pack(fill="both", expand=True, padx=10, pady=3)

    separator = ttk.Separator(home_frame, orient="horizontal")
    separator.pack(fill="x", pady=15, side="top", expand=True)

    heading = Label(home_frame,text="Welcome to Business Planner",font=("Bahnschrift SemiBold", 20, "bold"),
        bg="steel blue", fg="white", justify="center")
    heading.pack(pady=4, side="top")

    content = Label(home_frame,text=("Your all-in-one solution for organizing tasks, managing events, "
            "tracking expenses, and handling employee data efficiently. Stay "
            "productive and in control with our easy-to-use tools, designed to "
            "Enhance your business planning needs."),
            font=("Bahnschrift", 12),  bg="steel blue", fg="white", wraplength=700,justify="center")
    content.pack(pady=4, side="top")

    separator = ttk.Separator(home_frame, orient="horizontal")
    separator.pack(fill="x", pady=15, side="top", expand=True)

def menu():
    global menu_button
    menu_button = Button(root, text="OPEN", command=Tabs, width=40, height=1, bg="steel blue", fg="white", font=("Bahnschrift SemiBold", 10, "bold"))
    menu_button.pack(side="top", anchor="s", padx=5, pady=10)


def Tabs():
    global notebook_frame, notebook, about, task_manager, event_manager, expense_manager, employee_database

    notebook_frame = Frame(root, bg="white")
    notebook_frame.pack(side="top", fill="both", expand=True, padx=5, pady=5)

    notebook = ttk.Notebook(notebook_frame)
    notebook.pack(fill="both", expand=True)

    style = ttk.Style()
    style.configure(
        "TNotebook.Tab",
        padding=[10, 10],
        width=15,
        background="red",
        anchor="center",
        relief="solid",
    )
    style.configure("Top.TNotebook", tabposition="wn")
    style.configure("TNotebook", tabmargins=[5, 5, 5, 5])

    notebook.configure(style="Top.TNotebook")

    about = Frame(notebook, bg="steel blue", padx=10)
    task_manager = Frame(notebook, bg="light blue", padx=10)
    event_manager = Frame(notebook, bg="light green", padx=10)
    expense_manager = Frame(notebook, bg="light pink", padx=10)
    employee_database = Frame(notebook, bg="light pink", padx=10)

    def back():
        notebook_frame.destroy()
        Home_page()
        HomePageContent()
        menu()


    home_b = Button(notebook, text="Home", width=15, command=back, bg="steel blue", fg="white")
    home_b.pack(side="bottom", anchor="w", padx=5, pady=5)

    notebook.add(about, text="About")
    notebook.add(task_manager, text="Tasks")
    notebook.add(event_manager, text="Events")
    notebook.add(expense_manager, text="Expenses")
    notebook.add(employee_database, text="Employees")

    main_label.destroy()
    menu_button.destroy()
    home_frame.destroy()
    Task_manager()
    Expense_manager()
    Event_manager()
    Employeer_database()
    About()

def Task_manager():

    main_label = Label(task_manager, text="Task Manager", font=("Bahnschrift SemiBold", 30,"bold"))
    main_label.grid(row=0, pady=7, columnspan=4, sticky="ns")
    main_label.config(fg="white", bg="light blue")

    separator = ttk.Separator(task_manager, orient="horizontal")
    separator.grid(row=1, column=0, columnspan=4, sticky="ew", pady=7)

    # adding tasks section
    l1 = Label(task_manager, text="Description", bg="light blue", font=("Bahnschrift SemiBold", 10, "bold"))
    l1.grid(row=2, column=0, padx=10, pady=10, sticky="w")

    l2 = Label(task_manager, text="Priority", bg="light blue", font=("Bahnschrift SemiBold", 10, "bold"))
    l2.grid(row=3, column=0, padx=10, pady=10, sticky="w")

    l3 = Label(task_manager, text="Date/Time", bg="light blue", font=("Bahnschrift SemiBold", 10, "bold"))
    l3.grid(row=4, column=0, padx=10, pady=10, sticky="w")

    # Entry fields
    t_description = Entry(task_manager)
    t_description.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    t_priority = Entry(task_manager)
    t_priority.grid(row=3, column=1, padx=10, pady=10, sticky="w")

    t_deadline = Entry(task_manager)
    t_deadline.grid(row=4, column=1, padx=10, pady=10, sticky="w")

    # Handling task function
    def handling_task():
        desc = t_description.get()
        priority = t_priority.get()
        deadline = t_deadline.get()
        task.add_task(desc, priority, deadline)

    add_b = Button(task_manager, text="Add Task", command=handling_task, width=20)
    add_b.grid(row=6, column=0, padx=10, pady=10, sticky="wn")

    # View task section
    tree_frame = Frame(task_manager)
    tree_frame.grid(row=7, column=0, padx=10, pady=10, columnspan=20, sticky="w")

    t_tree = ttk.Treeview(tree_frame, height=20)
    t_tree["columns"] = (["ID", "Description", "Priority", "Deadline"])

    t_tree.column("#0", width=0)
    t_tree.column("ID", width=50, anchor=W)
    t_tree.column("Description", width=200, anchor=W)
    t_tree.column("Priority", width=200, anchor=W)
    t_tree.column("Deadline", width=200, anchor=W)

    t_tree.heading("#0", text="")
    t_tree.heading("ID", text="ID", anchor=W)
    t_tree.heading("Description", text="Description", anchor=W)
    t_tree.heading("Priority", text="Priority", anchor=W)
    t_tree.heading("Deadline", text="Deadline", anchor=W)

    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Bahnschrift SemiBold", 12, 'bold'))

    scrollbar = Scrollbar(tree_frame, command=t_tree.yview)
    t_tree.config(yscrollcommand=scrollbar.set)

    t_tree.pack(side="left", expand=True, fill="both")
    scrollbar.pack(side="right", expand=True, fill="both")

    def adding_treeview():
        for row in t_tree.get_children():
            t_tree.delete(row)
        tasks = task.view_tasks()
        if not tasks:
            messagebox.showinfo("Empty", "No Tasks Added Yet")
        else:
            for i in tasks:
                t_tree.insert("","end", values=i)

    view_b = Button(task_manager, text="View Task", width=20, command=adding_treeview)
    view_b.grid(row=6, column=1, padx=10, pady=10, sticky="w")

    # Remove Task
    l3 = Label(task_manager, text="Enter Task ID To Remove", bg="light blue", font=("Bahnschrift SemiBold", 10, "bold"))
    l3.grid(row=2, column=2, padx=10, pady=10, sticky="w")

    t_remove = Entry(task_manager)
    t_remove.grid(row=2, column=3, padx=10, pady=10, sticky="w")

    # Refresh Treeview
    def refresh_treeview():
        for row in t_tree.get_children():
            t_tree.delete(row)
        tasks = task.view_tasks()
        for i in tasks:
            t_tree.insert("", "end", values=i)

    def handle_removal():
        try:
            task_id = int(t_remove.get())
            if task.remove_task(task_id):
                messagebox.showinfo("Success", "Task removed successfully!")
                refresh_treeview()
            else:
                messagebox.showerror("Error", "Task ID not found!")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid Task ID.")

    remove_b = Button(task_manager, text="Remove Task", width=20, command=handle_removal)
    remove_b.grid(row=6, column=2, padx=10, pady=10, sticky="w")

    # Remove Past Tasks
    def remove_expired_tasks():
        task.remove_past_tasks()
        messagebox.showinfo("Success", "All expired tasks removed!")
        refresh_treeview()

    past_b = Button(task_manager, text="Remove Expired Tasks", width=20, command=remove_expired_tasks)
    past_b.grid(row=6, column=3, padx=10, pady=10, sticky="w")

def About():
    main_label = Label(about, text="Task Manager", font=("Bahnschrift SemiBold", 30,"bold"))
    main_label.grid(row=0, column=3, pady=7, sticky="n")
    main_label.config(fg="white", bg="light blue")

    separator = ttk.Separator(about, orient="horizontal")
    separator.grid(row=1, column=3, columnspan=10, sticky="ew", pady=7)

def Event_manager():
    pass

def Expense_manager():
    pass
def Employeer_database():
    pass


def bar():
    text = StringVar()
    text.set("Access all the feature by clicking OPEN, and Good luck, Have Fun!")
    bar = Label(root, textvariable=text)
    bar.config(fg="black", bg="light blue", height=2)
    bar.pack(side="bottom", fill="x")

Home_page()
HomePageContent()
menu()
bar()

root.mainloop()
