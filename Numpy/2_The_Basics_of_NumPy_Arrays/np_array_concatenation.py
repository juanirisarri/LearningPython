
# Array Concatenation: combine multiple arrays into one

# np.concatenate([x, y])
# np.vstack([x,grid1])
# np.hstack([y,grid2])


import numpy as np

x = np.array( [1,2,3] )
y = np.array( [3,2,1] )
z = np.array( [99,99,99] )

C1 = np.concatenate([x,y])  # C1 = np.concatenate([x,y], axis=0)
C2 = np.concatenate([x,y,z])



grid1 = np.array( [[1,2,3], [4,5,6]] )
grid2 = np.array( [[10,20,30], [40,50,60]] )
M1 = np.concatenate([ grid1, grid2 ], axis=0 )   # axis = 0 -> añade filas (mantiene el num de colum)
M2 = np.concatenate([ grid1, grid2 ], axis=1 )   # axis = 1 -> añade colum (mantiene el num de filas)


y1 = np.array([[99],[99]])

V1 = np.vstack([x,grid1])   # Vertical stack (x arriba)
H1 = np.hstack([y1,grid2])  # Horizontal stack (y izda)



print("\n")
print("----------------------------------")

print(C1)
print(C2)

print("----------------------------------")

print(M1)
print(M2)

print("----------------------------------")

print(V1)
print(H1)


print("----------------------------------")
print("\n")