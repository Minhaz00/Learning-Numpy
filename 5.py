                # Aggragate functions

import numpy as np
a = [[1, 2, 3, 4], [5, 6, 7, 8]]

# axis = None by default
x = np.sum(a)
print(x)
x = np.mean(a)
print(x)
x = np.max(a)
print(x)
x = np.min(a)
print(x)
x = np.std(a)
print(x)
x = np.var(a)
print(x)


print("\n")

# axis = 1 works row wise
x = np.sum(a, axis=1)
print(x)
x = np.mean(a, axis=1)
print(x)
x = np.max(a, axis=1)
print(x)
x = np.min(a, axis=1)
print(x)
x = np.std(a, axis=1)
print(x)
x = np.var(a, axis=1)
print(x)


print("\n")

# axis = 0 works column wise
x = np.sum(a, axis=0)
print(x)
x = np.mean(a, axis=0)
print(x)
x = np.max(a, axis=0)
print(x)
x = np.min(a, axis=0)
print(x)
x = np.std(a, axis=0)
print(x)
x = np.var(a, axis=0)
print(x)




