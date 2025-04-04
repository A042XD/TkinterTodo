import os, json
import tkinter as tk
from tkinter import ttk

class File:
    def __init__(self, path):
        self.path = path
        self.content = []
    def read(self):
        if os.path.exists(self.path) == False:
            self.content = [""]
        else:
            with open(self.path, 'r') as file:
                for line in file:
                    self.content.append(line.strip())
                file.close()
    def save(self):
        with open(self.path, 'w') as file:
            file.writelines(self.content)
            file.close()
class JsonFile(File):
    def __init__(self, path):
        super().__init__(path)
        self.content_single = ""
        self.content_json = []
    def restruct(self):
        self.content_single = ""
        for i in self.content:
            self.content_single += i
    def read(self):
        File.read(self)
        if self.content == [""] or self.content == []:
            self.content_json = []
        else:
            self.restruct()
            try:
                self.content_json = json.loads(self.content_single)
            except json.decoder.JSONDecodeError:
                self.content_json = []
    def save(self):
        self.content = [json.dumps(self.content_json)]
        File.save(self)
class Task: 
    def __init__(self, name):
        self.name = name
        self.start_date = ""
        self.completed = False
    def json(self):
        obj = {"name": self.name}
        return obj
class TaskCard:
    def __init__(self, root, task):
        self.task = task
        self.root = root
    def add_content(self):
        self.content = ttk.Frame(self.root)
        self.label = ttk.Label(self.content, text=self.task.name)
        self.complete_button = ttk.Button(self.content, text="Complete")
    def pack_content(self):
        self.label.pack(expand=False, fill=tk.NONE, side=tk.LEFT)
        self.complete_button.pack(expand=False, fill=tk.NONE, side=tk.RIGHT)
        self.content.pack(expand=False, fill=tk.X, ipadx=5, ipady=5, padx=5)
class TasksPage:
    def __init__(self, root, tasks_file):
        self.root = root
        self.tasks_file = tasks_file
        self.content = ttk.Frame(self.root)
        self.content.pack(expand=True, fill=tk.BOTH)
        self.add_content()
        self.pack_content()
        self.add_tasks_from_tasks_file()
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
        task = Task(self.add_entry_var.get())
        self.tasks_file.content_json.insert(0, task.json())
        # print(self.tasks_file.content_json)
        tmp = TaskCard(self.tasks_list, task)
        tmp.add_content()
        tmp.pack_content()
        self.add_entry_var.set("")
    def add_tasks_from_tasks_file(self):
        for i in self.tasks_file.content_json:
            tmp = TaskCard(self.tasks_list, Task(i["name"]))
            tmp.add_content()
            tmp.pack_content()
class AppInterface:
    def __init__(self, root, tasks_file):
        self.root = root
        self.notebook = ttk.Notebook(self.root)
        self.content1 = ttk.Frame(self.root)
        self.content2 = ttk.Frame(self.root)
        self.content3 = ttk.Frame(self.root)
        TasksPage(self.content1, tasks_file)
        self.notebook.add(self.content1, text="Tasks")
        self.notebook.add(self.content2, text="Habits")
        self.notebook.add(self.content3, text="Statistics")
        self.notebook.pack(expand=True, fill=tk.BOTH)
class App:
    def __init__(self):
        self.tasks_path = os.getcwd() + "/tasks.json"
        self.tasks_file = JsonFile(self.tasks_path)
        self.tasks_file.read()
        
        # App Interface
        self.root = tk.Tk()
        self.root.title("Todo App")
        self.root.geometry("400x600+200+100")
        self.root.resizable(False, False)
        AppInterface(self.root, self.tasks_file)
        self.root.mainloop()

        self.tasks_file.save()
if __name__ == "__main__":
    App()
