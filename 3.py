import numpy as np

a = np.array([[1,2,3], [4,5,6], [7,8,8]])
# print(a)
# print(a.shape)

# ===============printing 2nd row
# print(a[1])
# print(a[1, :])

# ===============printing an element
# print(a[1][2])
# print(a[1,2])

# ================printing 2nd column
# print(a[:, 1])

# ================ printing 1st 2 element of 2nd row
# print(a[1, 0:2])

# ================transpose of an array
# print(a.T)

# ================inverse matrix
# print(np.linalg.inv(a))

# ================determinant of matrix
# print(np.linalg.det(a))


# ===============diagonal of a matrix
# print(np.diag(a))


# ============== bool index
bool_index = a > 5
print(bool_index)
print(a[bool_index])        # showing only true indexed elements

b = np.where(a > 4, a, -1)    # if a[i] > 4 show a[i] else -1
print(b)


# ============= fancy indexing
ar = np.array([1,2,3,4,5,6])
ind = [1,3,4]
print(ar[ind])


#============== show all the even numbers in the array
even = np.argwhere(ar%2==0).flatten()
print(ar[even])



