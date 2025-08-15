import numpy as np

a = np.floor(np.random.randn(1,6) * 10)

print(a)
print('nilai maks dari a: ', a.max())
print('posisi max dari a:', a.argmax())
print('nilai min dari a:', a.min())
print('posisi min dari a:', a.argmin())

print('mengurutkan nilai a: ')
print(np.sort(a))

print('mengurutkan berdasarkan argumen a: ')
print(np.argsort(a))

print('-----------------')

b = np.floor(np.random.randn(2,2) * 10)

print(b)
print('nilai maks dari b: ', b.max())
print('posisi max dari b:', b.argmax())
print('nilai min dari b:', b.min())
print('posisi min dari b:', b.argmin())

print('mengurutkan nilai b: ')
print(np.sort(b))

print('mengurutkan berdasarkan argumen a: ')
print(np.argsort(b))

print('------------------')
dtipe = [('nama', 'S10'), ('tinggi', int)]
data = [('ucup', 150),
       ('otong', 170),
       ('mario', 180)]

c = np.array(data,dtype = dtipe)
print(c)

print('mengurutkan berdasarkan tinggi')
print(np.sort(c, order = 'tinggi'))

print('mengurutkan berdasarkan nama')
print(np.sort(c, order = 'nama'))
