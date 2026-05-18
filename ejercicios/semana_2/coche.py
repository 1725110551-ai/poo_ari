class Coche:

    def __init__(self,motor,velocidad_max,seguridad,tipo_de_combustible,capacidad,color,tracción,peso,dimensiones,modalidad):
        self.motor=motor
        self.velocidad_max=velocidad_max
        self.seguridad=seguridad
        self.tipo_de_combustible=tipo_de_combustible
        self.capacidad=capacidad
        self.color=color
        self.tracción=tracción
        self.peso=peso
        self.dimensiones=dimensiones
        self.modalidad=modalidad
        
        print(f"motor:{self.motor}")
        print(f"Velocidad máxima:{self.velocidad_max}")
        print(f"Seguridad:{self.seguridad}")
        print(f"Tipo de combustible:{self.tipo_de_combustible}")
        print(f"Capacidad:{self.capacidad}")
        print(f"Color:{self.color}")
        print(f"Tracción:{self.tracción}")
        print(f"Peso:{self.peso}")
        print(f"Dimensiones:{self.dimensiones}")
        print(f"Modalidad:{self.modalidad}")

        def manejarlo(self):
            print("manejar coche")
        def chocarlo(self):
            print("Chocar coche")
        def encender(self):
            print("Encender coche")
        def apagar(self):
            print("Apagar coche")
        def avanzar(self):
            print("Avanzar coche")

mitsubishi_lancer = Coche("4 cilindros", "200 km/h", "3 bolsas de aire", "gasolina", "5 pasajeros", "personalizable", "delantera", "1.5 toneladas", "L:4.5m, A:1.8m, An:1.4m", "manual")

mitsubishi_lancer.manejarlo()
mitsubishi_lancer.chocarlo()
mitsubishi_lancer.encender()
mitsubishi_lancer.apagar()
mitsubishi_lancer.avanzar()