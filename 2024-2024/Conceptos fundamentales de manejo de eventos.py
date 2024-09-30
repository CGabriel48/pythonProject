import tkinter as tk
from tkinter import messagebox


class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        # marco principal
        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        # Campo de entrada para agregar una tarea
        self.task_entry = tk.Entry(self.frame, width=30)
        self.task_entry.grid(row=0, column=0, padx=10)
        self.task_entry.bind("<Return>", self.add_task)

        # Botón para añadir tarea
        self.add_button = tk.Button(self.frame, text="Añadir Tarea", width=15, command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10)

        # Lista de tareas
        self.task_listbox = tk.Listbox(self.frame, height=10, width=50, selectmode=tk.SINGLE)
        self.task_listbox.grid(row=1, column=0, columnspan=2, pady=10)

        # Botón para marcar como completada
        self.complete_button = tk.Button(self.frame, text="Marcar como Completada", width=20,
                                         command=self.complete_task)
        self.complete_button.grid(row=2, column=0, padx=10, pady=5)

        # Botón para eliminar
        self.delete_button = tk.Button(self.frame, text="Eliminar Tarea", width=20, command=self.delete_task)
        self.delete_button.grid(row=2, column=1, padx=10, pady=5)

    def add_task(self, event=None):
        task = self.task_entry.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada Vacía", "No puedes añadir una tarea vacía.")

    def complete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(selected_task_index)
            self.task_listbox.delete(selected_task_index)
            self.task_listbox.insert(tk.END, f"[Completada] {task}")
        except IndexError:
            messagebox.showwarning("Sin Selección", "Selecciona una tarea para marcarla como completada.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Sin Selección", "Selecciona una tarea para eliminarla.")


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
