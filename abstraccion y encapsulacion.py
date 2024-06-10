print("Hola bienbenido soy")


class Persona:
    def __init__(self, nombre, edad, genero, estatura, cumpleaños):
        self.nombre = nombre
        self.edad = edad
        self.__genero = genero
        self.altura = estatura
        self.__cumpleaños = cumpleaños

    def hoja_de_presentacion(self):
        print(self.nombre)
        print("-tengo", self.edad)
        print("-mido", self.altura)
        print("-me identifico como", self.__genero)

    def saludar(self):
        print("hola mucho gusto me llamo", self.nombre)

    def cumplir_años(self):
        print("-y cumplo el", self.__cumpleaños)

    def despedia(self):
        print("nos vemos")

    def irse(self):
        print(self.nombre, "se fue")


persona_1 = Persona("Carlos", "18", "hombre", "1.58", "3 de enero")
persona_2 = Persona("Jose", "25", "hombre", "1.65", "4 de junio")

#este codigo fue hecho en base al que nos enseño en clases con algunas acciones extras tuve
#problemas con el poliformismo asi que no lo agrege mil dsiculpas
