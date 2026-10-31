class Nodo:
    def __init__(self,numero):
        self.numero=numero
        self.siguiente=None
class ListasEnlazadas:
    def __init__(self):
        self.cabeza=None
        #metodo para insertar un nodo al inicio
    def insertar_Nodo(self,numero):
        nuevo_nodo=Nodo(numero)
        if (self.cabeza is None):
            self.cabeza=Nodo(numero)
            return
        nuevo_nodo.siguiente=self.cabeza
        self.cabeza=nuevo_nodo
        #metodo para insertar un nodo al final
    def insertar_nodo_al_final(self,numero):
        nuevo_nodo=Nodo(numero)
        if(self.cabeza==None):
            self.cabeza=nuevo_nodo
            return
        actual=self.cabeza
        while(actual.siguiente):
            actual=actual.siguiente
        actual.siguiente=nuevo_nodo
    #Metodo para imprimir nuestra lista enlazada
    def imprimir_lista(self):
        actual=self.cabeza
        while(actual):
            print(actual.numero,"=>",end=" ")
            actual=actual.siguiente
        print("None")
# Método para eliminar el nodo al inicio
    def eliminar_inicio(self):
        if self.cabeza is None:
            print("La lista esta vacia, no hay nada que eliminar")
            return
        self.cabeza = self.cabeza.siguiente
    # Método para eliminar el nodo al final
    def eliminar_final(self):
        if self.cabeza is None:
            print("La lista esta vacia, no hay nada que eliminar")
            return
        if self.cabeza.siguiente is None:
            self.cabeza = None
            return
        actual = self.cabeza
        while actual.siguiente.siguiente:
            actual = actual.siguiente
        actual.siguiente = None
Mi_lista=ListasEnlazadas()
Mi_lista.insertar_Nodo(1)
Mi_lista.insertar_Nodo(2)
Mi_lista.insertar_nodo_al_final(56)
Mi_lista.imprimir_lista()
print("Eliminando al inicio:")
Mi_lista.eliminar_inicio()
Mi_lista.imprimir_lista()
print("Eliminando al final:")
Mi_lista.eliminar_final()
Mi_lista.imprimir_lista()