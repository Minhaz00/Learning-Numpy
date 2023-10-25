                # Generating arrays
import numpy as np

            # array/ matrix with value = 0
a = np.zeros(4)
b = np.zeros((2, 3))
# print(a)
# print(b)

            # array/ matrix with value = 1
a = np.ones(4)
b = np.ones((3, 3))
# print(a)
# print(b)

            # array/ matrix with value = any
a = np.full(5, 2)
b = np.full((2, 2), 5)
# print(a)
# print(b)

            # square, identity matrix with n * n
a = np.eye(5)
# print(a)

            # array with value = 0 - 9
a = np.arange(10)
# print(a)
a = np.arange(10, 100, 5)
print(a)

            # array with value = 0 to 10 in 5 element
a = np.linspace(0, 10, 5)
# print(a)