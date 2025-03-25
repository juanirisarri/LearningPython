
import numpy as np

x = np.random.randint(0,5,size=(3,4))


row_ind = 1
col_ind = [2,0,1]

mask = np.array([ 1,0,1,0], dtype=bool)    # 1==True 

print("\n")
print("----------------------------------")

print(x)
print("\n")

print(x[row_ind, col_ind])
print("\n")

print(x[:2, col_ind])     # fancy indexing with slicing
print("\n")

print(x[row_ind, mask])   # fancy indexing with masking


print("----------------------------------")
print("\n")

