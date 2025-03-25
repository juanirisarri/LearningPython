
import numpy as np

x1 = np.random.normal(0,1,size=(1,5))
x2 = np.arange(1,6)

x = np.vstack([x2,x1])



print("\n") 
print("----------------------------------")

# print(x1)
# print(x2)
print(x)
print("----------------------------------")

print("Positive and greater than 1: ", np.sum( (x[1,:] > 0) &  (np.abs(x[1,:]) > 1) ))

print("Positive or greater than +-1: ", np.sum( (x[1,:] > 0) |  (np.abs(x[1,:]) > 1) ))

print("Or Positive or in first 3 columns (not both): ", np.sum( (x[0,:]<=3) ^ (x[1,:] > 0) )  )

print("Not positive and not in first 3 columns: ", np.sum( ~ ( (x[0,:]<=3) | (x[1,:] > 0) ) ) )




print("----------------------------------")
print("\n") 