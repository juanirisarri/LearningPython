
import numpy as np

def selection_sort(x):
    for i in range(len(x)):
        swap = i + np.argmin(x[i:])
        (x[i], x[swap]) = (x[swap], x[i])
    return x


x = [2,1,0,5,3,-99]

x_sorted = x.copy()
x_sorted = selection_sort(x_sorted)


print("\n")
print("----------------------------------")

print(x)
print("\n")
print(x_sorted)

print("\n")
print("Using numpy's np.sort() and x.sort(): ")
print(np.sort(x))

x.sort()
print(x)

print("----------------------------------")
print("\n")




