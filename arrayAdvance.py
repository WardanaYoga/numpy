import numpy as np

# MEMBUAT MATRIX DENGAN TIPE DATA TERTENTU
a = np.array(([1,2,3], [4,5,6]), dtype = bool)

# MEMBUAT MATRIX DENGAN MENGGUNAKAN FUNCTION
def kuadrat(baris, kolom):
    return kolom ** 2

def jumlah(baris, kolom):
    return (kolom + baris)

b = np.array([0,1,2,3,4,5,6,7,8,9])
bfunc = np.fromfunction(kuadrat, (1,10), dtype = int ) # fungsi, ukuran matrix, tipe data

cfunc = np.fromfunction(jumlah, (4,4), dtype = float)


# MEMBUAT ARRAY ATAU MATRIX DENGAN ITERASI / ITERABLE

iterable = (x*x for x in range(5))
d = np.fromiter(iterable, dtype = int)

# MULTITYPE ARRAY
dtipe = [('nama', 'S255'), ('tinggi', int)]

data = [('ucup', 150),
       ('otong', 160),
       ('mario', 180)]

e = np.array(data, dtype = dtipe)

# Display
print(kuadrat(1,5)) # 1 merupakan kolom dan 5 adalah step
print(bfunc)
print(cfunc)
print(d)
print(data)
print(e)
print(e[0])
