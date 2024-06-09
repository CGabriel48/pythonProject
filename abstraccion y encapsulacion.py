print("Hola bienbenido soy")


class Persona:
    def __init__(self, nombre, edad, genero, estatura, cumpleaños):
        self.__nombre = nombre
        self.edad = edad
        self.__genero = genero
        self.altura = estatura
        self.__cumpleaños = cumpleaños

    def hoja_de_presentacion(self):
        print(self.__nombre)
        print("-tengo", self.edad)
        print("-mido", self.altura)
        print("-me identifico como", self.__genero)

    def saludar(self):
        print("hola mucho gusto me llamo")

    def cumplir_años(self):
        print("-y cumplo el", self.__cumpleaños)

    def despedia(self):
        print("nos vemos")

    def irse(self):
        print(self.__nombre, "se fue")


persona1 = Persona("Carlos", "18", "hombre", "1.58", "3 de enero")
persona2 = Persona("Jose", "25", "hombre", "1.65", "4 de junio")

persona1.hoja_de_presentacion()
persona1.cumplir_años()

persona2.saludar()
persona2.hoja_de_presentacion()
persona2.cumplir_años()
persona2.despedia()
persona2.irse()

