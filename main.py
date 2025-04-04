import tkinter as tk
from tkinter import ttk

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

