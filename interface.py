from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from Task_manager import TaskManager
from event_scheduler import EventScheduler
from expense_manager import BudgetManager
from employee_database import EmployeeDatabase

task = TaskManager()
event = EventScheduler()
expense = BudgetManager()
employee = EmployeeDatabase()

root = Tk()
root.title("Business Planner")
root.geometry("870x700")
root.config(bg="white")


def Home_page():
    global main_label
    main_label = Label(root, text="Business Planner", font=("Bahnschrift SemiBold", 30, "bold"), height=1)
    main_label.pack(pady=7, fill="both")
    main_label.config(fg="steel blue", bg="white")

def HomePageContent():
    global home_frame
    home_frame = Frame(root, bg="steel blue")
    home_frame.pack(fill="both", expand=True, padx=10, pady=3)


    separator = ttk.Separator(home_frame, orient="horizontal")
    separator.pack(fill="x", pady=15, side="top", expand=True)

    heading = Label(home_frame, text="Welcome to Business Planner", font=("Bahnschrift SemiBold", 20, "bold"),
                    bg="steel blue", fg="white", justify="center")
    heading.pack(pady=4, side="top")

    content = Label(home_frame, text=("Your all-in-one solution for organizing tasks, managing events, "
                                      "tracking expenses, and handling employee data efficiently. Stay "
                                      "productive and in control with our easy-to-use tools, designed to "
                                      "Enhance your business planning needs."),
                    font=("Bahnschrift", 12), bg="steel blue", fg="white", wraplength=700, justify="center")
    content.pack(pady=4, side="top")

    separator = ttk.Separator(home_frame, orient="horizontal")
    separator.pack(fill="x", pady=15, side="top", expand=True)

def menu():
    global menu_button
    menu_button = Button(root, text="OPEN", command=Tabs, width=40, height=1, bg="grey", fg="white",font=("Bahnschrift SemiBold", 10, "bold"))
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
        anchor="center",
        relief="solid",
    )
    style.configure("Top.TNotebook", tabposition="wn")
    style.configure("TNotebook", tabmargins=[5, 5, 5, 5])

    notebook.configure(style="Top.TNotebook")

    about = Frame(notebook, bg="steel blue", padx=10)
    task_manager = Frame(notebook, bg="light grey", padx=10)
    event_manager = Frame(notebook, bg="light grey", padx=10)
    expense_manager = Frame(notebook, bg="light grey", padx=10)
    employee_database = Frame(notebook, bg="light grey", padx=10)

    def back():
        notebook_frame.destroy()
        Home_page()
        HomePageContent()
        menu()

    home_b = Button(notebook, text="Home", width=15, command=back, bg="grey", fg="white")
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
    main_label = Label(task_manager, text="Task Manager", font=("Bahnschrift SemiBold", 30, "bold"))
    main_label.grid(row=0, pady=7, columnspan=5, sticky="ns")
    main_label.config(fg="white", bg="light grey")

    separator = ttk.Separator(task_manager, orient="horizontal")
    separator.grid(row=1, column=0, columnspan=5, sticky="ew", pady=7)

    l1 = Label(task_manager, text="Description", bg="light grey", font=("Bahnschrift SemiBold", 10, "bold"))
    l1.grid(row=2, column=0, padx=10, pady=10, sticky="w")

    l2 = Label(task_manager, text="Priority", bg="light grey", font=("Bahnschrift SemiBold", 10, "bold"))
    l2.grid(row=3, column=0, padx=10, pady=10, sticky="w")

    l3 = Label(task_manager, text="Date/Time", bg="light grey", font=("Bahnschrift SemiBold", 10, "bold"))
    l3.grid(row=4, column=0, padx=10, pady=10, sticky="w")

    l5 = Label(task_manager, text="(1-High, 2-Medium, 3-Low)", bg="light grey", font=("Bahnschrift", 10))
    l5.grid(row=3, column=2, padx=10, pady=10, sticky="w")

    l6 = Label(task_manager, text="(YYYY-MM-DD HH:MM)", bg="light grey", font=("Bahnschrift", 10))
    l6.grid(row=4, column=2, padx=10, pady=10, sticky="w")

    t_description = Entry(task_manager)
    t_description.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    t_priority = Entry(task_manager)
    t_priority.grid(row=3, column=1, padx=10, pady=10, sticky="w")

    t_deadline = Entry(task_manager)
    t_deadline.grid(row=4, column=1, padx=10, pady=10, sticky="w")

    def handling_task():
        desc = t_description.get()
        priority = t_priority.get()
        deadline = t_deadline.get()
        task.add_task(desc, priority, deadline)

    add_b = Button(task_manager, text="Add Task", command=handling_task, width=20, bg="light blue", height=2)
    add_b.grid(row=6, column=0, padx=10, pady=5, sticky="w")

    tree_frame = Frame(task_manager)
    tree_frame.grid(row=7, column=0, padx=10, pady=10, columnspan=20)

    t_tree = ttk.Treeview(tree_frame, height=17)
    t_tree["columns"] = (["ID", "Description", "Priority", "Deadline", "Status"])

    t_tree.column("#0", width=0)
    t_tree.column("ID", width=50, anchor=W)
    t_tree.column("Description", width=200, anchor=W)
    t_tree.column("Priority", width=100, anchor=W)
    t_tree.column("Deadline", width=150, anchor=W)
    t_tree.column("Status", width=150, anchor=W)

    t_tree.heading("#0", text="")
    t_tree.heading("ID", text="ID", anchor=W)
    t_tree.heading("Description", text="Description", anchor=W)
    t_tree.heading("Priority", text="Priority", anchor=W)
    t_tree.heading("Deadline", text="Deadline", anchor=W)
    t_tree.heading("Status", text="Status", anchor=W)

    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Bahnschrift SemiBold", 12, 'bold'))
    style.map("Treeview", background=[("selected", "#bce6ff")])

    # Define tags for coloring
    t_tree.tag_configure("pending", background="yellow")
    t_tree.tag_configure("done", background="lightgreen")

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
                status = "pending"
                tag = "pending" if status == "pending" else "done"
                t_tree.insert("", "end", values=i, tags=(tag,))

    view_b = Button(task_manager, text="View Task", width=20, command=adding_treeview, bg="light blue", height=2)
    view_b.grid(row=6, column=1, padx=10, pady=5, sticky="w")

    def refresh_treeview():
        for row in t_tree.get_children():
            t_tree.delete(row)
        tasks = task.view_tasks()
        for i in tasks:
            t_tree.insert("", "end", values=i)

    l4 = Label(task_manager, text="Enter/Select ID To Remove", bg="light grey",
               font=("Bahnschrift SemiBold", 10, "bold"))
    l4.grid(row=2, column=2, padx=10, pady=10, sticky="w")

    t_remove = Entry(task_manager, width=25)
    t_remove.grid(row=2, column=3, padx=10, pady=10, sticky="w")

    def remove_task():
        try:
            task_id_input = t_remove.get()
            if task_id_input:
                task_id = int(task_id_input)
                if task.remove_task(task_id) is True:
                    messagebox.showinfo("Success", "Task removed successfully!")
                    refresh_treeview()
                else:
                    messagebox.showerror("Error", "Task ID not found!")
            else:
                selected_item = t_tree.selection()
                if selected_item is not None:
                    task_id = int(t_tree.item(selected_item[0])['values'][0])
                    if task.remove_task(task_id) is True:
                        t_tree.delete(selected_item[0])
                        messagebox.showinfo("Success", f"Task ID {task_id} removed.")
                    else:
                        messagebox.showerror("Error", "Task ID not found.")
                else:
                    messagebox.showerror("Error", "Please select a task to remove.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid Task ID.")

    remove_b = Button(task_manager, text="Remove Task", width=20, command=remove_task, bg="light blue", height=2)
    remove_b.grid(row=6, column=2, padx=10, pady=5, sticky="w")

    def mark_task_done():
        try:
            selected_item = t_tree.selection()
            if selected_item:
                task_id = int(t_tree.item(selected_item[0])['values'][0])
                task.mark_task_as_done(task_id)
                refresh_treeview()
            else:
                messagebox.showerror("Error", "Please select a task to mark as done.")
        except ValueError:
            messagebox.showerror("Error", "Invalid Task ID.")

    done_b = Button(task_manager, text="Mark as Done", width=20, command=mark_task_done, bg="light blue", height=2)
    done_b.grid(row=4, column=3, padx=10, pady=10, sticky="w")

    def remove_expired_tasks():
        task.remove_past_tasks()
        messagebox.showinfo("Success", "All expired tasks removed!")
        refresh_treeview()

    past_b = Button(task_manager, text="Remove Expired Tasks", width=20, command=remove_expired_tasks, bg="light blue", height=2)
    past_b.grid(row=6, column=3, padx=10, pady=5, sticky="w")


def About():
    main_label = Label(about, text="About", font=("Bahnschrift SemiBold", 30, "bold"))
    main_label.grid(row=0, column=1, pady=7, sticky="n")
    main_label.config(fg="white", bg="steel blue")

    separator = ttk.Separator(about, orient="horizontal")
    separator.grid(row=1, column=0, columnspan=10, sticky="we", pady=10, padx=10)

    ownership = Label(about, text="Ownership", bg="steel blue", font=("Bahnschrift SemiBold", 20, "bold"), fg="white")
    ownership.grid(row=2, column=0, padx=10, pady=10, sticky="w")

    Devloped = Label(about, text="Developed by:", bg="steel blue", font=("Bahnschrift SemiBold", 15),fg="white")
    Devloped.grid(row=3, column=0, padx=10, pady=5, sticky="w")

    names = Label(about, text="H&S", bg="steel blue", font=("Bahnschrift", 12), fg="white")
    names.grid(row=3, column=1, pady=5, sticky="w")

    id = Label(about, text="ID:", bg="steel blue", font=("Bahnschrift SemiBold", 15, "bold"), fg="white")
    id.grid(row=4, column=0, padx=10, pady=5, sticky="w")

    sap = Label(about, text="56754 & 56804", bg="steel blue", font=("Bahnschrift", 12), fg="white")
    sap.grid(row=4, column=1, pady=5, sticky="w")

    department = Label(about, text="Department", bg="steel blue", font=("Bahnschrift SemiBold", 15, "bold"), fg="white")
    department.grid(row=5, column=0, padx=10, pady=5, sticky="w")

    bscy = Label(about, text="BSCY-3", bg="steel blue", font=("Bahnschrift", 12), fg="white")
    bscy.grid(row=5, column=1, pady=5, sticky="w")

    rights = Label(about, text="© 2025 All Rights Reserved.", bg="steel blue", font=("Bahnschrift SemiBold", 12),
                   fg="white")
    rights.grid(row=6, column=0, padx=5, pady=15, sticky="w")

    separator = ttk.Separator(about, orient="horizontal")
    separator.grid(row=7, column=0, columnspan=10, sticky="we", pady=20, padx=10)

    project = Label(about, text="About this Project", bg="steel blue", font=("Bahnschrift SemiBold", 20), fg="white")
    project.grid(row=9, column=0, padx=10, pady=10, sticky="w")

    p_details = (
        "• This project is a comprehensive business planner designed to simplify task management, event scheduling, expense tracking, and employee database.\n\n"
        "• It provides an intuitive interface and efficient tools to enhance productivity and streamline business operations.\n\n"
        "• This app showcases my growing skills in Python, GUI development (Tkinter), and practical problem-solving.")

    details = Label(about, text=p_details, bg="steel blue", font=("Bahnschrift SemiBold", 12), fg="white",
                    justify="left", wraplength=700)
    details.grid(row=10, column=0, columnspan=10, padx=10, pady=0, sticky="n")

def Event_manager():
    main_label = Label(event_manager, text="Event Schedular", font=("Bahnschrift SemiBold", 30, "bold"))
    main_label.grid(row=0, column=0, columnspan=10, pady=7, sticky="ns")
    main_label.config(fg="white", bg="light grey")

    separator = ttk.Separator(event_manager, orient="horizontal")
    separator.grid(row=1, column=0, columnspan=10, sticky="ew", pady=7)

    l1 = Label(event_manager, text="Description:", bg="light grey", font=("Bahnschrift SemiBold", 10), fg="black")
    l1.grid(row=2, column=0, padx=10, pady=10, sticky="w")

    l2 = Label(event_manager, text="Date/Time:", bg="light grey", font=("Bahnschrift SemiBold", 10), fg="black")
    l2.grid(row=3, column=0, padx=10, pady=10, sticky="w")

    l3 = Label(event_manager, text="(YYYY-MM-DD H:M)", bg="light grey", font=("Bahnschrift", 10))
    l3.grid(row=3, column=2, padx=10, pady=10, sticky="w")

    e_description = Entry(event_manager)
    e_description.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    e_time = Entry(event_manager)
    e_time.grid(row=3, column=1, padx=10, pady=10, sticky="w")

    def handling_event():
        desc = e_description.get()
        time = e_time.get()
        event.add_event(time, desc)

    add_b = Button(event_manager, text="Add Event", command=handling_event, width=20, bg="light blue", height=2)
    add_b.grid(row=7, column=0, padx=10, pady=10, sticky="w")

    tree_frame = Frame(event_manager)
    tree_frame.grid(row=8, column=0, padx=10, pady=10, columnspan=20)

    e_tree = ttk.Treeview(tree_frame, height=18)
    e_tree["columns"] = ["ID", "Description", "Date/time"]

    e_tree.column("#0", width=0)
    e_tree.column("ID", width=50, anchor=W)
    e_tree.column("Description", width=400, anchor=W)
    e_tree.column("Date/time", width=200, anchor=W)

    e_tree.heading("#0", text="")
    e_tree.heading("ID", text="ID", anchor=W)
    e_tree.heading("Description", text="Description", anchor=W)
    e_tree.heading("Date/time", text="Date/time", anchor=W)

    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Bahnschrift SemiBold", 12, 'bold'))

    scrollbar = Scrollbar(tree_frame, command=e_tree.yview)
    e_tree.config(yscrollcommand=scrollbar.set)

    e_tree.pack(side="left", expand=True, fill="both")
    scrollbar.pack(side="right", expand=True, fill="both")

    def adding_treeview():
        for row in e_tree.get_children():
            e_tree.delete(row)
        events = event.view_events()

        if not events:
            messagebox.showinfo("Empty", "No Events Added Yet")
        else:
            for x in events:
                e_tree.insert("", "end", values=x)

    view_b = Button(event_manager, text="View Events", width=20, command=adding_treeview, bg="light blue", height=2)
    view_b.grid(row=7, column=1, padx=10, pady=10, sticky="w")

    l3 = Label(event_manager, text="Enter/Select ID To Remove", bg="light grey",
               font=("Bahnschrift SemiBold", 10, "bold"))
    l3.grid(row=2, column=2, padx=10, pady=15, sticky="w")

    e_remove = Entry(event_manager)
    e_remove.grid(row=2, column=3, padx=10, pady=15, sticky="w")

    def refresh_treeview():
        for row in e_tree.get_children():
            e_tree.delete(row)
        events = event.view_events()
        for i in events:
            e_tree.insert("", "end", values=i)

    def remove_event():
        try:
            input_id = e_remove.get()
            if input_id:
                event_id = int(input_id)
                if event.remove_event(event_id) is True:
                    messagebox.showinfo("Success", "Event removed successfully!")
                    refresh_treeview()
                else:
                    messagebox.showerror("Error", "Event ID not found!")
            else:
                selected_item = e_tree.selection()
                if selected_item:
                    event_id = int(e_tree.item(selected_item[0])['values'][0])
                    if event.remove_event(event_id) is True:
                        e_tree.delete(selected_item[0])
                        messagebox.showinfo("Success", f"Event ID {event_id} removed.")
                    else:
                        messagebox.showerror("Error", "Event ID not found.")
                else:
                    messagebox.showerror("Error", "Please select an event to remove.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid Event ID.")

    remove_b = Button(event_manager, text="Remove Event", width=20, command=remove_event, bg="light blue", height=2)
    remove_b.grid(row=7, column=2, padx=10, pady=10, sticky="w")

    def remove_past():
        event.remove_past_events()
        messagebox.showinfo("Success", "All past events removed!")
        refresh_treeview()

    past_b = Button(event_manager, text="Remove Expired Events", width=20, command=remove_past, bg="light blue", height=2)
    past_b.grid(row=7, column=3, padx=10, pady=10, sticky="w")

def Expense_manager():
    main_label = Label(expense_manager, text="Expense Manager", font=("Bahnschrift SemiBold", 30, "bold"))
    main_label.grid(row=0, column=0, columnspan=10, pady=7, sticky="ns")
    main_label.config(fg="white", bg="light grey")

    separator = ttk.Separator(expense_manager, orient="horizontal")
    separator.grid(row=1, column=0, columnspan=10, sticky="ew", pady=7)

    l1 = Label(expense_manager, text="Name:", bg="light grey", font=("Bahnschrift SemiBold", 10, "bold"))
    l1.grid(row=2, column=0, padx=10, pady=10, sticky="w")

    l2 = Label(expense_manager, text="Amount:", bg="light grey", font=("Bahnschrift SemiBold", 10, "bold"))
    l2.grid(row=3, column=0, padx=10, pady=10, sticky="w")

    l3 = Label(expense_manager, text="Category:", bg="light grey", font=("Bahnschrift SemiBold", 10, "bold"))
    l3.grid(row=4, column=0, padx=10, pady=10, sticky="w")

    l5 = Label(expense_manager, text="Description:", bg="light grey", font=("Bahnschrift SemiBold", 10, "bold"))
    l5.grid(row=5, column=0, padx=10, pady=10, sticky="w")

    ex_name = Entry(expense_manager)
    ex_name.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    ex_amount = Entry(expense_manager)
    ex_amount.grid(row=3, column=1, padx=10, pady=10, sticky="w")

    options = ["Marketing", "Operational Cost", "Development Cost", "Maintenance & Support", "Legal Matters", "Debts",
               "Capital expenditure"]

    ex_category = ttk.Combobox(expense_manager, values=options, width=17)
    ex_category.grid(row=4, column=1, padx=10, pady=10, sticky="w")
    ex_category.set("Marketing")

    ex_description = Entry(expense_manager)
    ex_description.grid(row=5, column=1, padx=10, pady=10, sticky="w")

    def handling_expenses():
        name = ex_name.get()
        amount = ex_amount.get()
        category = ex_category.get()
        desc = ex_description.get()
        try:
            expense.add_budget(name, amount, category, desc)
            messagebox.showinfo("success", "expense added successfully")
        except:
            messagebox.showerror("Error", "Could not Add expense")

    add_b = Button(expense_manager, text="Add Budget", width=25, command=handling_expenses, bg="light blue", height=2)
    add_b.grid(row=2, column=2, padx=15, pady=10, sticky="w")

    tree_frame = Frame(expense_manager)
    tree_frame.grid(row=7, column=0, padx=10, pady=10, columnspan=20)

    ex_tree = ttk.Treeview(tree_frame, height=17)
    ex_tree["columns"] = (["Name", "Amount", "Category", "Description", "Status"])

    ex_tree.column("#0", width=0)
    ex_tree.column("Name", width=125, anchor=W)
    ex_tree.column("Amount", width=100, anchor=W)
    ex_tree.column("Category", width=150, anchor=W)
    ex_tree.column("Description", width=175, anchor=W)
    ex_tree.column("Status", width=115, anchor=W)

    ex_tree.heading("#0", text="")
    ex_tree.heading("Name", text="Name", anchor=W)
    ex_tree.heading("Amount", text="Amount", anchor=W)
    ex_tree.heading("Category", text="Category", anchor=W)
    ex_tree.heading("Description", text="Description", anchor=W)
    ex_tree.heading("Status", text="Status", anchor=W)

    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Bahnschrift SemiBold", 12, 'bold'))

    scrollbar = Scrollbar(tree_frame, command=ex_tree.yview)
    ex_tree.config(yscrollcommand=scrollbar.set)

    ex_tree.pack(side="left", expand=True, fill="both")
    scrollbar.pack(side="right", expand=True, fill="both")

    def adding_treeview():
        if ex_tree.get_children():
            ex_tree.delete(*ex_tree.get_children())
        try:
            budgets = expense.view_budgets()
            if not budgets:
                messagebox.showerror("Empty", "No Budgets Added Yet")
                return
            print("Budgets to display:", budgets)
            for x in budgets:
                if len(x) == 5:
                    ex_tree.insert("", "end", values=x)
                else:
                    messagebox.showwarning("Data Issue", "Some budgets have missing values.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    view_b = Button(expense_manager, text="View Budgets", width=25, command=adding_treeview, bg="light blue", height=2)
    view_b.grid(row=3, column=2, padx=15, pady=10, sticky="w")

    l5 = Label(expense_manager, text="NAME (Approval/Disapproval)", bg="light grey",
               font=("Bahnschrift SemiBold", 10, "bold"))
    l5.grid(row=5, column=2, padx=15, pady=10, sticky="w")

    ex_status = Entry(expense_manager, width=30)
    ex_status.grid(row=5, column=3, padx=15, pady=10, sticky="w")

    def handle_approval():
        budget_name = ex_status.get()
        if budget_name:
            expense.approve_budget(budget_name)
            messagebox.showinfo("Success", f"Budget for {budget_name} approved successfully.")
        else:
            messagebox.showwarning("Input Error", "Please enter a valid budget name.")

    app_b = Button(expense_manager, text="Approve Budget", width=25, command=handle_approval, bg="light blue", height=2)
    app_b.grid(row=2, column=3, padx=15, pady=10, sticky="w")

    def handle_disapproval():
        budget_name = ex_status.get()
        if budget_name:
            expense.disapprove_budget(budget_name)
            adding_treeview()
            messagebox.showinfo("Success", f"Budget for {budget_name} has been marked as disapproved.")
        else:
            messagebox.showwarning("Input Error", "Please enter a valid budget name.")

    dis_b = Button(expense_manager, text="Disapprove Budget", width=25, command=handle_disapproval, bg="light blue", height=2)
    dis_b.grid(row=3, column=3, padx=15, pady=10, sticky="w")

def Employeer_database():
    main_label = Label(employee_database, text="Employee Database", font=("Bahnschrift SemiBold", 30, "bold"))
    main_label.grid(row=0, column=0, columnspan=10, pady=7, sticky="ns")
    main_label.config(fg="white", bg="light grey")

    separator = ttk.Separator(employee_database, orient="horizontal")
    separator.grid(row=1, column=0, columnspan=10, sticky="ew", pady=7)

    def add_employee():
        root = Tk()
        root.title("Add Employee")
        root.geometry("750x600")
        root.config(bg="white")

        main_label = Label(root, text="Add Employee", font=("Bahnschrift SemiBold", 30, "bold"))
        main_label.grid(row=0, column=0, columnspan=5, pady=5, padx=10, sticky="n")
        main_label.config(fg="black", bg="white")

        separator = ttk.Separator(root, orient="horizontal")
        separator.grid(row=1, column=0, columnspan=5, sticky="ew", pady=10, padx=10)

        p_info = Label(root, text="Personal Information", font=("Bahnschrift SemiBold", 14, "bold"), bg="white")
        p_info.grid(row=2, column=0, sticky="w", pady=5, padx=20)

        employee_id = Label(root, text="ID:", fg="grey", bg="white")
        employee_id.grid(row=3, column=0, sticky="w", pady=5, padx=20)
        employee_id = Label(root, text=employee.generate_employee_id(), fg="grey", bg="white")
        employee_id.grid(row=3, column=1, sticky="w", pady=5, padx=20)

        fullname_label = Label(root, text="Full Name:", font=("Bahnschrift", 12), bg="white")
        fullname_label.grid(row=4, column=0, pady=5, sticky="w", padx=20)
        fullname_entry = Entry(root, bg="light grey")
        fullname_entry.grid(row=4, column=1, pady=5, padx=20)

        fathername_label = Label(root, text="Father's Name:", font=("Bahnschrift", 12), bg="white")
        fathername_label.grid(row=4, column=2, pady=5, sticky="w", padx=20)
        fathername_entry = Entry(root, bg="light grey")
        fathername_entry.grid(row=4, column=3, pady=5, padx=20)

        gender_label = Label(root, text="Gender:", font=("Bahnschrift", 12), bg="white")
        gender_label.grid(row=5, column=0, pady=5, sticky="w", padx=20)
        opt = ["Male", "Female", "helicopter"]
        gender_entry = ttk.Combobox(root, values=opt, width=17)
        gender_entry.grid(row=5, column=1, pady=5, padx=20)
        gender_entry.set("")

        marital_status_label = Label(root, text="Marital Status:", font=("Bahnschrift", 12), bg="white")
        marital_status_label.grid(row=5, column=2, pady=5, sticky="w", padx=20)
        opt = ["Married", "Single", "Divorced", "Lonely"]
        marital_status_entry = ttk.Combobox(root, values=opt, width=17)
        marital_status_entry.grid(row=5, column=3, pady=5, padx=20)
        marital_status_entry.set("")

        separator = ttk.Separator(root, orient="horizontal")
        separator.grid(row=7, column=0, columnspan=5, sticky="ew", pady=10, padx=10)

        c_info = Label(root, text="Contact Information", font=("Bahnschrift SemiBold", 14, "bold"), bg="white")
        c_info.grid(row=8, column=0, sticky="w", pady=5, padx=20)

        phone_label = Label(root, text="Phone:", font=("Bahnschrift", 12), bg="white")
        phone_label.grid(row=9, column=0, pady=5, sticky="w", padx=20)
        phone_entry = Entry(root, bg="light grey")
        phone_entry.grid(row=9, column=1, pady=5, padx=20)

        email_label = Label(root, text="Email:", font=("Bahnschrift", 12), bg="white")
        email_label.grid(row=10, column=0, pady=5, sticky="w", padx=20)
        email_entry = Entry(root, bg="light grey")
        email_entry.grid(row=10, column=1, pady=5, padx=20)

        address_label = Label(root, text="Address:", font=("Bahnschrift", 12), bg="white")
        address_label.grid(row=11, column=0, pady=5, sticky="w", padx=20)
        address_entry = Entry(root, bg="light grey")
        address_entry.grid(row=11, column=1, pady=5, padx=20)

        separator = ttk.Separator(root, orient="horizontal")
        separator.grid(row=12, column=0, columnspan=5, sticky="ew", pady=10, padx=10)

        j_info = Label(root, text="Job Details", font=("Bahnschrift SemiBold", 14, "bold"), bg="white")
        j_info.grid(row=13, column=0, sticky="w", pady=5, padx=20)

        department_label = Label(root, text="Department:", font=("Bahnschrift", 12), bg="white")
        department_label.grid(row=14, column=0, pady=5, sticky="w", padx=20)
        opt = ["Marketing", "Development", "security", "Legal", "Human Resource"]
        department_entry = ttk.Combobox(root, values=opt, width=17)
        department_entry.grid(row=14, column=1, pady=5, padx=20)
        department_entry.set("")

        position_label = Label(root, text="Position:", font=("Bahnschrift", 12), bg="white")
        position_label.grid(row=15, column=0, pady=5, sticky="w", padx=20)
        position_entry = Entry(root, bg="light grey")
        position_entry.grid(row=15, column=1, pady=5, padx=20)

        hours_label = Label(root, text="Hours per Week:", font=("Bahnschrift", 12), bg="white")
        hours_label.grid(row=14, column=2, pady=5, sticky="w", padx=20)
        hours_entry = Entry(root, bg="light grey")
        hours_entry.grid(row=14, column=3, pady=5, padx=20)

        salary_label = Label(root, text="Salary:", font=("Bahnschrift", 12), bg="white")
        salary_label.grid(row=15, column=2, pady=5, sticky="w", padx=20)
        salary_entry = Entry(root, bg="light grey")
        salary_entry.grid(row=15, column=3, pady=5, padx=20)

        separator = ttk.Separator(root, orient="horizontal")
        separator.grid(row=16, column=0, columnspan=5, sticky="ew", pady=5, padx=10)

        def handling_emp_addition():
            fullname = fullname_entry.get()
            fathername = fathername_entry.get()
            gender = gender_entry.get()
            marital_status = marital_status_entry.get()
            phone = phone_entry.get()
            email = email_entry.get()
            address = address_entry.get()
            department = department_entry.get()
            position = position_entry.get()
            hours = hours_entry.get()
            salary = salary_entry.get()

            if not fullname or not fathername or not gender or not marital_status or not phone or not email or not address or not department or not position or not hours or not salary:
                messagebox.showwarning("Input Error", "All fields are required!")
                return

            personal_info = {'fullname': fullname, 'fathername': fathername, 'gender': gender,'marital_status': marital_status}
            contact_info = {'phone': phone, 'email': email, 'address': address}
            job_details = {'department': department, 'position': position, 'hours_per_week': hours, 'salary': salary}

            employee.add_employee(personal_info, contact_info, job_details)
            messagebox.showinfo("Success", f"Employee {fullname} added successfully!")

        save_button = Button(root, text="SAVE", width=20, command=handling_emp_addition, bg="green", fg="white")
        save_button.grid(row=18, column=0, columnspan=1, pady=15, padx=20, sticky="w")

        root.mainloop()

    add_b = Button(employee_database, text="Add an Employee", width=20, command=add_employee, bg="light blue", height=2)
    add_b.grid(row=2, column=0, padx=10, pady=10, sticky="w")

    tree_frame = Frame(employee_database)
    tree_frame.grid(row=7, column=0, padx=10, pady=50, columnspan=20)

    em_tree = ttk.Treeview(tree_frame, height=17)
    em_tree["columns"] = (["ID", "Name", "Department", "Salary", "Working Hours"])

    em_tree.column("#0", width=0)
    em_tree.column("ID", width=50, anchor=W)
    em_tree.column("Name", width=150, anchor=W)
    em_tree.column("Department", width=150, anchor=W)
    em_tree.column("Salary", width=125, anchor=W)
    em_tree.column("Working Hours", width=175, anchor=W)

    em_tree.heading("#0", text="")
    em_tree.heading("ID", text="ID", anchor=W)
    em_tree.heading("Name", text="Name", anchor=W)
    em_tree.heading("Department", text="Department", anchor=W)
    em_tree.heading("Salary", text="Salary", anchor=W)
    em_tree.heading("Working Hours", text="Working Hours", anchor=W)

    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Bahnschrift SemiBold", 12, 'bold'))

    scrollbar = Scrollbar(tree_frame, command=em_tree.yview)
    em_tree.config(yscrollcommand=scrollbar.set)

    em_tree.pack(side="left", expand=True, fill="both")
    scrollbar.pack(side="right", expand=True, fill="both")

    def adding_in_treeview():
        employee_data = employee.display_employees()

        if not employee_data:
            messagebox.showinfo("No Employees", "No employees to display.")
            return

        for row in em_tree.get_children():
            em_tree.delete(row)

        for emp in employee_data:
            em_tree.insert("", "end", values=emp)


    display_b = Button(employee_database, text="Display all Employees", width=20, command=adding_in_treeview, bg="light blue", height=2)
    display_b.grid(row=3, column=0, padx=10, pady=5, sticky="w")

    def employee_form(employee_data):
        root = Tk()
        root.title("Employee Details")
        root.geometry("600x600")
        root.config(bg="white")

        main_label = Label(root, text="Employee Details", font=("Bahnschrift SemiBold", 30, "bold"))
        main_label.grid(row=0, column=0, columnspan=5, pady=5, padx=10, sticky="n")
        main_label.config(fg="black", bg="white")

        separator = ttk.Separator(root, orient="horizontal")
        separator.grid(row=1, column=0, columnspan=5, sticky="ew", pady=10, padx=10)

        Label(root, text="Personal Information", font=("Bahnschrift SemiBold", 16, "bold"), bg="white").grid(
         row=2, column=0, columnspan=5, sticky="w", pady=5, padx=10)

        Label(root, text="ID:", bg="white", font=("Bahnschrift SemiBold", 12, "bold")).grid(row=3, column=0, sticky="w", pady=5, padx=10)
        Label(root, text=employee_data["employee_id"], bg="light grey").grid(row=3, column=1, sticky="w", pady=5,padx=10)

        Label(root, text="Full Name:", bg="white", font=("Bahnschrift SemiBold", 12, "bold")).grid(row=4, column=0, sticky="w", pady=5, padx=10)
        Label(root, text=employee_data["fullname"], bg="light grey").grid(row=4, column=1, sticky="w", pady=5, padx=10)

        Label(root, text="Father's Name:", bg="white", font=("Bahnschrift SemiBold", 12, "bold")).grid(row=4, column=2, sticky="w", pady=5, padx=10)
        Label(root, text=employee_data["fathername"], bg="light grey").grid(row=4, column=3, sticky="w", pady=5,padx=10)

        Label(root, text="Gender:", bg="white", font=("Bahnschrift SemiBold", 12, "bold")).grid(row=5, column=0, sticky="w", pady=5, padx=10)
        Label(root, text=employee_data["gender"], bg="light grey").grid(row=5, column=1, sticky="w", pady=5, padx=10)

        Label(root, text="Marital Status:", bg="white", font=("Bahnschrift SemiBold", 12, "bold")).grid(row=5, column=2, sticky="w", pady=5, padx=10)
        Label(root, text=employee_data["marital_status"], bg="light grey").grid(row=5, column=3, sticky="w", pady=5,padx=10)

        separator = ttk.Separator(root, orient="horizontal")
        separator.grid(row=6, column=0, columnspan=5, sticky="ew", pady=10, padx=10)

        Label(root, text="Contact Information", font=("Bahnschrift SemiBold", 16, "bold"), bg="white").grid(
        row=7, column=0, columnspan=5, sticky="w", pady=5, padx=10)

        Label(root, text="Phone:", bg="white", font=("Bahnschrift SemiBold", 12, "bold")).grid(row=8, column=0, sticky="w", pady=5, padx=10)
        Label(root, text=employee_data["phone"], bg="light grey").grid(row=8, column=1, sticky="w", pady=5, padx=10)

        Label(root, text="Email:", bg="white", font=("Bahnschrift SemiBold", 12, "bold")).grid(row=8, column=2, sticky="w", pady=5, padx=10)
        Label(root, text=employee_data["email"], bg="light grey").grid(row=8, column=3, sticky="w", pady=5, padx=10)

        Label(root, text="Address:", bg="white", font=("Bahnschrift SemiBold", 12, "bold")).grid(row=9, column=0, sticky="w", pady=5, padx=10)
        Label(root, text=employee_data["address"], bg="light grey").grid(row=9, column=1, columnspan=3, sticky="w",pady=5, padx=10)

        separator = ttk.Separator(root, orient="horizontal")
        separator.grid(row=10, column=0, columnspan=5, sticky="ew", pady=10, padx=10)

        Label(root, text="Job Details", font=("Bahnschrift SemiBold", 16, "bold"), bg="white").grid(
        row=11, column=0, columnspan=5, sticky="w", pady=5, padx=10)

        Label(root, text="Department:", bg="white", font=("Bahnschrift SemiBold", 12, "bold")).grid(row=12, column=0, sticky="w", pady=5, padx=10)
        Label(root, text=employee_data["department"], bg="light grey").grid(row=12, column=1, sticky="w", pady=5,padx=10)

        Label(root, text="Position:", bg="white", font=("Bahnschrift SemiBold", 12, "bold")).grid(row=12, column=2, sticky="w", pady=5, padx=10)
        Label(root, text=employee_data["position"], bg="light grey").grid(row=12, column=3, sticky="w", pady=5, padx=10)

        Label(root, text="Hours per Week:", bg="white", font=("Bahnschrift SemiBold", 12, "bold")).grid(row=13, column=0, sticky="w", pady=5, padx=10)
        Label(root, text=employee_data["hours_per_week"], bg="light grey").grid(row=13, column=1, sticky="w", pady=5,padx=10)

        Label(root, text="Salary:", bg="white", font=("Bahnschrift SemiBold", 12, "bold")).grid(row=13, column=2, sticky="w", pady=5, padx=10)
        Label(root, text=employee_data["salary"], bg="light grey").grid(row=13, column=3, sticky="w", pady=5, padx=10)

        separator = ttk.Separator(root, orient="horizontal")
        separator.grid(row=15, column=0, columnspan=5, sticky="ew", pady=5)

        close_button = Button(root, text="CLOSE", width=20, bg="red", fg="white", command=root.destroy)
        close_button.grid(row=18, column=0, columnspan=1, pady=15, padx=10, sticky="w")

        root.mainloop()

    def show_employee():
        employee_id = search_entry.get()
        employee_data = employee.search_employee(employee_id)

        if employee_data:
            employee_form(employee_data)
        else:
            messagebox.showinfo("Employee Not Found", f"No employee found with ID {employee_id}")

    search_label = Label(employee_database, text="Enter Search ID:", font=("Bahnschrift", 10), bg="light grey")
    search_label.grid(row=2, column=1, pady=10, sticky="w", padx=10)
    search_entry = Entry(employee_database, width=25)
    search_entry.grid(row=2, column=2, pady=10, padx=5, sticky="w")

    search_b = Button(employee_database, text="search Employee", width=20, command=show_employee, bg="light blue", height=2)
    search_b.grid(row=2, column=3, padx=20, pady=10, sticky="w")

    remove_label = Label(employee_database, text="Enter removal ID:", font=("Bahnschrift", 10), bg="light grey")
    remove_label.grid(row=3, column=1, pady=10, sticky="w", padx=10)
    removal_entry = Entry(employee_database, width=25)
    removal_entry.grid(row=3, column=2, pady=10, padx=5, sticky="w")

    def refresh_treeview():
        for row in em_tree.get_children():
            em_tree.delete(row)

        adding_in_treeview()

    def handling_removal():
        remove_id = removal_entry.get()
        if not remove_id:
            messagebox.showerror("Input Error", "Employee ID is required.")
            return
        if employee.remove_employee(remove_id):
            messagebox.showinfo("Success", "Employee Removed Successfully!")
            refresh_treeview()
        else:
            messagebox.showerror("Error", "Employee not found or error occurred.")

    remove_b = Button(employee_database, text="Remove employee", width=20, command=handling_removal, bg="light blue", height=2)
    remove_b.grid(row=3, column=3, padx=20, pady=10, sticky="w")

def bar():
    text = StringVar()
    text.set("Access all the feature by clicking OPEN, and Good luck, Have Fun!")
    bar = Label(root, textvariable=text)
    bar.config(fg="white", bg="steel blue", height=2)
    bar.pack(side="bottom", fill="x")

Home_page()
HomePageContent()
menu()
bar()

root.mainloop()
