
# to access a slice of an array x, use this:
# x[start:stop:step] -> si se omiten:: start=0, stop=-1, step=1 



import numpy as np

x = np.arange(10)
x2 = np.random.randint(10, size=(3, 4)) # Two-dimensional array


print("\n")
print("----------------------------------")

print( x )
print( x[1:3:1] )
print( x[:5] )
print( x[5:] )
print( x[1:3] )
print( x[::2] )
print( x[1::2] )
print( x[:4:2] )

print("----------------------------------")

print( x[::-1] )
print( x[9:0:-2] )
print( x[6::-3] )

print("----------------------------------")

print( x2 )
print("\n")
print( x2[0:2:1 , 1:3:] )
print("\n")
print( x2[1:2: , ::] )   # similar as x2[1 , :] 
print("\n")
print( x2[1 , :] )
print("\n")
print( x2[:: , 1:2:] )   # similar as x2[: , 1]
print("\n")
print( x2[: , 1] )   
print("\n")
print( x2[0:1: , ::2] )
print("\n")
print( x2[::-1 , ::-1] )

print("----------------------------------")

print( x2 )
print("\n")

print( x2[: , 1] ) 
print( x2[1 , :] )  
print( x2[1] )


print("----------------------------------")
print("\n")