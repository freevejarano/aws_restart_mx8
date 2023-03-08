userReply = input("Necesitas entregar un paquete? Si o No → ").capitalize()

if userReply == "Si":
    print("Podemos ayudarte con la entrega")
else:
    print("Vuelve cuando lo necesites")
    exit() # Es una función para salir de la ejecución del programa


userReply = input("Qué le gustaría comprar estampas, sobre o hacer una copia? ").lower()

if userReply == "estampas":
    print("Tenemos muchos diseños")
elif userReply == "sobre":
    print("Tenemos muchos sobres")
elif userReply == "copia":
    copies = input("Cuántas copias quiere sacar? ")
    print("Se sacara el número de copias:", copies)
else:
    print("Gracias vuelva pronto")