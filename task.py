import tkinter as tk
from tkinter import ttk

# Class for storing task information
#   - Name
#   - Completed
class Task: 
    def __init__(self, name):
        self.name = name
        self.start_date = ""
        self.completed = False
    def json(self):
        obj = {"name": self.name}
        return obj

# Class for the task widget
#   - Takes in Task and creates card Widget
class TaskCard:
    def __init__(self, root, task, tasks_file):
        self.task = task
        self.root = root
        self.tasks_file = tasks_file
    def add_content(self):
        self.content = ttk.Frame(self.root)
        self.label = ttk.Label(self.content, text=self.task.name)
        self.complete_button = ttk.Button(self.content, text="Complete", command=self.delete_task)
    def pack_content(self):
        self.label.pack(expand=False, fill=tk.NONE, side=tk.LEFT)
        self.complete_button.pack(expand=False, fill=tk.NONE, side=tk.RIGHT)
        self.content.pack(expand=False, fill=tk.X, ipadx=5, ipady=5, padx=5)
    def delete_task(self):
        self.tasks_file.content_json.remove(self.task.json())
        self.content.pack_forget()
