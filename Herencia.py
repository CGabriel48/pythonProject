class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.vida = vida
        self.defensa = defensa

    def atributos(self):
        print(self.nombre, ":", sep="")
        print("-fuerza:", self.fuerza)
        print("-inteligencia:", self.inteligencia)
        print("-vida:", self.vida)
        print("-defensa:", self.defensa)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.defensa = self.defensa + defensa
        self.inteligencia = self.inteligencia + inteligencia

    def esta_vivo(selfs):
        return selfs.vida > 0

    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")



class arquero(Personaje):


    def __init__(self, nombre, fuerza,inteligencia, defensa, vida, arco):
        super().__init__(nombre, fuerza,inteligencia,defensa,vida)
        self.arco = arco

    def seleccione_un_arma(self):
        opcion = int(input("elige un arma, (1) arco oxidado daño+2, (2) arco de madera daño+3"))
        if opcion == 1:
            self.arco = 2
        elif opcion == 2:
            self.arco = 3
        elise:\
            print("seleccione una de las opciones disponibles")

    def atributos(self):
        super().atributos()
        print("arma", self.arco)





class tanque(Personaje):
  def __int__(self, nombre, fuerza, inteligencia, defensa, vida, escudo):
      super().__int__(nombre, fuerza, inteligencia, defensa, vida)
      self.escudo = escudo

  def atributos(self):
    super().atributos()
    print("escudo", self.escudo)


Max = tanque("Max", 5, 10, 20, 150)
Sin_clase = Personaje("Samus", 10, 10, 10, 100)
Lilia = arquero("Lilia", 5, 15,5,50, 0)

