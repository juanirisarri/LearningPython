

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
                        
    hcaballito = "No hago caballito"         
    
    def caballito(self):                     
        self.hcaballito = "Hago caballito"

    def estado(self):                       
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

        



























