numbers = [1, 2, 3, 4, 5]
print(numbers)
numbers[2] = int(input("Digite el nuevo número central: "))
print(numbers)
del numbers[4]
print(numbers)
print("Longitud:", len(numbers))