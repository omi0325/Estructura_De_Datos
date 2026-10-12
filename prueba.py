from collections import deque

pila=[20,40,50,60,80]
for numero in range(5):
    numero=pila.pop()
    print("salio: ",numero)
print("la pila tiene: ",pila)
print("la nueva pila es ",numero)

cola=deque()
cola.append(45)
cola.append(56)
print(cola)
numero=cola.popleft()
print(cola)

class nodo:
    def __init__(self,dato):
        self.dato=dato
        selft.siguiente=None
        nodo1=nodo(10)
        nodo1.siguiente=nodo2
        
