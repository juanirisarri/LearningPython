
import numpy as np

x = np.random.normal(0, 1, size=(1,30))

mask_pos = x[x>0]

print("\n") 
print("----------------------------------")

print(x)
print("\n") 
print(mask_pos)    # array 1D que guarda los elementos positivos de x por orden



print("----------------------------------")
print("\n") 