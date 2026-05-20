class Mesa:

    def __init__(self,material,medidas,color,peso,fecha_de_fabricacion,marca,cantidad_de_patas,num_max_de_personas,resistencia):
        self.material=material
        self.medidas=medidas
        self.color=color
        self.peso=peso
        self.fecha_de_fabricacion=fecha_de_fabricacion
        self.marca=marca
        self.cantidad_de_patas=cantidad_de_patas
        self.num_max_de_personas=num_max_de_personas
        self.resistencia=resistencia

        print(f"Material de fabricación:{self.material}")
        print(f"Medidas de la mesa:{self.medidas}")
        print(f"Color de la mesa:{self.color}")
        print(f"Peso de la mesa:{self.peso}")
        print(f"Fecha de fabricación:{self.fecha_de_fabricacion}")
        print(f"Marca de la mesa:{self.marca}")
        print(f"Cantidad de patas de la mesa:{self.cantidad_de_patas}")
        print(f"Número máximo de personas que pueden sentarse en la mesa:{self.num_max_de_personas}")
        print(f"Resistencia de la mesa:{self.resistencia}")

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

Mesa_de_salon = Mesa ("Metal,madera","Al:40cm,An:155cm","blanca","14kg","2023-11-19","IKEA","4","6","100 kg")

Mesa_de_salon.cargarla()
Mesa_de_salon.sentarse()
Mesa_de_salon.aventar()
Mesa_de_salon.voltearla()
Mesa_de_salon.pararse()