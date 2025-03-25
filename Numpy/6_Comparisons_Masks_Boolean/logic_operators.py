
import numpy as np

x = np.array([ 1,2,3,4,5 ])

x2 = np.array([ 5,4,3,2,1 ])

out = (x <= 3)

print("\n")
print("----------------------------------")


print( x < 3)    # Output: [ True  True  False  False  False]   
print(np.less(x,3))
print("\n")
print( out) 
print("\n")
print( x == 3)
print("\n")
print( x != 3)

print("----------------------------------")

print( x <= x2)
print("\n")
print( x != x2)
print("\n")
print( x == x2)

print("----------------------------------")
print("\n")