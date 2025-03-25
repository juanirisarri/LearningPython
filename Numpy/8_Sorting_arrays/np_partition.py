
import numpy as np

#x = np.random.randint(1,100, 100)
x = np.array([7, 2, 3, 1, 6, 5, 4])
x2 = np.random.randint(1,100, (3,5))
K = 2

print("\n")
print("----------------------------------")

print(x)
print("\n")

print(np.partition(x,K))

print("----------------------------------")

# print(x2)
# print("\n")

# print(np.partition(x2,K, axis=1))
# print("\n") 
#print(np.partition(x2,K, axis=1))

print("----------------------------------")
print("\n")