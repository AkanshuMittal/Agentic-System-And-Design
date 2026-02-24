import numpy as np 

a = np.array([10, 20, 30, 40, 50])

b = a[1:3]

print(b)

b[1] = 999

print(b)

print(a)


### Learn about copy in numpy 

d = np.array([1,2,3,4])

e = d[1:3].copy()

e[0] = 999

print(d)

print(e)