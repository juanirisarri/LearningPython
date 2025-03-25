
import numpy as np

mean = 2.3
std = 0.2       # var = std^2


N = np.random.normal(mean, std, size=(5,9000000))


print("\n")
print("----------------------------------")

print("Mean = ", N.mean() )
print("Mean of each row = ", np.mean(N,axis=1) )

print("\n")

print("Std = ", np.std(N) )
print("Std of each row = ", N.std(axis=1) )

print("\n")

print("Var = ", N.var() )
print("Var of each row = ", np.var(N,axis=1) )

print("\n")

print("Median = ", np.median(N))
print("Median of each row = ", np.median(N,axis=1) )




print("----------------------------------")
print("\n")