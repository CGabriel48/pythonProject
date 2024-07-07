# como lcase prinsipal voy a ocupar un producto para ocuparlo en un "mercado"

class Producto:
    def __init__(self, nombre, cantidad, precio):
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    def obtener_informacion(self):
        return f"Nombre: {self._nombre}, Cantidad: {self._cantidad}, Precio: {self._precio}"

    def calcular_valor_total(self):
        return self._cantidad * self._precio


    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_cantidad(self):
        return self._cantidad

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def get_precio(self):
        return self._precio

    def set_precio(self, precio):
        self._precio = precio

# aqui voy a crear 3 subclases siendo agricola, ganadero y pesquero
class ProductoAgricola(Producto):
    def __init__(self, nombre, cantidad, precio, tipo_cultivo):
        super().__init__(nombre, cantidad, precio)
        self.tipo_cultivo = tipo_cultivo

    def obtener_informacion(self):
        return f"{super().obtener_informacion()}, Tipo de Cultivo: {self.tipo_cultivo}"


class ProductoGanadero(Producto):
    def __init__(self, nombre, cantidad, precio, tipo_ganado):
        super().__init__(nombre, cantidad, precio)
        self.tipo_ganado = tipo_ganado

    def obtener_informacion(self):
        return f"{super().obtener_informacion()}, Tipo de Ganado: {self.tipo_ganado}"


class ProductoPesquero(Producto):
    def __init__(self, nombre, cantidad, precio, tipo_pescado):
        super().__init__(nombre, cantidad, precio)
        self.tipo_pescado = tipo_pescado

    def obtener_informacion(self):
        return f"{super().obtener_informacion()}, Tipo de Pescado: {self.tipo_pescado}"


def mostrar_informacion_producto(producto):
    print(producto.obtener_informacion())


# La instancias de cada clase
arroz = ProductoAgricola("Arroz", 100, 0.5, "Cereal")
vaca = ProductoGanadero("Vaca", 10, 500, "Bovino")
atun = ProductoPesquero("Atún", 50, 2, "Marino")

# Demostrarcion de encapsulación simple
print(arroz.get_nombre())  # Obtencion del nombre del producto agrícola
arroz.set_nombre("Maíz")  # Cambiar nombre del producto agrícola
print(arroz.get_nombre())  # Verificacion del cambio

# Mostrar la información de cada producto
mostrar_informacion_producto(arroz)
mostrar_informacion_producto(vaca)
mostrar_informacion_producto(atun)

# Calcular valor total de cada producto
print(f"Valor total de arroz: {arroz.calcular_valor_total()}")
print(f"Valor total de vaca: {vaca.calcular_valor_total()}")
print(f"Valor total de atún: {atun.calcular_valor_total()}")



