import numpy as np
                # solving linear equation

# Linear eqn through Matrix: Ax = B
# therefore x = A^-1 * B

A = np.array([[1, 1], [1.5, 4.0]])
B = np.array([2200, 5050])

x = np.linalg.inv(A).dot(B)     # slow, not accurate
print(x)

x = np.linalg.solve(A, B)       # fast, accurate, preferable
print(x)
