import random

print("Bienvenido vamos a adivinar tu número")
print("Yo pienso un número y tú lo adivinas")


number = random.randint(1,10)

isGuessRight = False

while isGuessRight != True:
    guess = int(input("Adivina un número del 1 al 10: "))
    
    if guess == number:
        print("Bien, adivinaste el número")
        isGuessRight = True
    else:
        print("El número no es correcto, intenta de nuevo")