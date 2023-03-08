print("Python tiene tres tipos de datos numéricos: int, float y complex")

#### COMENTARIO 
# numeral ignora solo la linea

"""
Esto es un comentario multilinea
puede ser " o ' pero iguales
"""


# Consideraciones de las variables
# letras y números y _
# no son válidos los caracteres especiales
# no es válido que la variable empiece por un número,
# pero puede contenerlo en cualquier otra posición
# minúsculas
# case sensitive

# NO es válido usar espacios
# método camello (Camel) → miVariable miNombre
# método por _ → mi_variable 

### Entero int ###

myValue = 1

print(myValue)

print(type(myValue))

print("-"*20)

### Float ###

myValue = 3.14

print(myValue)

print(type(myValue))

print(str(myValue) + " es de tipo "+ str(type(myValue)))

print("{} es de tipo {}".format(myValue, type(myValue)))

print(f"{myValue} es de tipo {type(myValue)}")

print("-"*20)

### Complex ###

myValue = 5j

print(myValue)

print(type(myValue))

print(str(myValue) + " es de tipo "+ str(type(myValue)))

print("-"*20)

### Booleano bool ###

myValue = False

print(myValue)

print(type(myValue))

print(str(myValue) + " es de tipo "+ str(type(myValue)))