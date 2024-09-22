import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import datetime

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("600x400")

        # Frame para la lista de eventos
        self.frame_eventos = tk.Frame(self.root)
        self.frame_eventos.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # TreeView para mostrar la lista de eventos
        self.eventos_tree = ttk.Treeview(self.frame_eventos, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.eventos_tree.heading("Fecha", text="Fecha")
        self.eventos_tree.heading("Hora", text="Hora")
        self.eventos_tree.heading("Descripción", text="Descripción")
        self.eventos_tree.pack(fill=tk.BOTH, expand=True)

        # Frame para los campos de entrada
        self.frame_inputs = tk.Frame(self.root)
        self.frame_inputs.pack(fill=tk.X, padx=10, pady=5)

        # Etiqueta y campo de entrada para la fecha
        self.lbl_fecha = tk.Label(self.frame_inputs, text="Fecha:")
        self.lbl_fecha.grid(row=0, column=0, padx=5, pady=5)
        self.entry_fecha = DateEntry(self.frame_inputs, date_pattern="yyyy-mm-dd")
        self.entry_fecha.grid(row=0, column=1, padx=5, pady=5)

        # Etiqueta y campo de entrada para la hora
        self.lbl_hora = tk.Label(self.frame_inputs, text="Hora (HH:MM):")
        self.lbl_hora.grid(row=0, column=2, padx=5, pady=5)
        self.entry_hora = tk.Entry(self.frame_inputs)
        self.entry_hora.grid(row=0, column=3, padx=5, pady=5)

        # Etiqueta y campo de entrada para la descripción
        self.lbl_desc = tk.Label(self.frame_inputs, text="Descripción:")
        self.lbl_desc.grid(row=1, column=0, padx=5, pady=5)
        self.entry_desc = tk.Entry(self.frame_inputs)
        self.entry_desc.grid(row=1, column=1, columnspan=3, padx=5, pady=5, sticky="we")

        # Frame para los botones
        self.frame_botones = tk.Frame(self.root)
        self.frame_botones.pack(fill=tk.X, padx=10, pady=10)

        # Botón para agregar eventos
        self.btn_agregar = tk.Button(self.frame_botones, text="Agregar Evento", command=self.agregar_evento)
        self.btn_agregar.pack(side=tk.LEFT, padx=5)

        # Botón para eliminar evento seleccionado
        self.btn_eliminar = tk.Button(self.frame_botones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento)
        self.btn_eliminar.pack(side=tk.LEFT, padx=5)

        # Botón para salir
        self.btn_salir = tk.Button(self.frame_botones, text="Salir", command=self.root.quit)
        self.btn_salir.pack(side=tk.RIGHT, padx=5)

    def agregar_evento(self):
        """Función para agregar un evento a la lista."""
        fecha = self.entry_fecha.get()
        hora = self.entry_hora.get()
        descripcion = self.entry_desc.get()

        # Validar los campos antes de agregar el evento
        if not fecha or not hora or not descripcion:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        try:
            # Verificar si la hora está en formato HH:MM
            datetime.datetime.strptime(hora, '%H:%M')
        except ValueError:
            messagebox.showerror("Error", "La hora debe estar en formato HH:MM")
            return

        # Agregar el evento al TreeView
        self.eventos_tree.insert("", tk.END, values=(fecha, hora, descripcion))

        # Limpiar los campos de entrada
        self.entry_fecha.set_date(datetime.datetime.now())
        self.entry_hora.delete(0, tk.END)
        self.entry_desc.delete(0, tk.END)

    def eliminar_evento(self):
        """Función para eliminar el evento seleccionado de la lista."""
        selected_item = self.eventos_tree.selection()

        if not selected_item:
            messagebox.showwarning("Advertencia", "Debe seleccionar un evento para eliminar")
            return

        # Confirmación antes de eliminar
        if messagebox.askyesno("Confirmación", "¿Está seguro que desea eliminar el evento seleccionado?"):
            self.eventos_tree.delete(selected_item)

# Crear la ventana principal
if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
