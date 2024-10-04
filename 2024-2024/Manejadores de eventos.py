import tkinter as tk
from tkinter import messagebox

# Funciones para la lista
def add_task(event=None):
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task(event=None):
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Delete Error", "Please select a task to delete.")

def complete_task(event=None):
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(selected_task_index)
        # Mark the task as completed by adding a visual cue (e.g., adding a strikethrough effect)
        listbox_tasks.delete(selected_task_index)
        listbox_tasks.insert(selected_task_index, f"[COMPLETED] {task}")
    except IndexError:
        messagebox.showwarning("Completion Error", "Please select a task to mark as completed.")

#ventana principal
window = tk.Tk()
window.title("Task Manager")
window.geometry("400x400")

#elementos de la interfaz
entry_task = tk.Entry(window, width=35)
entry_task.pack(pady=10)

button_add_task = tk.Button(window, text="Add Task", width=40, command=add_task)
button_add_task.pack(pady=5)

button_delete_task = tk.Button(window, text="Delete Task", width=40, command=delete_task)
button_delete_task.pack(pady=5)

button_complete_task = tk.Button(window, text="Complete Task", width=40, command=complete_task)
button_complete_task.pack(pady=5)

listbox_tasks = tk.Listbox(window, height=15, width=50)
listbox_tasks.pack(pady=10)

#atajos con el teclado
window.bind('<Return>', add_task)
window.bind('<Delete>', delete_task)
window.bind('<c>', complete_task)
window.bind('<Escape>', lambda event: window.quit())

# Iniciar la interfaz gráfica
window.mainloop()
