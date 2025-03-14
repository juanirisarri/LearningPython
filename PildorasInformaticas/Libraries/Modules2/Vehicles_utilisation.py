
#import Vehicles_module as VM
from Vehicles_module import *

print("\n")
print("-----------------------------------")

# Si uso 'import Vehicles_module as VM' :

# miCoche = VM.Vehiculos("Mazda", "MX5")
# miCoche.estado()
# print("-----------------------------------")
# miCoche.acelerar()
# miCoche.estado()


# Si uso 'from Vehicles_module import *' :

miCoche = Vehiculos("Mazda", "MX5")
miCoche.estado()
print("-----------------------------------")
miCoche.acelerar()
miCoche.estado()



print("-----------------------------------")
print("\n")