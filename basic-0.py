# import tkinter as tk

# root = tk.Tk()

# label = tk.Label(root, text='Just a first GUI app', padx=10, pady=10)
# label.pack()

# root.mainloop()

# ------------------------------------------------ #

# import tkinter as tk


# class Root(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.label = tk.Label(self, text='Just a first GUI app', padx=10, pady=10)
#         self.label.pack()


# root = Root()
# root.mainloop()

# ------------------------------------------------ #

import tkinter as tk


def add_task(event=None):
    task_text = root.new.get()

    new_task = tk.Label(root, text=task_text, bg="green", fg="white", pady=10)
    new_task.pack(side=tk.TOP, fill=tk.X)
    root.tasks.append(new_task)
    root.new.delete(0, tk.END)


root = tk.Tk()

root.tasks = []
root.title("To-Do App v1")
root.geometry("300x400")

todo1 = tk.Label(root, text="--- Add Items Here ---", bg="lightgrey", fg="black", pady=10)
root.tasks.append(todo1)
root.tasks[0].pack(side=tk.TOP)
root.new = tk.Entry(root, bg="white", fg="black")
root.new.pack(side=tk.BOTTOM)
root.new.focus_set()

root.bind("<Return>", add_task)


root.mainloop()


# ------------------------------------------------ #


# import tkinter as tk


# class Todo(tk.Tk):
#     def __init__(self):
#         super().__init__()

#         self.tasks = []

#         self.title("To-Do App v1")
#         self.geometry("300x400")

#         todo1 = tk.Label(self, text="--- Add Items Here ---", bg="lightgrey", fg="black", pady=10)

#         self.tasks.append(todo1)
#         self.tasks[0].pack(side=tk.TOP)

#         self.new = tk.Text(self, height=3, bg="white", fg="black")

#         self.new.pack(side=tk.BOTTOM)
#         self.new.focus_set()

#         self.bind("<Return>", self.add_task)

#     def add_task(self, event=None):
#         task_text = self.new.get(1.0,tk.END).strip()

#         new_task = tk.Label(self, text=task_text, bg="green", fg="white", pady=10)
#         new_task.pack(side=tk.TOP, fill=tk.X)
#         self.tasks.append(new_task)

#         self.new.delete(1.0, tk.END)

# if __name__ == "__main__":
#     todo = Todo()
#     todo.mainloop()


# ------------------------------------------------ #

# import tkinter as tk
# import tkinter.messagebox as msg

# class Todo(tk.Tk):
#     def __init__(self, tasks=None):
#         super().__init__()

#         if not tasks:
#             self.tasks = []
#         else:
#             self.tasks = tasks

#         self.tasks_canvas = tk.Canvas(self)

#         self.tasks_frame = tk.Frame(self.tasks_canvas)
#         self.text_frame = tk.Frame(self)

#         self.scrollbar = tk.Scrollbar(self.tasks_canvas, orient="vertical", command=self.tasks_canvas.yview)

#         self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)

#         self.title("To-Do App v2")
#         self.geometry("300x400")

#         self.task_create = tk.Text(self.text_frame, height=3, bg="white", fg="black")

#         self.tasks_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
#         self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

#         self.canvas_frame = self.tasks_canvas.create_window((0, 0), window=self.tasks_frame, anchor="n")

#         self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
#         self.text_frame.pack(side=tk.BOTTOM, fill=tk.X)
#         self.task_create.focus_set()

#         todo1 = tk.Label(self.tasks_frame, text="--- Add Items Here ---", bg="lightgrey", fg="black", pady=10)
#         todo1.bind("<Button-1>", self.remove_task)

#         self.tasks.append(todo1)

#         for task in self.tasks:
#             task.pack(side=tk.TOP, fill=tk.X)

#         self.bind("<Return>", self.add_task)
#         self.bind("<Configure>", self.on_frame_configure)
#         self.bind_all("<MouseWheel>", self.mouse_scroll)
#         self.bind_all("<Button-4>", self.mouse_scroll)
#         self.bind_all("<Button-5>", self.mouse_scroll)
#         self.tasks_canvas.bind("<Configure>", self.task_width)

#         self.colour_schemes = [{"bg": "lightgrey", "fg": "black"}, {"bg": "grey", "fg": "white"}]

#     def add_task(self, event=None):
#         task_text = self.task_create.get(1.0,tk.END).strip()

#         if len(task_text) > 0:
#             new_task = tk.Label(self.tasks_frame, text=task_text, pady=10)

#             self.set_task_colour(len(self.tasks), new_task)

#             new_task.bind("<Button-1>", self.remove_task)
#             new_task.pack(side=tk.TOP, fill=tk.X)

#             self.tasks.append(new_task)

#         self.task_create.delete(1.0, tk.END)

#     def remove_task(self, event):
#         task = event.widget
#         if msg.askyesno("Really Delete?", "Delete " + task.cget("text") + "?"):
#             self.tasks.remove(event.widget)
#             event.widget.destroy()
#             self.recolour_tasks()

#     def recolour_tasks(self):
#         for index, task in enumerate(self.tasks):
#             self.set_task_colour(index, task)

#     def set_task_colour(self, position, task):
#         _, task_style_choice = divmod(position, 2)

#         my_scheme_choice = self.colour_schemes[task_style_choice]

#         task.configure(bg=my_scheme_choice["bg"])
#         task.configure(fg=my_scheme_choice["fg"])

#     def on_frame_configure(self, event=None):
#         self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all"))

#     def task_width(self, event):
#         canvas_width = event.width
#         self.tasks_canvas.itemconfig(self.canvas_frame, width = canvas_width)

#     def mouse_scroll(self, event):
#         if event.delta:
#             self.tasks_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
#         else:
#             if event.num == 5:
#                 move = 1
#             else:
#                 move = -1

#             self.tasks_canvas.yview_scroll(move, "units")

# if __name__ == "__main__":
#     todo = Todo()
#     todo.mainloop()