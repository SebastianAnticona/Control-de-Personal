from Empleado import *

class Arquitecto(Empleado):
    def __init__(self,tdc,n,s,t,c,ctp):
        super().__init__(tdc,n,s,t)
        self.comision = c
        self.cantidad_de_proyectos = ctp

    def ver(self):
        t1 = super().ver()
        t1 += f"\nComisión              : {self.comision:.0f}%"
        t1 += "\nCantidad de Proyectos : " + str(self.cantidad_de_proyectos)
        t1 += "\n=================="
        return t1
        