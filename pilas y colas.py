from collections import deque
cola = deque()
repetir = "1"
while repetir == "1":
    opcion = 0
    while opcion != 4:
        print("MENU DE COLAS")
        print("1. Insertar cola")
        print("2. Borrar en cola")
        print("3. Listar cola")
        print("4. Salir")
        opcion = int(input("Elige una opcion: "))
        if opcion == 1:
            numero = int(input("Ingresa un numero: "))
            cola.append(numero)
            print("Numero agregado")
        elif opcion == 2:
            if len(cola) > 0:
                numero = cola.popleft()
                print("Numero eliminado:", numero)
            else:
                print("La cola esta vacia")
        elif opcion == 3:
            if len(cola) > 0:
                print("Elementos de la cola:")
                for numero in cola:
                    print(numero)
            else:
                print("La cola esta vacia")
        elif opcion == 4:
            print("Saliendo del menu")
        else:
            print("Opcion incorrecta")
    repetir = input("Deseas ejecutar nuevamente? (si(1)/no(2)): ")
print("Programa terminado")


pila = []
repetir = "1"
while repetir == "1":
    opcion = 0
    while opcion != 4:
        print("MENU DE PILAS")
        print("1. Insertar en pila")
        print("2. Borrar en pila")
        print("3. Listar pila")
        print("4. Salir")
        opcion = int(input("Elige una opcion: "))
        if opcion == 1:
            numero = int(input("Ingresa un numero: "))
            pila.append(numero)
            print("Numero agregado")
        elif opcion == 2:
            if len(pila) > 0:
                numero = pila.pop()
                print("Numero eliminado:", numero)
            else:
                print("La pila esta vacia")
        elif opcion == 3:
            if len(pila) > 0:
                print("Elementos de la pila:")
                for numero in pila:
                    print(numero)
            else:
                print("La pila esta vacia")
        elif opcion == 4:
            print("Saliendo del menu")
        else:
            print("Opcion incorrecta")
    repetir = input("Deseas ejecutar nuevamente? (si(1)/no(2)): ")
print("Programa terminado")