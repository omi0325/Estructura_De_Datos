#Declarando un arreglo
numeros = [10,20,30,40,50]
#imprimir un elemento especifico del arreglo 
print (numeros[2])
#Reasignación
numeros[3]=35
print (numeros)
#Agrega un nuevo valor al final del arreglo
numeros.append(60)
print (numeros)
#Elimina cualquier valor en el arreglo
numeros.remove(35)
print (numeros)
#Elimina cualquier posicion en el arreglo
numeros.pop(4)
print(numeros)

fruta=["Manzana","Fresa","Sandia","Mango","Melon","Platano"]
fruta.pop(4)
print(fruta)
fruta.remove("Manzana")
print(fruta)
