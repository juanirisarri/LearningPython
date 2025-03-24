
# to copy the data within an array or a subarray: copy() 

import numpy as np

np.random.seed(0) # seed for reproducibility
x2 = np.random.randint(10, size=(3, 4)) # Two-dimensional array


print("\n")
print("----------------------------------")

print(x2)
print("\n")
x2_sub = x2[:2, :2]
print(x2_sub)
print("\n")
x2_sub_copy = x2[:2, :2].copy()
print(x2_sub_copy)


print("----------------------------------")
print("\n")
print("----------------------------------")

x2_sub[1,1] = 999
print(x2_sub)
print("\n")
print(x2)
print("\n")
print(x2_sub_copy)


print("----------------------------------")
print("\n")