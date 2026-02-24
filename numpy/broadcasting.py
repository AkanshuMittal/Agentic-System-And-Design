import numpy as np 

## 1D array broadcasting
a = np.array([1,2,3])
print(a + 10)


## 2D array broadcasting
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(b + 10)

c = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
vector = np.array([10,20,30])

print(c + vector)


mat = np.array([1,2])
vec = np.array([2])

print(mat + vec)