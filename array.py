import numpy as np
"""
a = np.array([5,6,7,8])
x = a[[True,True,False,True]]

for y in x:
    print('y = '+ str(y))
"""

arr = np.array([41, 42, 43, 44])
filter_arr = []

for element in arr :
    if element > 43:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
new1 = arr[filter_arr]

print('show = '+ str(new1))