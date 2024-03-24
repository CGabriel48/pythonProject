# Creamos el diccionario con información personal ficticia
informacion_personal = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Quito",
}

# Accedemos al valor asociado con la ciudad y lo modificamos
informacion_personal["ciudad"] = "Puyo"

# Agregamos una nueva valor que represente la profesión de la persona
informacion_personal["profesion"] = "Ingeniero"

# Verificamos si la clave "telefono" existe y, si no, la agregamos
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "123456789"

# Eliminamos la clave "edad" del diccionario
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimimos el diccionario resultante
print("Diccionario final:")
print(informacion_personal)
