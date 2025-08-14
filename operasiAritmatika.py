import numpy as np

# LIST PYTHON
a = [1,2,3,4,5]
b = [6,7,8,9,10]

# Penjumlahan python
hasil_penjumlahan = a + b
# hasil_pengurangan = a - b
# hasil_perkalian = a * b
# hasil_pembagian = a / b


# array numpy
anp = np.array([1,2,3,4,5])
bnp = np.array([6,7,8,9,10])

# Elemenwise Operation 
hasil_array_penjumlahan = anp + bnp
hasil_array_pengurangan = anp - bnp
hasil_array_perkalian = anp * bnp
hasil_array_pembagian = anp/bnp
hasil_array_kuadrat = anp**2


# Multi Dimensi
c = np.array([(1,2,3) , (4,5,6)])
d = np.array([(7,8,9) , (-1,-2,-3)])

hasil_multidimensi_penjumlahan = c + d
hasil_multidimensi_perkalian = c * d


print(hasil_penjumlahan)
# print(hasil_pengurangan)
# print(hasil_perkalian)
# print(hasil_pembagian)

print(hasil_array_penjumlahan)
print(hasil_array_pengurangan)
print(hasil_array_perkalian)
print(hasil_array_pembagian)
print(hasil_array_kuadrat)
print(hasil_multidimensi_penjumlahan)
print(hasil_multidimensi_perkalian)
