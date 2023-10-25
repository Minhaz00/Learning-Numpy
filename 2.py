# List vs numpy array

import numpy as np
l = [1, 2, 3, 4]               # a list
a = np.array([1, 2, 3, 4])     # numpy array
# print(l, a)

# 1 =>
# in list we can append element / concat list
# but in numpy array we can't append element

l = l + [6]
l.append(7)
# print(l)

a = a + np.array(5)     # Adds 5 to all the previous elements
# print(a)


# 2 =>
# in list multiplication works on number of element
# whereas in array  multiplication works on elements itself

l2 = [2, 3, 5, 6]
l2 = l2 * 2
# print(l2)

a2 = np.array([2, 3, 4])
a2 = a2 * 2
# print(a2)

# 3. =>
# dot product of lists vs arrays
l3 = [1, 2, 3]
l4 = [4, 5, 6]
dot1 = 0
for i in range(len(l3)):
    dot1 += l3[i] * l4[i]
print(dot1)

ar1 = np.array(l3)
ar2 = np.array(l4)
dot2 = np.dot(ar1, ar2)         # method 1
dot3 = ar1 @ ar2                # method 2
dot4 = (ar1 * ar2).sum()        # method 3
print(dot2)
print(dot3)
print(dot4)



# ==========some operations on array elements
a = np.sqrt(a) # gives sqrt of every element
a = np.log(a) # gives log of every element
# print(a)


