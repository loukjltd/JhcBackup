import numpy as np

originalArray = np.arange(0, 60, 5)
originalArray = originalArray.reshape(3, 4)
print(originalArray)
print('\n')

cOrderArray = originalArray.copy(order='C')
print(cOrderArray)
for x in np.nditer(cOrderArray):
    print(x, end=', ')
print('\n')

fOrderArray = originalArray.copy(order='F')
print(fOrderArray)
for x in np.nditer(fOrderArray):
    print(x, end=', ')
