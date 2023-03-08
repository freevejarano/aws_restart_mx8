
students = ["Luis", "Christian", "Mayte"]

"""
for student in students:
    if student == "Luis":
        continue # Saltar una iteración
    print("Hola", student)
"""

# range con un solo argumento va de 0 hasta n, sumando de a 1 (salto)
# range con dos argumentos va de n1 a n2, sumando de a 1 (salto)
# range con tres argumentos va de n1 a n2 con saltos de n3

for i in range(2,10,3):
    print(i)

# IMPRIMIR TODOS LOS NUMEROS PARES DE 0 a 100 INCLUYENDO EL 100

for i in range(101):
    if i % 2 == 0:
        print(i)

for i in range(0, 101, 2):
    print(i)
    
    