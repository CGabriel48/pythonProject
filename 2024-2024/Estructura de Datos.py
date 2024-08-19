#Producto
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters
    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Setters
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


#Inventario
class Inventario:
    def __init__(self):
        self.productos = []

    def añadir_producto(self, producto):
        if any(prod.get_id() == producto.get_id() for prod in self.productos):
            print(f"Error: Ya existe un producto con el ID {producto.get_id()}.")
        else:
            self.productos.append(producto)
            print(f"Producto {producto.get_nombre()} añadido con éxito.")

    def eliminar_producto(self, id):
        self.productos = [prod for prod in self.productos if prod.get_id() != id]
        print(f"Producto con ID {id} eliminado, si existía.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        for prod in self.productos:
            if prod.get_id() == id:
                if cantidad is not None:
                    prod.set_cantidad(cantidad)
                if precio is not None:
                    prod.set_precio(precio)
                print(f"Producto con ID {id} actualizado.")
                return
        print(f"Producto con ID {id} no encontrado.")

    def buscar_producto(self, nombre):
        resultados = [prod for prod in self.productos if nombre.lower() in prod.get_nombre().lower()]
        if resultados:
            for prod in resultados:
                print(prod)
        else:
            print(f"No se encontraron productos con el nombre '{nombre}'.")

    def mostrar_productos(self):
        if self.productos:
            for prod in self.productos:
                print(prod)
        else:
            print("El inventario está vacío.")


# Interfaz de Usuario
def menu():
    inventario = Inventario()

    while True:
        print("\nSistema de Gestión de Inventarios")
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar cantidad o precio de un producto por ID")
        print("4. Buscar producto(s) por nombre")
        print("5. Mostrar todos los productos en el inventario")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad del producto: "))
            precio = float(input("Ingrese precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == '2':
            id = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == '3':
            id = input("Ingrese ID del producto a actualizar: ")
            cantidad = input("Ingrese nueva cantidad (o presione Enter para dejarla igual): ")
            precio = input("Ingrese nuevo precio (o presione Enter para dejarlo igual): ")
            inventario.actualizar_producto(id, cantidad=int(cantidad) if cantidad else None,
                                           precio=float(precio) if precio else None)

        elif opcion == '4':
            nombre = input("Ingrese nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == '5':
            inventario.mostrar_productos()

        elif opcion == '6':
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    menu()
