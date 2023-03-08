# Para importar un módulo uso import + nombre del módulo
# Puedo usar un alias importación + as + alias
import csv # Manejo de archivos formato csv
import copy # Hacer copias de colecciones


# Definiendo un diccionario que funciona como plantilla
myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

#print(myVehicle.items())

for key, value in myVehicle.items(): pass
    #print(key,value)

# Lista de diccionarios que se declar vacía
myInventoryList = []


# Manejo de archivos

# qué archivo abrir, cómo lo abro, que codificación tiene, etc
# default el modo de abrirlo es de lectura
# r lectura
# w escritura
# a añadir / agregar

with open('car_fleet.csv') as csvFile:
    # Hago lectura del csv
    csvReader = csv.reader(csvFile, delimiter=',')
    
    lineCount = 0
    
    for row in csvReader:
        if lineCount == 0:
            print(f"Las columnas son: {', '.join(row)}\n")
            lineCount += 1
        else:
            #print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')
            # Utilizo la plantilla
            currentVehicle = copy.deepcopy(myVehicle)
            
            # Asignar valores al diccionario
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7] 
            
            # Agregar el nuevo diccionario a la lista
            myInventoryList.append(currentVehicle)
            
            lineCount += 1


for car in myInventoryList:
    for key, value in car.items():
        print(f"{key} : {value}")
    print("-"*30)