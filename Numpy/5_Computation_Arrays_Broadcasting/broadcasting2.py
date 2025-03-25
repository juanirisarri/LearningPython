
import numpy as np

# RULE 1:
# If the two arrays differ in their number of dimensions, the shape of the
# one with fewer dimensions is padded with ones on its leading (left) side.

a = np.array([1,2,3])
M = np.ones((4,3))

print("\n")
print("----------------------------------")

print("M = ", M)
print("\n")
print("a = ", a)
print("----------------------------------")

print("M+a = ", M+a)

print("----------------------------------")
print("\n")