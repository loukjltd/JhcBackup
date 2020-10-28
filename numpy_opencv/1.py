import numpy as np

list1 = list(range(0, 9))

arr1 = np.array(list1)
arr2 = arr1.reshape(3, 3)

print(arr1)
print(arr2)