
import numpy as np

np.random.seed(0) # seed for reproducibility

x1 = np.random.randint(10, size=6) # One-dimensional array
x2 = np.random.randint(10, size=(3, 4)) # Two-dimensional array
x3 = np.random.randint(10, size=(3, 4, 5)) # Three-dimensional array




print("\n")
print("----------------------------------")

print(x1)
print(x1[0])
print(x1[4])
print(x1[-1])

print("----------------------------------")

print(x2)
print(x2[0,0])
print(x2[2,1])
print(x2[2,-1])

print("----------------------------------")
x2[0,2] = 99
print(x2)

print("----------------------------------")
print(x3)
print(x3[1,1,0])

print("----------------------------------")
print("\n")













































