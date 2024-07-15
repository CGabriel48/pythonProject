class Archivo:
    def __init__(self, nombre_archivo):

        #Constructor que inicializa el nombre del archivo y abre el archivo en modo de escritura.

        self.nombre_archivo = nombre_archivo
        print(f"Abriendo el archivo: {self.nombre_archivo}")
        self.archivo = open(self.nombre_archivo, 'w')

    def escribir(self, contenido):

        #Método para escribir contenido en el archivo.

        if self.archivo:
            self.archivo.write(contenido)
        else:
            print("El archivo no está abierto.")

    def __del__(self):

        #Destruidor que cierra el archivo al destruir el objeto.

        if self.archivo:
            print(f"Cerrando el archivo: {self.nombre_archivo}")
            self.archivo.close()


class Cliente:
    def __init__(self, nombre_cliente):

        #Constructor que inicializa el nombre del cliente y simula la apertura de una conexión.

        self.nombre_cliente = nombre_cliente
        print(f"Conectando con el cliente: {self.nombre_cliente}")
        # Aquí se simula la apertura de una conexión
        self.conexion = True

    def enviar_datos(self, datos):

        #Método para enviar datos al cliente.

        if self.conexion:
            print(f"Enviando datos a {self.nombre_cliente}: {datos}")
        else:
            print("La conexión no está activa.")

    def __del__(self):

        #Destruidor que simula el cierre de la conexión al destruir el objeto.

        if self.conexion:
            print(f"Desconectando del cliente: {self.nombre_cliente}")
            self.conexion = False


# uso
def main():
    # Crear una instancia de la clase Archivo y escribir en él
    archivo = Archivo("ejemplo.txt")
    archivo.escribir("Hola, este es un archivo de prueba.")

    # Crear una instancia de la clase Cliente y enviar datos
    cliente = Cliente("Cliente1")
    cliente.enviar_datos("Hola, cliente!")

    # Los objetos se destruyen automáticamente al final del bloque


if __name__ == "__main__":
    main()
