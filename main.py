import tkinter as tk
from tkinter import ttk
from file import *
from task import *
from dates import *

<<<<<<< HEAD
root = tk.Tk()
root.title("Habits Tracker")
root.geometry("400x600")
content = ttk.Frame(root)

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
def add_habit():
    tmp = task(name.get())
    tmp.widget_card(widgets["tasks_list"])
    name.set("")

widgets["add_button"] = ttk.Button(content, text="Add task", command=add_habit)
widgets["add_button"].pack(expand=False, fill=tk.X, padx=5, pady=5)

content.pack(expand=True, fill=tk.BOTH)
root.mainloop()

=======
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
        tmp = TaskCard(self.tasks_list, task, self.tasks_file)
        tmp.add_content()
        tmp.pack_content()
        self.add_entry_var.set("")
    def add_tasks_from_tasks_file(self):
        for i in self.tasks_file.content_json:
            tmp_task = Task(i["name"])
            if 'date' in i:
                tmp_task.set_start_date(to_date(i["date"]))
            tmp = TaskCard(self.tasks_list, tmp_task, self.tasks_file)
            tmp.add_content()
            tmp.pack_content()
class AppInterface:
    def __init__(self, root, tasks_file):
        self.root = root
        self.notebook = ttk.Notebook(self.root)
        self.content1 = ttk.Frame(self.root)
        self.content2 = ttk.Frame(self.root)
        self.content3 = ttk.Frame(self.root)
        self.content4 = ttk.Frame(self.root)
        TasksPage(self.content1, tasks_file)
        self.notebook.add(self.content1, text="Tasks")
        self.notebook.add(self.content2, text="Habits")
        self.notebook.add(self.content3, text="History")
        self.notebook.add(self.content4, text="Statistics")
        self.notebook.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
class App:
    def __init__(self):
        self.tasks_path = os.getcwd() + "/data/tasks.json"
        self.habits_path = os.getcwd() + "/data/habits.json"
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
>>>>>>> file-saving
