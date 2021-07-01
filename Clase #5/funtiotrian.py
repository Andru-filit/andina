def unTriangulo (a, b, c):
    if a + b <= c and b +c <= a and c + a <= b:
        return False
    
print(unTriangulo(1, 1, 1))
print(unTriangulo (1, 1, 3))