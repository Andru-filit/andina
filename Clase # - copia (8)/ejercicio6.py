loteria=[]
for i in range(5):
    numero=int(input("ingrese los numeros ganadores"+ str(i) +"de la loteria:  "))
    loteria.append(numero)
print("Los numero de la loteria ganadores son:", sorted(loteria))