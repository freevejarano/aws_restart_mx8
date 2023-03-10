import json

# variables para considerar
filename = "username.json"

name = ""

# Manejo de excepciones
try:
    with open(filename, 'r') as r:
        name = json.load(r)
    a = 5/0
except IOError:
    print("Primera vez de registro")
except ZeroDivisionError:
    print("Divides entre 0 y no")
    

if name != "":
    print("Bienvenido del vuelta", name)
else:
    name = input("Hola, cuál es tu nombre? ")
    print("Bienvenido", name)
    
    try:
        with open(filename, "w") as f:
            json.dump(name, f) # Subir en el archivo un json con el nombre
    except IOError:
        print("Hubo un problema escribiendo el archivo")