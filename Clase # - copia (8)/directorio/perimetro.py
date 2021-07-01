def perCadrado():
    lado = int(input("Ingrese el valor del Lado :  "))
    return print("el area del Cuadrado es", 4 * lado)

def perRectangulo():
    base= int(input("ingrese el valor de la base  : "))
    altura= int(input("Ingrese el valor de altura  :"))
    return print("el perimetro del Rectangulo es ", (2 * base), (2 * altura))

def perCirculo():
    radio= int(input("Ingrese el valor del Radio  :"))
    __pi= 3.1416
    return print("el area del circulo es ",2 *  __pi * radio)

if __name__==("__main__"):
    print("estoy en la funcion principal")
    perCirculo()
    perCadrado()
    perRectangulo()
else:
    print("en este momento me comporto como un modulo")
