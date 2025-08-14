import numpy as np

# MEMBUAT VECTOR
a = np.array ([1,2,3,4,5])
print(a)

b = np.array([1.5, 2.5, 3.5, 5, 6, 7])
print(b)

# MEMBUAT VECTOR DENGAN RANGE
c = np.arange(1,10,2)
print(c)

# MEMBUAT LINEAR SPACE
d = np.linspace(1,10,4)
print(d)

# MEMBUAT ARRAY MULTIDIMENSI / MATRIX
e = np.array([(1,2,3) , (4,5,6)])
print(e)

# MATRIX DENGAN NILAI NOL
f = np.zeros([2,5])
print(f)

# MATRIX DENGAN NILAI SATU
g = np.ones(5)
print(g)

# MATRIX DENGAN NILAI IDENTITAS
h1 = np.identity(5)
print(h1)

h2 = np.eye(5)
print(h2)
