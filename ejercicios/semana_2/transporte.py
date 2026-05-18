class Transporte:

    def __init__(self,color,marca,modelo,dimensiones,velocidad_maxima,combustible,tipo,seguridad,capacidad,peso):
        self.color=color
        self.marca=marca
        self.modelo=modelo
        self.dimensiones=dimensiones
        self.velocidad_maxima=velocidad_maxima
        self.combustible=combustible
        self.tipo=tipo
        self.seguridad=seguridad
        self.capacidad=capacidad
        self.peso=peso
        
        print(f"Color:{self.color}")
        print(f"Marca:{self.marca}")
        print(f"Modelo:{self.modelo}")
        print(f"Dimensiones:{self.dimensiones}")
        print(f"Velocidad máxima:{self.velocidad_maxima}")
        print(f"Combustible:{self.combustible}")
        print(f"Tipo:{self.tipo}")
        print(f"Seguridad:{self.seguridad}")
        print(f"Capacidad:{self.capacidad}")
        print(f"Peso:{self.peso}")

    def manejarlo(self):
        print("manejar combi")
    def chocarlo(self):
        print("Chocar combi")
    def encender(self):
        print("Encender combi")
    def apagar(self):
        print("Apagar combi")
    def avanzar(self):
        print("Avanzar combi")

combi = Transporte("gris claro","GMC","C200","L:5.91m, A:2.28m, An:1.95m","120 km/h","diesel","van","3 bolsas de aire, frenos ABS","11 pasajeros","2.5 toneladas")

combi.manejarlo()
combi.chocarlo()
combi.encender()
combi.apagar()
combi.avanzar()