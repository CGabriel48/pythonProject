
class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.archivo = archivo
        self.productos = self.cargar_inventario()

    def cargar_inventario(self):
        productos = {}
        try:
            with open(self.archivo, 'r') as file:
                for linea in file:
                    nombre, cantidad = linea.strip().split(',')
                    productos[nombre] = int(cantidad)
        except FileNotFoundError:
            print(f"Archivo '{self.archivo}' no encontrado, se creará un nuevo archivo.")
        except Exception as e:
            print(f"Error al cargar el inventario: {e}")
        return productos

    def guardar_inventario(self):
        try:
            with open(self.archivo, 'w') as file:
                for nombre, cantidad in self.productos.items():
                    file.write(f"{nombre},{cantidad}\n")
        except PermissionError:
            print(f"No tienes permiso para escribir en el archivo '{self.archivo}'.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def agregar_producto(self, nombre, cantidad):
        if nombre in self.productos:
            self.productos[nombre] += cantidad
        else:
            self.productos[nombre] = cantidad
        self.guardar_inventario()

    def eliminar_producto(self, nombre):
        if nombre in self.productos:
            del self.productos[nombre]
            self.guardar_inventario()
        else:
            print(f"El producto '{nombre}' no existe en el inventario.")

    def actualizar_producto(self, nombre, cantidad):
        if nombre in self.productos:
            self.productos[nombre] = cantidad
            self.guardar_inventario()
        else:
            print(f"El producto '{nombre}' no existe en el inventario.")
def mostrar_menu():
    print("Sistema de Gestión de Inventarios")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Mostrar inventario")
    print("5. Salir")

def ejecutar():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            inventario.agregar_producto(nombre, cantidad)
            print(f"Producto '{nombre}' agregado/actualizado exitosamente.")
        elif opcion == '2':
            nombre = input("Nombre del producto: ")
            inventario.eliminar_producto(nombre)
            print(f"Producto '{nombre}' eliminado exitosamente.")
        elif opcion == '3':
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Nueva cantidad: "))
            inventario.actualizar_producto(nombre, cantidad)
            print(f"Producto '{nombre}' actualizado exitosamente.")
        elif opcion == '4':
            for nombre, cantidad in inventario.productos.items():
                print(f"{nombre}: {cantidad}")
        elif opcion == '5':
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

if __name__ == "__main__":
    ejecutar()