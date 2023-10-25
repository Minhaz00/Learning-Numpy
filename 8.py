                # Random numbers
import numpy as np

a = np.random.random(5)
# print(a)


b = np.random.randint(1, 12, 10)
# print(b)
b = np.random.randint(10, 20, size=(3,3))
# print(b)


c = np.random.randn(1000)
# print(c.mean(), c.var())


a = np.random.choice(5, size=10)
# print(a)
a = np.random.choice([44,34,12,5,6], size=(2,3))
# print(a)