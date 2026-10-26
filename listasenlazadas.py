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
Mi_lista=ListasEnlazadas()
Mi_lista.insertar_Nodo(1)
Mi_lista.insertar_Nodo(2)
Mi_lista.insertar_nodo_al_final(56)
Mi_lista.imprimir_lista()