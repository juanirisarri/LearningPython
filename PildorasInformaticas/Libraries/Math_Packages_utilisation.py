
# Si este script está en la carpeta 'PildorasInformaticas' debería ser:
# from Libraries.Packages.Math_package.Math_module_A import *

from Packages.Math_package.Math_module_A import *
from Packages.Math_package.Math_module_B import *

#from Packages.Math_package import Math_module_A as MMA
#from Packages.Math_package import Math_module_B as MMB


n1 = 5
n2 = 3
n3 = 4.8

print("\n")
print("-----------------------------------")


# Si uso 'from Packages.Math_package.Math_module_A import *' :

sumar(n1,n2)
restar(n1,n2)
multiplicar(n1,n2)
redondear(n3)



# Si uso 'from Packages.Math_package import Math_module_A as MMA' :

# MMA.sumar(n1,n2)
# MMA.restar(n1,n2)
# MMA.multiplicar(n1,n2)
# MMB.redondear(n3)

print("-----------------------------------")
print("\n")