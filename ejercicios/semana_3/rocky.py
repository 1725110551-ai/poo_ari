class Perro:

    def __init__(self,peso,nacionalidad,genero,edad_perruna,fecha_de_nacimiento,nombre,raza,estatura,temperatura,color_de_pelaje):
        self.peso=peso
        self.nacionalidad=nacionalidad
        self.genero=genero
        self.edad=edad_perruna
        self.fecha_de_nacimiento=fecha_de_nacimiento
        self.nombre=nombre
        self.raza=raza
        self.estatura=estatura
        self.temperatura=temperatura
        self.color_de_pelaje=color_de_pelaje
        
        print(f"peso:{self.peso}")
        print(f"nacionalidad:{self.nacionalidad}")
        print(f"genero:{self.genero}")
        print(f"edad:{self.edad}")
        print(f"fecha de nacimiento:{self.fecha_de_nacimiento}")
        print(f"nombre:{self.nombre}")
        print(f"raza:{self.raza}")
        print(f"estatura:{self.estatura}")
        print(f"temperatura:{self.temperatura}")
        print(f"color de pelaje:{self.color_de_pelaje}")

    def entrenar(self):
        print("Entrenar a rocky")
    def acariciar(self):
        print("acariciar a rocky")
    def bañar(self):
        print("bañar a rocky")
    def veterinario(self):
        print("llevar a rocky al veterinario")
    def jugar(self):
        print("jugar con rocky")

Rocky = Perro("45 kg", "Estadounidense", "Macho", "26 años", "2023-11-19", "Rocky", "Pitbull americano", "53 cm", "37.8 °C", "cafe con blanco")

Rocky.entrenar()
Rocky.acariciar()
Rocky.bañar()
Rocky.veterinario()
Rocky.jugar()