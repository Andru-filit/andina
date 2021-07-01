def esUntriangulo(a, b, c):
    return a+b > c and b + c > a and c + a > b

a=float(input("Ingrese la La longitud del primer lado: "))
b=float(input("Ingrese la La longitud del segundo lado: "))
c=float(input("Ingrese la La longitud del terce lado: "))

if esUntriangulo (a, b, c):
    print("felicitaciones, puede ser un triangulo. ")

else:
        print("no puede ser un triangulo. ")
         
