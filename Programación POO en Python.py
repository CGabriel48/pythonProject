
#clase creada para definir los parametros a utilizar siendo puesta para lo que seria 1 dia
class dia():

    def __init__(self, dia, temperatura):
        self.__temperatura = temperatura
        self.__dia = dia

    def obtener_dia(self):
        return self.__dia

    def obtener_temperatura(self):
        return self.__temperatura

    def __str__(self):
        return f'{self.__dia}: {self.__temperatura}°C'
#lineas hechas para qeu se regrese la temperatura con el simbolo de grados centigrados


#segunda clase hecha para el calculo del promedio y poder agregar la temperatura en dada dia#
class clima_semanal:
    def __init__(self):
        self.__dias_clima = []

    def agregar_dia(self, dias, temperatura):
        nuevo_dia = dia(dias, temperatura)
        self.__dias_clima.append(nuevo_dia)

    def calcular_promedio_semanal(self):
        if not self.__dias_clima:
            return 0
        total_temperaturas = sum(dia.obtener_temperatura() for dia in self.__dias_clima)
        return total_temperaturas / len(self.__dias_clima)

    def mostrar_dia(self):
        for dia in self.__dias_clima:
            print(dia)

    def __str__(self):
        return "\n".join(str(dia) for dia in self.__dias_clima)


#y las lineas para ejecutar el codigo basado en el de programacion tradicional

def main():
    clima_de_la_semana = clima_semanal()

    print("Ingrese las temperaturas diarias de la semana:")
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    for dia in dias_semana:
        temperatura = float(input(f'Temperatura de {dia}:'))
        clima_de_la_semana.agregar_dia(dia, temperatura)

    print("\nDatos de la semana:")
    clima_de_la_semana.mostrar_dia()

    promedio = clima_de_la_semana.calcular_promedio_semanal()
    print(f"\nEl promedio de temperatura es: {promedio:.2f}ºC")

if __name__ == "__main__":
    main()