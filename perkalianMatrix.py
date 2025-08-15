import numpy as np

a = np.array(([1,2], [3,4]))
b = np.ones([2,2])

print("Matrix a: ")
print(a)

print("Matrix b: ")
print(b)

# Perkalian Matrix
c1 = a * b #perkalian biasa
c1 = np.dot(a,b) # perkalian dot aljabar linear
c2 = a.dot(b)

print("Matrix C1: ")
print(c1)

print("Matrx C2: ")
print(c2)
