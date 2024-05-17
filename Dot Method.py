#DOT METHOD
import numpy as np

#EXAMPLE 1
x = np.array([[8.1, 3.7], [4.9, 8.1]])
y = np.array([[1, 2], [3, 4]])

result = np.dot(x,y)

print(f'EXAMPLE no2:{result}')

#EXAMPLE 2
x2 = np.array([[4, 2], [3, 2]])
y2 = np.array([[5, 4], [7, 8]])

result = np.dot(x2, y2)

print(f"Example no2: {result}")

#EXAMPLE 3
x3 = np.array([[9, 2], [2, 9]])
y3 = np.array([5, 7])

result = np.dot(x3, y3)

print(f"Example no3: {result}")
