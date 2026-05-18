class Silla:

    def __init__(self,material,medidas,color_respaldo,peso):
        self.material=material
        self.medidas=medidas
        self.color_respaldo=color_respaldo
        self.peso=peso

        print(f"Material de fabricación:{self.material}")
        print(f"Medidas de la silla:{self.medidas}")
        print(f"Color del respaldo:{self.color_respaldo}")
        print(f"Peso de la silla:{self.peso}")

    def cargarla(self):
        print("Cargar la silla")
    def sentarse(self):
        print("Sentarse en la silla")
    def aventar(self):
        print("Aventar la silla")
    def voltearla(self):
        print("Voltear la silla")
    def pararse(self):
        print("Pararse sobre la silla")

Silla_de_salon = Silla ("Metal,aluminio,madera,tela","Al:40cm,An:35cm","Negro","18kg")

Silla_de_salon.cargarla()
Silla_de_salon.sentarse()
Silla_de_salon.aventar()
Silla_de_salon.voltearla()
Silla_de_salon.pararse()