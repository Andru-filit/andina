largestNumber = -99999999
numbrer = int(input("introduszca un numero o escriba -1 para detener: "))

while numbrer != -1:
    if numbrer > largestNumber:
        largestNumber = numbrer
numbrer = int(input("introduzca un numero o escriba -1 para detener "))
print("Elnumero mas grande es: ", largestNumber)
