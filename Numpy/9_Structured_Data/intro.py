
import numpy as np


categories = ('name', 'age', 'weight' )
formats    = ( (np.str_,10) , np.int_, np.float64 )

data = np.zeros(4, dtype = {'names':categories, 'formats':formats} )


name = ['Alice', 'Bob', 'Cathy', 'Doug']
age = [25, 45, 37, 19]
weight = [55.0, 85.5, 68.0, 61.5]


data['name'] = name
data['age'] = age
data['weight'] = weight


print("\n")
print("----------------------------------")

print(data)
print("----------------------------------")
print(data[2])
print("----------------------------------")
print(data['age'])
print("----------------------------------")
print( data[data['age'] < 30]['name'] )
print("----------------------------------")
print( data[data['age'] < 30])
print("----------------------------------")
print("\n")