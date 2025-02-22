
# Conceptos vistos en de este ejemplo: 
#       - Herencia múltiple: Varias superclases
#       - uso de 'super'



class Vehiculos():   
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



class VElectricos(): 

    def __init__(self, bat):
        self.autonomia = 100
        self.bateria   = bat
        

    def cargarEnergia(self):
        self.bateria = 100
        



class Moto(Vehiculos):  
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

    def __init__(self, marca, modelo,bat):
        super().__init__(marca, modelo)
        self.autonomia = 100
        self.bateria   = bat


    def estado(self):       # Se sobreescribe para incluir la bateria
        super().estado()
        print("Bateria: ", self.bateria)

        
# Queda solucionado el problema. Ahora se puede crear un 
# objeto BiciElectrica con marca, modelo y bateria



# Fin de las clases
#--------------------------------------------------------
#--------------------------------------------------------

print("\n")
miBici = BiciElectrica("Orbea", "X1pro",76)        # No se inicia con un valor de bateria 
miBici.estado()
print("---------------------------------")
miBici.acelerar()
miBici.caballito()
miBici.estado()
print("---------------------------------")
miBici.cargarEnergia()
miBici.estado()
print("\n")






















