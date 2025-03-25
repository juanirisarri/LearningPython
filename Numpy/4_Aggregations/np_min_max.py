
import numpy as np

L = np.random.random(10000)  
M = np.random.random((3, 4))


print("\n")
print("----------------------------------")

# print(L)
# print("\n")

print("The max of L is: ", np.max(L))
print("The max of L is: ", L.max())
print("The min of L is: ", np.min(L))
print("The min of L is: ", L.min())

print("----------------------------------")

print(M)
print("\n")
print("The max of each column of M is: ", M.max(axis=0))
print("The min of each row of M is: ",    np.min(M,axis=1))

print("----------------------------------")
print("\n")