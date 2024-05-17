#FLATTEN METHOD
import numpy as np

#EXAMPLE 1
array = np.array([[5, 2, 8], [6, 9, 2]])

result = array.flatten()
print(f'EXAMPLE 1:{result}')

#EXAMPLE 2

array2 = np.array([[[2, 1], [8, 2]], [[4, 1], [9, 8]]])

result = array.flatten()
print(f'EXAMPLE 2:{result}')

#EXAMPLE 3

x = np.array([[1, 2], [3, 2]])
y = np.array([[7, 3], [9, 8]])

z = np.dot(x, y)

result = z.flatten()
print(f'EXAMPLE 3:{result}')
