
# One important—and extremely useful—thing to know about array slices is that they
# return views rather than copies of the array data

# Es decir, si defino x2_sub = x2[:2, :2] y modifico x2_sub, también se modifica x2 !!!

import numpy as np


np.random.seed(0) # seed for reproducibility
x2 = np.random.randint(10, size=(3, 4)) # Two-dimensional array




print("\n")
print("----------------------------------")

print(x2)
print("\n")
x2_sub = x2[:2, :2]
print(x2_sub)

print("----------------------------------")
print("\n")
print("----------------------------------")

x2_sub[1,1] = 999
print(x2)
print("\n")
print(x2_sub)


print("----------------------------------")
print("\n")