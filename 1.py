import numpy as np
print(np.__version__)


a = np.array([1,2,3,4])
# print(a)
# print(a.shape)
# print(a.dtype)
# print(a.ndim)               #dimension
# print(a.size)               #size of array
# print(a.itemsize)           #size in bytes

a[0] = 10
# print(a)


#copying
a = np.array([1,2,3])
b = a       # copyed by reference
b[0] = 12
# print(a, b) # a also changed
c = a.copy()
a[1] = 13
# print(a, b, c)


# check if two arrays are same or not
a = np.array([1,2,3])
b = np.array([1,2,3])
# print(np.allclose(a,b))

# nan and inf
a = np.nan
# print(a)
a = np.inf
# print(a)
# print(np.isnan(a), np.isinf(a))


# delete, append, insert
a = np.array([2,3,4])
a = np.append(a, [8, 9])
print(a)
a = np.insert(a, 3, [5,6,7])
print(a)

