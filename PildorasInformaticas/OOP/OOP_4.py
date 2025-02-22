
# Conceptos vistos en de este ejemplo: 
#       - Herencia múltiple: varias superclases



class Vehiculos():   # Esta es una super clase (superclass) de la cual hereda moto
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelera = False
        self.frena = False


    def arrancar(self):
        self.enMarcha = True


    def acelerar(self):
        self.acelera = True


    def frenar(self):
        self.frena = True


    def estado(self):
        print("Marca: ", self.marca)
        print("Modelo: ", self.modelo)
        print("En marcha: ", self.enMarcha)
        print("Acelera: ", self.acelera)
        print("Frena: ", self.frena)



class VElectricos(): # Esta es una super clase (superclass) de la cual hereda bicicletaElectrica

    def __init__(self, bat):
        self.autonomia = 100
        self.bateria   = bat
        

    def cargarEnergia(self):
        self.bateria = 100
        print("Bateria: ", self.bateria )




class Moto(Vehiculos):  # Esta es una subclase (subclass) de Vehiculo (hereda de ella)
                        # Hereda los constructores, los atributos y métodos de su superclase
                        # Puede sobreescribir los constructores, los atributos y los métodos de su superclase
                        # Puede definir sus propios constructores, atributos y métodos 
    
    hcaballito = "No hago caballito"         # Atributo propio
    
    def caballito(self):                     # Metodo propio
        self.hcaballito = "Hago caballito"

    def estado(self):                        # sobreescribo este metodo heredado
        print("Marca: ", self.marca)
        print("Modelo: ", self.modelo)
        print("En marcha: ", self.enMarcha)
        print("Acelera: ", self.acelera)
        print("Frena: ", self.frena)
        print(self.hcaballito)



class BiciElectrica(Moto, VElectricos):     # Hereda de dos superclases
    pass                                                                                                                    
# Ahora mismo hereda el constructor de la primera superclase solo (Moto). Se soluciona en OOP5.py



# Fin de las clases
#--------------------------------------------------------
#--------------------------------------------------------

print("\n")
miBici = BiciElectrica("Orbea", "X1pro")        # No se inicia con un valor de bateria 
miBici.estado()
print("---------------------------------")
miBici.acelerar()
miBici.caballito()
miBici.estado()
miBici.cargarEnergia()
print("\n")


print("---------------------------------")
print("---------------------------------")
print("\n")

tuBici = BiciElectrica(76)                      # Esto da error
print(tuBici.bateria)
tuBici.cargarEnergia()
print("\n")



















