# linalg.inv method
import numpy as np
from numpy.linalg import inv

#EXAMPLE 1
A = np.array([[5, 3], [3.5, 5]])

result = inv(A)

print(f'EXAMPLE 1:{result}')

#EXAMPLE 2
B = np.array([[1, 5], [3, 4]])

result = inv(B)

print(f'EXAMPLE 2:{result}')

#EXAMPLE 3
C = np.array([[2, 1], [1,3]])

result = inv(C)

print(f'EXAMPLE 3:{result}')
