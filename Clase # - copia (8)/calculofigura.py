from sys import path

path.append("..\\directorio")

from directorio.area import areaCuadrado, areaCirculo, areaRectangulo
from directorio.perimetro import perCadrado, perCirculo, perRectangulo

def main():
    print("--" * 30)
    print("programa para calcular areas y perimetros de figuras geometricas")
    print("--" * 30)
    figura = input("Ingrese el nombre de la figura geometrica")
    if figura.lower()=="circulo":
        areaCirculo()
        perCirculo()
    elif figura.lower() == "Cuadrado":
        areaCuadrado()
        perCadrado()
    elif figura.lower() == "Cuadrado":
        areaRectangulo()
        perRectangulo()    
    else:
        print("no puedo calcular la figura")

if __name__==("__main__"):
    main()



