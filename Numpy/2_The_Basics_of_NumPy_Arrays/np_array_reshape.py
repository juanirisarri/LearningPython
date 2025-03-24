
import numpy as np

x1 = np.arange(1,10)
x2 = x1.reshape( (3,3) )
x3 = x1[np.newaxis, :]    # **two-dimensional** row or column vector


print("\n")
print("----------------------------------")

print(x1)
print("\n")
print(x2)

print("----------------------------------")

x2[0,0] = 999  # cambia x2 pero tamb x1

print(x1)
print("\n")
print(x2)

print("----------------------------------")

print(x1)
print("\n")
print(x3)


print("----------------------------------")
print("\n")