myList = []

for i in range(10):
    myList.append(i + 1)

print(myList)

myList.reverse()
print(myList)
myList.sort()
print(myList)
ubicacion = myList.index(3)
print(ubicacion)
myList.pop()
print(myList)
myList.pop(0)
print(myList)