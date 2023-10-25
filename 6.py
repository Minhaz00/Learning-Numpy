                    # datatypes
import numpy as np

# we can set custom type irrespective of data in the array
a = np.array([1.2, 3.12])
print(a)
print(a.dtype)

a = np.array([1.2, 3.12], dtype=np.int64)
print(a)
print(a.dtype)

a = np.array([1.2, 3.12], dtype=np.int32)
print(a)
print(a.dtype)

a = np.array([1.2, 3.12], dtype=np.float32)
print(a)
print(a.dtype)

