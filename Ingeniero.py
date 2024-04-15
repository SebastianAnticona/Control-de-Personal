from Empleado import *

class Ingeniero(Empleado):
    def __init__(self,tdc,n,s,t,e,ade):
        super().__init__(tdc,n,s,t)
        self.especialidad = e
        self.experiencia = ade
    
    def ver (self):
        t1 = super().ver()
        t1 += "\nEspecialidad          : " + self.especialidad
        t1 += "\nAños de Experiencia   : " + str(self.experiencia)
        t1 += "\n=================="
        return t1
        