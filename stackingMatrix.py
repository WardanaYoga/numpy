import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])
print(a+b)

aMatrix = np.zeros((2,3))
bMatrix = np.ones ((2,3))


# STACKING MATRIX / MENUMPUK MATRIX

c = np.hstack((a,b))
cMat = np.hstack((aMatrix,bMatrix))
print(c)
print(cMat)

d = np.vstack((a,b))
dMat = np.vstack((aMatrix,bMatrix))
print(d)
print(dMat)
