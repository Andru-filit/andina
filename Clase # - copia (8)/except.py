try:
    x= int(input("Ingrese un numero:  "))
    y = 1 / x
    print(y)

except ZeroDivisionError:
    print("No puedes dividir entre ceron, lo siento. ")
except ValueError:
    print("Debes ingresar un valor entero. ")

print("FIN")