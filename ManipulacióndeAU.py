#numeros= [10,20,30,40,50]
#numeros[2]=100
#numeros.append([60,70])
#numeros.insert(2,25)
#print(numeros)
#numeros= [10,20,30]
#numeros[len(numeros):]=[40]
#print(numeros[3:])
#calificaciones=[70,85,90,65]
#aqui agregamos el 95 con un append de esta forma se agrega al final del arreglo
#calificaciones.append(95)
#aqui ocupamos un insert para posicionar el 80 entre el 85 y 90
#calificaciones.insert(2,80)
#imprimimos todo el arreglo
#print(calificaciones)
#colores=["Azul","Amarillo","Rosa","Negro"]
#pusimos un append para que este independiente los valores nuevos con el arreglo original
#colores.append(["Verde","Morado","Rojo"])
#print(colores)
#aqui imprimimos nada mas la posicion 3 donde se ubica negro
#print(colores[3])
numeros=[10,20,30,40]
#ingresamos el 95 entre el 20 y el 30 
numeros.insert(2,95)
#agregamos al final el numero 50
numeros.append(50)
#despues del 50 se agrega el numero 67
numeros.append(67)
#se imprime todo el arreglo
print(numeros)
#se imprime el numero 95 en la posicion 2
print(numeros[2])
#se imprime el numero 67 en la posicion 6
print(numeros[6])