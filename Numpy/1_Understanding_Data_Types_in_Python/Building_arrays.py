
import numpy as np

# Create a length-10 integer array filled with zeros:
A = np.zeros( (1,10), dtype=int)    # (10) works too 


# Create a 3x3 identity matrix
A2 = np.eye(3)

# Create a 3x5 floating-point array filled with 1:
B = np.ones( (3,5), dtype=float )


# Create a 3x5 array filled with 3.14
C = np.full( (3,5) , 3.14 )


# Create an array filled with a linear sequence: 
# Starting at 0, ending at 20 (not included), stepping by 2
D = np.arange(0,20,2)


# Create an array of five values evenly spaced between 0 and 1
E = np.linspace(0, 1, 5)


# Create a 3x3 array of UNIFORMLY distributed (random values between 0 and 1)
F = np.random.random((3,3))


# Create a 3x3 array of NORMALLY distributed random values
# with mean 0 and standard deviation 1
G = np.random.normal( 0, 1, (3,3) )


# Create a 3x3 array of random integers in the interval [0, 10)
H = np.random.randint( 0, 10, (3,3) )



# Create an uninitialized array of three integers
# The values will be whatever happens to already exist at that memory location
I = np.empty(3)










print("\n")
print("----------------------------------")

print(A)
print("\n")
print(A2)
print("\n")
print(B)
print("\n")
print(C)
print("\n")
print(D)
print("\n")
print(E)
print("\n")
print(F)
print("\n")
print(G)
print("\n")
print(H)
print("\n")
print(I)
print("\n")


print("----------------------------------")
print("\n")








