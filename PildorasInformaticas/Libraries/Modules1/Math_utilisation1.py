
#import Math_module
#import Math_module as MM
#from Math_module import sumar
from Math_module import *


n1 = 5
n2 = 3

print("\n")
print("-----------------------------------")

# Si uso 'import Math_module as MM' ::

# MM.sumar(n1,n2)
# MM.restar(n1,n2)
# MM.multiplicar(n1,n2)



# Si uso 'from Math_module import sumar' ::

# sumar(n1,n2)



# Si uso 'from Math_module import *' ::

sumar(n1,n2)
restar(n1,n2)
multiplicar(n1,n2)


print("-----------------------------------")
print("\n")