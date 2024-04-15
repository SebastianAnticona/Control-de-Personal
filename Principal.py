from Pila import *
from Validacion import *

from Arquitecto import *
from Administrativo import *
from Ingeniero import *


def datos(d):
    nombre = valtexto("Ingrese su nombre: ")
    salario = valReal("Ingrese su salario: ")
    telefono = valtelefono("Ingrese su número telefónico(Celular): ")
    if d == "Arquitecto":
        comision = valcomision("Ingrese su comisión(%): ")
        cantidad_de_proyectos = valEntero("Ingrese la cantidad de proyectos: ")

        dd = Arquitecto(d,nombre,salario,telefono,comision,cantidad_de_proyectos)
    
    elif d == "Administrativo":
        cargo = valtexto("Ingrese su cargo: ")

        dd = Administrativo(d,nombre,salario,telefono,cargo)
    
    else:
        especialidad = valtexto("Ingrese su especialidad: ")
        experiencia = valEntero("Ingrese sus años de experiencia: ")

        dd = Ingeniero(d,nombre,salario,telefono,especialidad,experiencia)  
    return dd

def agregarEmp(pila):
        d = valtp("Desea registrar Arquitecto, Administrativo o Ingeniero: ")
        
        a = datos(d)
        pila.poner(a)
        
        print(pila.nombreC, "Registrado correctamente")
        return pila

def eliminarEmp(pila):
    pila.sacar()
    print("Eliminación realizada con éxito")
    return pila

def listarEmp(pila):
    print("Lista de " + pila.nombreC +"s\n==================")
    for emp in pila.mostrar():
        print(emp.ver())

def menu(pila):
    while True:
        print("=================\nMenú de opciones\n=================")
        print("1.- Registrar ")
        o = "1-2"
        n = 2
        if len(pila.mostrar()) > 0:
            print("2.- Eliminar ")
            print("3.- Listar ")
            o = "1-4"
            n = 4
        print(f"{n}.- Salir ")
        try:
            m_o = int(input(f"Elija opción<{o}>: "))
            if m_o == 1:
                pila = agregarEmp(pila)
            elif m_o == n:
                print("Programa Terminado :D")
                break
            elif n == 4:
                if m_o == 2:
                    pila = eliminarEmp(pila)
                elif m_o == 3:
                    listarEmp(pila)
            else:
                print("'ERROR' Opción no válida")
        except ValueError:
            print("'ERROR' Ingrese la númeración correspondiente")

#programa principal
pilaEmp = Pila("Empleado")
menu(pilaEmp)