from tkinter import *
import tkinter.ttk
from tkinter import ttk
from Task_manager import TaskManager
from event_scheduler import EventScheduler
from expense_manager import BudgetManager
from employee_database import EmployeeDatabase

root = Tk()
root.title("personalfinance tracker")
root.geometry("700x600")
root.config(bg="white")

def menu():
    global menu_button
    menu_button = Button(root, text="menu", command=Tabs)
    menu_button.pack(side="top", anchor="w")

def Tabs():
    notebook_frame = Frame(root, bg="white")
    notebook_frame.pack(side="top", fill="both", expand=True, padx=5, pady=5)  # Pack the notebook frame at the top

    notebook = ttk.Notebook(notebook_frame)
    notebook.pack(fill="both", expand=True)

    # text
    style = ttk.Style()
    style.configure(
        "TNotebook.Tab",
        padding=[10, 10],
        width=15,
        background = "red",
        anchor='center',
        relief="solid",
    )
    # tabs
    style.configure("Top.TNotebook", tabposition="wn")
    style.configure("TNotebook", tabmargins=[5,5,5,5])

    notebook.configure(style="Top.TNotebook")


    about = Frame(notebook, bg="steel blue", padx=10)
    task_manager = Frame(notebook, bg="lightblue", padx=10)
    event_manager = Frame(notebook, bg="lightgreen", padx=10)
    expense_manager = Frame(notebook, bg="lightpink", padx=10)
    employee_database = Frame(notebook, bg="lightpink", padx=10)

    def back():
        notebook_frame.destroy()
        menu()

    b1 = Button(notebook, text="Home", width=15, command=back)
    b1.pack(side="bottom", anchor="w", padx=5, pady=5)


    notebook.add(about, text="About")
    notebook.add(task_manager, text="Tasks")
    notebook.add(event_manager, text="Events")
    notebook.add(expense_manager, text="Expenses")
    notebook.add(employee_database, text="Employees")

    menu_button.destroy()

def bar():
    # Footer text
    text = StringVar()
    text.set("Group Project\t\t\tDeveloped by Hamza and Sunnan\t\t\t56804, 56754")
    bar = Label(root, textvariable=text)
    bar.config(fg="black", bg="light blue", height=2)
    bar.pack(side="bottom", fill="x")



menu()
bar()

root.mainloop()
