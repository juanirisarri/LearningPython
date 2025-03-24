
# Attributes of each array:
# ndim:     number of dimensions
# shape:    size of each dimension
# size:     total number of elements in the array
# dtype:    the data type of the array
# itemsize: lists the size (in bytes) of each array element
# nbytes:   lists the total size (in bytes) of the array



import numpy as np

np.random.seed(0) # seed for reproducibility

x1 = np.random.randint(10, size=6) # One-dimensional array
x2 = np.random.randint(10, size=(3, 4)) # Two-dimensional array
x3 = np.random.randint(10, size=(3, 4, 5)) # Three-dimensional array





print("\n")
print("----------------------------------")

print("x3 dimensions: ", x3.ndim)
print("x3 shape: ",      x3.shape)
print("x3 size: ",       x3.size)
print("x3 type: ",       x3.dtype)
print("x3 itemsize: ",   x3.itemsize)
print("x3 nbytes: ",     x3.nbytes)

print("----------------------------------")
print("\n")



















