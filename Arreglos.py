"""#Declarando un arreglo
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

#Eliminamos un elemento del arreglo usando el nombre
fruta=["Manzana","Fresa","Sandia","Mango","Melon","Platano"]
fruta.pop(4)
print(fruta)
fruta.remove("Manzana")
print(fruta) 
arreglo=[]
print(arreglo)
n=int(input("Ingrese el tamaño del arreglo: "))
print(n)
print("El arreglo es: ", arreglo)
arreglo =[0]*n
for i in range(n):
         dato= int (input("Ingrese un numero: "))
         arreglo[i]=dato
         print(arreglo)"""
n=15
arreglo=[0]*n
for i in range(n):
 t=int(input("Ingrese el numero: "))
arreglo.append(t)
print(arreglo)
for i in range(n):
 if arreglo[i]% 5 !=0:
    arreglo[i]=arreglo[i] + (5-arreglo[i]%5)
print(arreglo)
for i in range(15):
 print(arreglo[i])