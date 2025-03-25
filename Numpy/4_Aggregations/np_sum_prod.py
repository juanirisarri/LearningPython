
import numpy as np

L = np.random.random(10000)  

#M = np.ones((3,4))
M = np.random.random((3, 4))

Q = np.random.randint(1,3,(2,3))

# for this huge array, sum(L) works too, but it is much more slower than np.sum(L)
# In general sum and np.sum are different !!


print("\n")
print("----------------------------------")
print("np.sum()")
print("\n")

# print(L)
# print("\n")

print("The 'L' sum is: ", np.sum(L))
print("The 'L' sum is: ", L.sum())

print("----------------------------------")

print(M)
print("\n")

print("The 'M' sum is: ", np.sum(M))
print("The 'M' sum is: ", M.sum())
print("The 'M' sum along axis 0 (for each each column) is: ", np.sum(M,axis=0))
print("The 'M' sum along axis 1 (for each each row) is: ", M.sum(axis=1))

print("----------------------------------")
print("----------------------------------")
print("np.prod()")
print("\n")

print(Q)
print("\n")

print("The 'Q' prod is: ", np.prod(Q))
print("The 'Q' prod is: ", Q.prod())
print("The 'Q' prod for each column is: ", Q.prod(axis=0))
print("The 'Q' prod for each row is: ", np.prod(Q,axis=1))


print("----------------------------------")
print("\n")