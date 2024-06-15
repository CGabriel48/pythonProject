
# funcion hecha para agregar los dias de la semana y la temperatura

def ingresar_temperaturas_diarias():

    temperaturas = []
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    print("Ingrese la __temperatura:")

    for dia in dias:
        temperatura = float(input(f'Temperatura de {dia}: '))
        temperaturas.append(temperatura)

    return temperaturas

#y funcion para promediar las temperaturas

def promedio_semanal(temperaturas):

    if len(temperaturas) == 0:
        return 0

    total_temperaturas = sum(temperaturas)
    promedio = total_temperaturas / len(temperaturas)
    return promedio

# lineas para ejecutar las funciones

def main():
    # Ingreso de temperaturas diarias
    temperaturas = ingresar_temperaturas_diarias()

    # Calcular el promedio semanal
    promedio = promedio_semanal(temperaturas)

    # Mostrar resultado
    print(f'\nEl promedio de temperaturas de la semana es: {promedio:.2f}')

# Ejecución del programa
if __name__ == "__main__":
    main()

