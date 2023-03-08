### LISTAS ###

# Secuencia
# Cualquier variedad de tipos
# Permite repetidos
# Es mutable ###
# contiene los elementos en [] separados por ,

# Posiciones representadas en indices
# 0,1,2,3

# En los indices positivos se cuenta desde 0 hasta el tamaño de la lista -1
# Si uso indices negativos se accede de atrás para adelante desde 1
#           0       1       2
fruits = ["Grape", "Apple", "Coco"]


print(fruits)

fruits[0] = True

print(f"Fruits es {type(fruits)} el primer elemento es {type(fruits[0])}")

print(fruits.index("Coco"))

print("-"*30)

### TUPLA ###

# Una lista aburrida
# ES INMUTABLE
# Se declara con () y se separa sus elementos con ,

colors = ("Blue", "Red", "Yellow")

print(colors[0])

print("-"*30)

### Diccionario ###
# similitud encuentro una palabra y su significado
# Key , value
# Mutable
# No admite repetidos → Sobreescribir
# Se declara con {} se separa por ,
# cada item se compone de key : value

# Key son strings (casi siempre, ojalá siempre) o números → es única
# Value puede ser cualquier tipo

records = {"Luis":100, "José": 95, "Irene": 97}

print(records)

print(records["Luis"])