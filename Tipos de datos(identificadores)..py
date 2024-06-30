#Primero crear las funciones para calcular las figuras
def calcular_area_rectangulo(base: float, altura: float) -> float:
    area_rectangulo = base * altura
    return area_rectangulo

def calcular_area_circulo(radio: float) -> float:
    PI = 3.14  #al seer un circulo se crea la instancia PI para agregar lo que equivaldria el numero pi
    area_circulo = PI * radio ** 2
    return area_circulo

def calcular_area_triangulo_equilatero(base: float, altura: float) -> float:
    area_equilatero = base * altura / 2
    return area_equilatero

#toca crear una funcion para verificar si el numro que se va a utilisar es valido

def numero_valido(valor: str) -> bool:
    try:
        float(valor)
        return True
    except ValueError:
        return False

# ya finalmente el ejecutor del codigo

def main():

    figura = input("Ingrese la figura para calcular el área (rectángulo/círculo/triangulo): ").strip().lower()

    if figura == "rectángulo" or figura == "rectangulo":
        base = input("Ingrese la base del rectángulo: ")
        altura = input("Ingrese la altura del rectángulo: ")

        if numero_valido(base) and numero_valido(altura):
            base = float(base)
            altura = float(altura)
            area = calcular_area_rectangulo(base, altura)
            print(f"El área del rectángulo es: {area}")
        else:
            print("Error: La base y la altura deben ser números válidos.")

    elif figura == "círculo" or figura == "circulo":
        radio = input("Ingrese el radio del círculo: ")

        if numero_valido(radio):
            radio = float(radio)
            area = calcular_area_circulo(radio)
            print(f"El área del círculo es: {area}")
        else:
            print("Error: El radio debe ser un número válido.")

    if figura == "triangulo" or figura == "triangulo":
        baset = input("Ingrese la base del triangulo: ")
        alturat = input("Ingrese la altura del triangulo: ")

        if numero_valido(baset) and numero_valido(alturat):
            baset = float(baset)
            alturat = float(alturat)
            area = calcular_area_triangulo_equilatero(baset, alturat)
            print(f"El área del triangulo es: {area}")

""" por si nota parecido el codigo del triangulo con el del rectangulo solo es copia y pega del de arriba ya que al ser
este triangulo ipoteticamente equilatero no cambia mucho la manera de calcular el area con la del rectangulo """


    else:
        print("Error: Figura no reconocida. Por favor, ingrese 'rectángulo', 'círculo' o 'traingulo'.")



if __name__ == "__main__":
    main()