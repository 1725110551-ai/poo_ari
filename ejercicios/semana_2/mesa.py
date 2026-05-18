class Mesa:

    def __init__(self,material,medidas,color,peso):
        self.material=material
        self.medidas=medidas
        self.color=color
        self.peso=peso

        print(f"Material de fabricación:{self.material}")
        print(f"Medidas de la mesa:{self.medidas}")
        print(f"Color de la mesa:{self.color}")
        print(f"Peso de la mesa:{self.peso}")

    def cargarla(self):
        print("Cargar la mesa")
    def sentarse(self):
        print("Sentarse en la mesa")
    def aventar(self):
        print("Aventar la mesa")
    def voltearla(self):
        print("Voltear la mesa")
    def pararse(self):
        print("Pararse sobre la mesa")

Mesa_de_salon = Mesa ("Metal,madera","Al:40cm,An:155cm","blanca","14kg")

Mesa_de_salon.cargarla()
Mesa_de_salon.sentarse()
Mesa_de_salon.aventar()
Mesa_de_salon.voltearla()
Mesa_de_salon.pararse()