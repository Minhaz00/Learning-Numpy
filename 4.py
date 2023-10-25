#                       reshaping
import numpy as np

a = np.arange(1, 7)
#           creates a new array a of size 6
# print(a)
# print(a.shape)

#           reshape 1D array into 2D matrix
# print(a.reshape(3, 2))

#           reshape into n:1 or 1:n matrix
b = a[:, np.newaxis]
c = a[np.newaxis, :]
# print(b.shape)
# print(b)
# print(c.shape)
# print(c)


# concat array
ar1 = np.array([[1, 2], [3, 4]])
ar2 = np.array([[5, 6]])
ar3 = np.concatenate((ar1, ar2))
# print(ar3)

ar3 = np.concatenate((ar1, ar2.T), axis=1)
# print(ar3)

ar3 = np.concatenate((ar1, ar2), axis=None)
# print(ar3)


# another way to concat
ar1 = [1, 2, 3]
ar2 = [4, 5, 6]

x = np.hstack((ar1, ar2))       # stack horizontally 1D
# print(x)
x = np.vstack((ar1, ar2))       # stack vertically 2D
# print(x)


# add elements to every row
a = np.array([[1, 2, 3], [1, 1, 1], [2, 2, 3]])
b = np.array([[1, 1, 1]])
x = a + b
# print(x)

# split array
a = np.array([[1,2,3],
             [4,5,6],
             [7,8,9],
             [10,11,12]])
print(np.split(a, 3, axis=1)) # split into 3 array col-wise
print(np.split(a, 2, axis=0)) # split into 2 2D array row-wise

