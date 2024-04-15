from Empleado import *

class Administrativo(Empleado):
    def __init__(self,tdc,n,s,t,c):
        super().__init__(tdc,n,s,t)
        self.cargo = c

    def ver(self):
        t1 = super().ver()
        t1 += "\nCargo                 :" + self.cargo
        t1 += "\n=================="
        return t1
        
