
import numpy as np

L = np.array([2, 3, 1, 6, -99, 4, 8, 99 ])


print("\n")
print("----------------------------------")

print("min index: ", np.argmin(L))
print("min index: ", L.argmin())

print("max index: ", np.argmax(L))
print("max index: ", L.argmax())

print("----------------------------------")
print("\n")