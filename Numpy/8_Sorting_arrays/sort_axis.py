
import numpy as np

x = np.random.randint(1,100, size=(3,4) )



print("\n")
print("----------------------------------")

print(x)
print("\n")

print(np.sort(x, axis=0))  # sort every column
print("\n")

print(np.sort(x, axis=1)) # sort every row

print("----------------------------------")
print("\n")









