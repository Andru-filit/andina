diccionario ={
    "clave1":234,
    "clave2":True,
    "clave3":"valor 1",
    "clave4":[1,2,3,4]
}
print(diccionario)
print(type(diccionario))
print(len(diccionario))
print(diccionario["clave1"])
print(diccionario.keys())
print(sorted(diccionario.keys()))
print(diccionario.items())
print(diccionario.values())
diccionario[4]="Color"
print(diccionario)
diccionario["clave4"]='999999999'
print(diccionario)
del diccionario["clave1"]
print(diccionario)
print(diccionario.popitem())
print(diccionario)
print(diccionario.clear())
print(diccionario)

