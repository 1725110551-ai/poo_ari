class Silla:

    def __init__(self,material,medidas,color_respaldo,peso,marca,fecha_de_fabricacion,resistencia,color_asiento,cantidad_de_patas,ajustable):
        self.material=material
        self.medidas=medidas
        self.color_respaldo=color_respaldo
        self.peso=peso
        self.marca=marca
        self.fecha_de_fabricacion=fecha_de_fabricacion
        self.resistencia=resistencia
        self.color_asiento=color_asiento
        self.cantidad_de_patas=cantidad_de_patas
        self.ajustable=ajustable

        print(f"Material de fabricación:{self.material}")
        print(f"Medidas de la silla:{self.medidas}")
        print(f"Color del respaldo:{self.color_respaldo}")
        print(f"Peso de la silla:{self.peso}")
        print(f"Marca de la silla:{self.marca}")
        print(f"Fecha de fabricación:{self.fecha_de_fabricacion}")
        print(f"Resistencia de la silla:{self.resistencia}")
        print(f"Color del asiento:{self.color_asiento}")
        print(f"Cantidad de patas:{self.cantidad_de_patas}")
        print(f"Es ajustable?:{self.ajustable}")

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

Silla_de_salon = Silla ("Metal,aluminio,madera,tela","Al:40cm,An:35cm","Negro","18kg","IKEA","2023-11-19","150 kg","Gris","4","NO")

Silla_de_salon.cargarla()
Silla_de_salon.sentarse()
Silla_de_salon.aventar()
Silla_de_salon.voltearla()
Silla_de_salon.pararse()