
# Conceptos vistos en de este ejemplo: 
#       - polimorfismo



class Coche():
    def desplaz(self):
        print("Uso 4 ruedas")


class Moto():
    def desplaz(self):
        print("Uso 2 ruedas")


class Camion():
    def desplaz(self):
        print("Uso 6 ruedas")




def desplazamiento(vehiculo):
    vehiculo.desplaz()              # llama al desplaz en función del objeto que le entre


# Fin de las clases
#--------------------------------------------------------
#--------------------------------------------------------


miCoche = Coche()
miMoto = Moto()
miCamion = Camion()

print("\n")

desplazamiento(miCoche)
desplazamiento(miMoto)
desplazamiento(miCamion)

print("\n")






















