class Vehiculo:
    combustible = ""
    caballos = 0
    def __init__(self, combustible, caballos):
        self.combustible = combustible
        self.caballos = caballos

    def imprimir(self):
        print("Combustible: " + self.combustible + "Caballos: " + self.caballos)
        print("Pienso: " + self.combustible + "Gramos: " + self.caballos)

