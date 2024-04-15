
class Empleado():
    def __init__(self,tdc,n,s,t):
        self.tipo_de_clase = tdc
        self.nombre = n
        self.salario = s
        self.telefono = t 
    
    def ver(self):
        t1 =  "Clase                 : " + self.tipo_de_clase
        t1 += "\nNombre                : " + self.nombre
        t1 += f"\nSalario               : S/.{self.salario:.2f}"
        t1 += "\nTeléfono              : " + str(self.telefono)
        return t1
        
         