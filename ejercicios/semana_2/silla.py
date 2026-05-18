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

Silla = Silla ("Metal,aluminio,madera,tela","Al:40cm,An:35cm","Negro","18kg")

Silla.cargarla()
Silla.sentarse()
Silla.aventar()
Silla.voltearla()
Silla.pararse()