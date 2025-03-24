
import numpy as np


# np.split(x, [sp1, sp2])       spi == index of the split point i 
# np.hsplit( grid, [sp1 sp2] )
# np.vsplit( grid, [sp1 sp2] ) 

x = np.array([ 1, 2, 3, 99, 99, 3, 2, 1  ])
grid = np.arange(16).reshape( (4,4) )


x1,x2,x3 = np.split(x,[3,5]) # x1 goes from index=0 to index=3 (not included)

x4,x5,x6 = np.hsplit(x,[3,5])

left,right = np.hsplit( grid, [2] ) 

upper,lower = np.vsplit(grid, [2])



print("\n")
print("----------------------------------")

print(x)
print(x1)
print(x2)
print(x3)

print("----------------------------------")

print(x)
print(x4)
print(x5)
print(x6)

print("----------------------------------")

print(grid)
print("\n")
print(left)
print("\n")
print(right)
print("\n")
print(upper)
print("\n")
print(lower)


print("----------------------------------")
print("\n")