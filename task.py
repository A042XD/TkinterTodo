import tkinter as tk
from tkinter import ttk
from dates import *

# Class for storing task information
#   - Name
#   - Completed
class Task: 
    def __init__(self, name, date=current_date):
        self.name = name
        self.start_date = date
        self.completed = False
    def set_start_date(self, date):
        self.start_date = date
    def json(self):
        obj = {"name": self.name, "date": self.start_date.to_dict()}
        return obj
class DeadlineTask:
   pass 

# Class for the task widget
#   - Takes in Task and creates card Widget
class TaskCard:
    def __init__(self, root, task, tasks_file):
        self.task = task
        self.root = root
        self.tasks_file = tasks_file
    def add_content(self):
        self.content = ttk.Frame(self.root, border=2)
        self.label = ttk.Label(self.content, text=self.task.name)
        start_date_label = "Created on " + self.task.start_date.to_string()
        self.date_label = ttk.Label(self.content, text=start_date_label)
        self.complete_button = ttk.Button(self.content, text="Complete", command=self.delete_task)
    def pack_content(self):
        self.label.pack(expand=False, fill=tk.NONE, side=tk.LEFT)
        self.date_label.pack(expand=True, fill=tk.NONE, side=tk.LEFT, anchor=tk.CENTER)
        self.complete_button.pack(expand=False, fill=tk.NONE, side=tk.RIGHT)
        self.content.pack(expand=False, fill=tk.X, ipadx=5, ipady=5, padx=5)
    def delete_task(self):
        self.tasks_file.content_json.remove(self.task.json())
        self.content.pack_forget()
