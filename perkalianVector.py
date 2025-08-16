import numpy as np

a = np.array([1, 3, 2]) # x y z
b = np.array([2, 1, 2])

# Perkalian dot
c = np.dot(a,b)

# Perkalian cross

d = np.array([1,2,0])
e = np.array([2,1,0])

f = np.cross(d,e)
f1 = np.cross(e,d)

print(c)
print(f)
print(f1)
