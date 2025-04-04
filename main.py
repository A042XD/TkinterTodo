import tkinter as tk
from tkinter import ttk

"""
# Setup
root = tk.Tk()
root.title("Habits Tracker")
root.geometry("400x600")
content = ttk.Frame(root)

# Widgets
widgets = {}
widgets["tasks_list"] = ttk.Frame(content)
widgets["tasks_list"].pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
name = tk.StringVar(root)
widgets["name_entry"] = tk.Entry(content, textvariable=name)
widgets["name_entry"].pack(expand=False, fill=tk.X, padx=5, pady=5)

class task:
    def __init__(self, name):
        self.name = name
        self.root = None
        self.frame = None
    def complete(self):
        self.frame.pack_forget()
        del self
    def widget_card(self, root):
        self.root = root
        self.frame = ttk.Frame(root)
        label = ttk.Label(self.frame, text=self.name).pack(expand=False, fill=tk.NONE, padx=5, pady=5, side=tk.LEFT)
        button = ttk.Button(self.frame, text="Complete", command=self.complete).pack(expand=False, fill=tk.NONE, padx=5, pady=5, side=tk.RIGHT)
        self.frame.pack(fill=tk.X, padx=5, pady=5)
def add_task():
    tmp = task(name.get())
    tmp.widget_card(widgets["tasks_list"])
    name.set("")

widgets["add_button"] = ttk.Button(content, text="Add task", command=add_task)
widgets["add_button"].pack(expand=False, fill=tk.X, padx=5, pady=5)
content.pack(expand=True, fill=tk.BOTH)

# Mainloop
root.mainloop()
"""

import os

class File:
    def __init__(self, path):
        self.path = path
    def open_create(self):
        pass 
class Task: 
    def __init__(self, name, date):
        self.name = name
        self.start_date = ""
        self.completed = False
class TasksPage:
    def __init__(self, root):
        self.root = root
        self.content = ttk.Frame(self.root)
        self.content.pack(expand=True, fill=tk.BOTH)
        self.add_content()
        self.pack_content()
    def add_content(self):
        self.caption = ttk.Label(self.content, text="Tasks")
        self.tasks_list = ttk.Frame(self.content)
        self.add_entry_var = tk.StringVar(self.root)
        self.add_entry = ttk.Entry(self.content, textvariable=self.add_entry_var)
        self.add_button = ttk.Button(self.content, text="Add Task", command=self.create_task)
    def pack_content(self):
        self.caption.pack(anchor=tk.W, padx=5, pady=5)
        self.tasks_list.pack(expand=True, fill=tk.BOTH)
        self.add_entry.pack(fill=tk.X, padx=5, pady=5)
        self.add_button.pack(fill=tk.X, padx=5, pady=5)
    def create_task(self):
        self.add_entry_var.set("")
class App:
    def __init__(self, root):
        self.root = root
        self.notebook = ttk.Notebook(self.root)
        self.content1 = ttk.Frame(self.root)
        self.content2 = ttk.Frame(self.root)
        self.content3 = ttk.Frame(self.root)
        TasksPage(self.content1)
        self.notebook.add(self.content1, text="Tasks")
        self.notebook.add(self.content2, text="Habits")
        self.notebook.add(self.content3, text="Statistics")
        self.notebook.pack(expand=True, fill=tk.BOTH)
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Todo App")
    root.geometry("400x600+200+100")
    root.resizable(False, True)
    App(root)
    root.mainloop()
