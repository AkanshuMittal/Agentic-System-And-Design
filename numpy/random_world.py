import numpy as np 

print(np.random.rand(5))
    
print(np.random.rand(2,3))

print()

print(np.random.randn(5))

print(np.random.randn(2,3))

print()

print(np.random.randint(1,10))

print(np.random.randint(1,10, size=(2,3)))

print(np.random.randint(0,20, (5,5)))

print()

print(np.random.choice([1,2,3,4,5], size=3))

print(np.random.choice([1,2,3,4,5], size=(2,3)))

#print(np.random.choice([1,2,3,4,5], size=(2,3), replace=False))

print(np.random.choice([1,2,3,4,5], size=(2,3), replace=True))

print()




