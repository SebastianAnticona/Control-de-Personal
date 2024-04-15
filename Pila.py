class Pila():
    def __init__(self,n):
        self.lista = []
        self.nombreC = n
        
    def poner(self, x):
        self.lista = self.lista + [x]
        #self.lista.append(x)

    def sacar(self):
        if not self.vacia():
            del self.lista[-1]

    def tope(self):
        if not self.vacia():
            x = self.lista[-1]
            return x

    def mostrar(self):
        return self.lista

    def vacia(self):
        return len(self.lista) == 0
