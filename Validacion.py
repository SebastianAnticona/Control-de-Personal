
def valtp(m):
    while True:
        tipo = input(m).capitalize()
        if tipo == "Arquitecto" or tipo == "Administrativo" or tipo == "Ingeniero" :
            return tipo
        else:
            print("'ERROR' Clase no encontrada")

def valtexto(m):
    while True:
        texto = input(m)
        c=0
        for t in texto:
            if not t.isalpha() and t != " " : 
                c = 1
        if c != 1 :
            return texto
        else:
            print("'ERROR' Debe ingresar solo texto")

def valEntero(m):
    while True:
        numero = input(m)
        if numero.isdigit():
            return int(numero)
        else:
            print("'ERROR' Debe ingrese solo números enteros")

def valReal(m):
    while True:
        try:
            numero = float(input(m))
            if numero < 0:
                print("'ERROR' Valor negativo")
            else:
                break
        except ValueError:
            print("'ERROR' Debe ingresar un número real")
    return numero

def valtelefono(m):
    while True:
        try:
            numero = int(input(m))
            if numero > 899999999 and numero < 1000000000 :
                return numero
            else:
                print("'ERROR' El número debe contar con 9 dígitos")
        except ValueError:
            print("'ERROR' Debe ingresar un número de teléfono(celular)")

def valcomision(m):
    while True:
        try:
            numero = int(input(m))
            if numero > 0 and numero < 101:
                return numero
            else:
                print("'ERROR' Valor fuera del rango")
        except ValueError:
            print("'ERROR' Debe ingrese solo números enteros")