from numpy import random
import numpy as np
"""
x = random.randint(10,size=(2,10))
print(x)

"""
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))#p=probability

print(x)

arr = np.array([1, 2, 3, 4, 5])

print(random.permutation(arr))
