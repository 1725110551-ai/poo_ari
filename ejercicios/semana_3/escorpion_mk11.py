class Personaje_videojuego:

    def __init__(self,peso,nacionalidad,genero,edad,fecha_de_nacimiento,armas,poderes,raza,color_de_skin,bando):
        self.peso=peso
        self.nacionalidad=nacionalidad
        self.genero=genero
        self.edad=edad
        self.fecha_de_nacimiento=fecha_de_nacimiento
        self.armas=armas
        self.poderes=poderes
        self.raza=raza
        self.color_de_skin=color_de_skin
        self.bando=bando
        
        print(f"peso:{self.peso}")
        print(f"nacionalidad:{self.nacionalidad}")
        print(f"genero:{self.genero}")
        print(f"edad:{self.edad}")
        print(f"fecha de nacimiento:{self.fecha_de_nacimiento}")
        print(f"armas:{self.armas}")
        print(f"poderes:{self.poderes}")
        print(f"raza:{self.raza}")
        print(f"color de skin:{self.color_de_skin}")
        print(f"bando:{self.bando}")

    def seleccionarlo(self):
        print("Seleccionar a escorpion")
    def luchar(self):
        print("Luchar contra escorpion")
    def armamento(self):
        print("Usar armamento de escorpion")
    def golpearl(self):
        print("Golpear con escorpion")
    def avanzar(self):
        print("Avanzar con escorpion")

escorpion = Personaje_videojuego("70 kg", "Estadounidense", "Masculino", "30", "1993-05-15", "Katanas", "Control de tierra", "Humano", "Amarillo", "Protector de la Tierra")

escorpion.seleccionarlo()
escorpion.luchar()
escorpion.armamento()
escorpion.golpearl()
escorpion.avanzar()