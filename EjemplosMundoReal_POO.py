class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True  # Un libro está disponible por defecto

    def __str__(self):
        return f"{self.titulo} por {self.autor} (ISBN: {self.isbn})"

#clase hecha para saber quien posee el libro actualmente
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario

    def __str__(self):
        return f"{self.nombre} (ID: {self.id_usuario})"

#esta clase muestrara que libro y quien lo tiene en el momento
class Reserva:
    def __init__(self, libro, usuario):
        self.libro = libro
        self.usuario = usuario

    def __str__(self):
        return f"Reserva: {self.libro.titulo} reservado por {self.usuario.nombre}"

#esta clase es "el edificio" dentro del codigo
class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.reservas = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro agregado: {libro}")

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"Usuario registrado: {usuario}")

    def realizar_reserva(self, isbn, id_usuario):
        libro = self.buscar_libro_por_isbn(isbn)
        usuario = self.buscar_usuario_por_id(id_usuario)
        if libro and usuario:
            if libro.disponible:
                reserva = Reserva(libro, usuario)
                self.reservas.append(reserva)
                libro.disponible = False
                print(f"Reserva realizada: {reserva}")
            else:
                print(f"El libro {libro.titulo} no está disponible.")
        else:
            print("Libro o usuario no encontrado.")

    def buscar_libro_por_isbn(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                return libro
        return None

    def buscar_usuario_por_id(self, id_usuario):
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                return usuario
        return None


#dos funciones de busqueda para que se pueda encontrar el libro y el poseedor actual de este

    def mostrar_libros_disponibles(self):
        disponibles = [libro for libro in self.libros if libro.disponible]
        if disponibles:
            print("Libros disponibles:")
            for libro in disponibles:
                print(libro)
        else:
            print("No hay libros disponibles.")

    def mostrar_reservas(self):
        if self.reservas:
            print("Reservas actuales:")
            for reserva in self.reservas:
                print(reserva)
        else:
            print("No hay reservas.")


# Crear una instancia de la biblioteca
mi_biblioteca = Biblioteca()

# Agregar libros a la biblioteca
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "978-3-16-148410-0")
libro2 = Libro("Constitucion de la republica del Ecuador", "George Orwell", "978-0-452-28423-4")
mi_biblioteca.agregar_libro(libro1)
mi_biblioteca.agregar_libro(libro2)

# Registrar usuarios en la biblioteca
usuario1 = Usuario("Juan Pérez", "001")
usuario2 = Usuario("Ana Gómez", "002")
mi_biblioteca.registrar_usuario(usuario1)
mi_biblioteca.registrar_usuario(usuario2)

# Realizar reservas de libros
mi_biblioteca.realizar_reserva("978-3-16-148410-0", "001")
mi_biblioteca.realizar_reserva("978-0-452-28423-4", "002")

# Mostrar libros disponibles y reservas actuales
mi_biblioteca.mostrar_libros_disponibles()
mi_biblioteca.mostrar_reservas()
