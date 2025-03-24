
import numpy as np

myList = [1, 4, 2, 5, 3]

myArray1 = np.array([1, 3, 5 , 2])
myArray2 = np.array(myList) 

myArrayWithType = np.array(myList, dtype='float32')

my3DArray = np.array([ [1, 2, 3],[6, 4, 8],[9, 0, 1] ])

print("\n")
print("----------------------------------")
print(myList)
print(myArray1)
print(myArray2)
print(myArrayWithType)
print("\n")
print(my3DArray)
print("----------------------------------")
print("\n")


