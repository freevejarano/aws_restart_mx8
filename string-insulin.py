# guarda la secuencia
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

lsInsulin = "malwmrllpllallalwgpdpaaa"

bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"

aInsulin = "giveqcctsicslyqlenycn"

cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"

insulin = bInsulin + aInsulin

# impresiones de los valores

print("La secuencia de la preproinsulina humana es", preproInsulin)

print("Las cadenas de secuencia son")

print(lsInsulin)

print(bInsulin)

print(aInsulin)

print(cInsulin)


# calcular el peso molecular de la insulina

# crea un diccionario con los pesos
aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
'V': 117.15, 'W': 204.23, 'Y': 181.19} 


# conteo de aminoacidos
aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A', 'C',
'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
'V', 'W', 'Y']}) 

"""
print(aaCountInsulin)
# Dict comprehension
# alternativa
nuevo = {} 
for x in ['A', 'C','D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T','V', 'W', 'Y']:
    nuevo[x] = float(insulin.upper().count(x))

print(nuevo)

# List comprehension
# alternativa
lista = []
for i in range(10):
    lista.append(i**2)

#print(lista)

# equivalencia
# nombre de la lista = [resultado_de_cada_elemento for i in range(10)]
lista2 = [i**2 for i in range(10)]

#print(lista2)

"""

# multiplicar la cuenta de los pesos
molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in
['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',
'S', 'T', 'V', 'W', 'Y']}.values())

"""
print(molecularWeightInsulin)

# alternativa
nuevo = {}

for x in ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T', 'V', 'W', 'Y']:
    nuevo[x] = aaCountInsulin[x] * aaWeights[x]

lista_valores = nuevo.values() 

suma = sum(lista_valores)

print(suma)

"""

print("The rough molecular weight of insulin: " + str(molecularWeightInsulin))

molecularWeightInsulinActual = 5807.63
print("Error percentage: " + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))