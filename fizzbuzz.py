"""
Escribe un programa en Python que itere (recorra en un ciclo) los números enteros del 1 al 50. 
Para los múltiplos de tres imprime "Fizz" en lugar del número y para los múltiplos de cinco 
imprime "Buzz". Para los números que son múltiplos de tres y de cinco imprime "FizzBuzz". 
Ejemplo de salida : 
fizzbuzz 
1 
2 
fizz 
4 
buzz
"""


for i in range(1,51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)