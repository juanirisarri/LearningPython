
import numpy as np

x = np.random.normal(0, 1, size=(3,4))

pos = (x>0)   # boolean array
neg = (x<0)


print("\n")
print("----------------------------------")

print(x)
print("\n")

print("Positive: ", np.count_nonzero(pos))
print("Negative: ", np.sum(neg))                  # True == +1

print("Negative in each column: ", np.sum(neg, axis=0 ))               

print("All positive in each row: ", np.all(pos, axis=1) )
print("Any positive: ", np.any(pos) )

print("----------------------------------")
print("\n") 