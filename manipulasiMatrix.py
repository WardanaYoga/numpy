import numpy as np

a = np.array(([1,2,3],[4,5,6]))
print("Matrix a: ", a.shape)
print(a)

# Transpose Matrix
print('Transpose Matrix dari a: ')
print(a.transpose())
print(np.transpose(a)) # cara lain
print(a.T) # cara lain
print("Matrix a dengan ukuran: ", a.shape)

# Flatten array, vector baris
print('flatten matrix a: ')
print(a.ravel())
print(np.ravel(a))
print("Matrix a dengan ukuran: ", a.shape)

# reshape matrix
print('reshape matrix a: ')
print(a.reshape(3,2))
print(a.reshape(6,1))
print("Matrix a dengan ukuran: ", a.shape)

# resize matrix
print("resize matrix a: ")
a.resize(3,2)
print(a)
print("Matrix a dengan ukuran: ", a.shape)
