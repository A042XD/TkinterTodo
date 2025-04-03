import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Todo-app")
root.geometry("400x400")
content = ttk.Frame(root)

button = [ttk.Button(content, text="hello", command=None) for i in range(0,10)]
for i in button:
    i.pack()
label = ttk.Label(content, text="test-text", foreground="white", width=50,background="black")
label.pack()

entry = ttk.Entry(content)
entry.insert(0,"卧槽")
entry.delete(0,tk.END)
entry.get()

text_box = tk.Text(content)
text_box.get("1.0","2.5") # 从 (1,0) 到 (2,5) 的矩阵的内容

text_box.pack()
entry.pack()

content.pack()
root.mainloop()
