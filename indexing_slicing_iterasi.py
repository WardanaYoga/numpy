import numpy as np

a = np.arange(10)**2

print(a)

# Mengambil nilai
print('elemen ke 1 daari a adalah', a[0])
print('elemen ke 7 dari a adalah', a[6])
print('elemen ke terakhir dari a adalah', a[-1])



# SLICING
print('element dari 1 - 6 adalah', a[0:6])
print('element dari 4 - akhir', a[3:])
print('element dari awal - 5', a[:5])


# ITERASI
for i in a:
    print('value sama dengan ', i)
