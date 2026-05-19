class Alumno:

    def __init__(self,peso,nacionalidad,genero,edad,fecha_de_nacimiento,nombre_completo,matricula,estatura,nombre_carrera,cuatrimestre):
        self.peso=peso
        self.nacionalidad=nacionalidad
        self.genero=genero
        self.edad=edad
        self.fecha_de_nacimiento=fecha_de_nacimiento
        self.nombre_completo=nombre_completo
        self.matricula=matricula
        self.estatura=estatura
        self.nombre_carrera=nombre_carrera
        self.cuatrimestre=cuatrimestre
        
        print(f"peso:{self.peso}")
        print(f"nacionalidad:{self.nacionalidad}")
        print(f"genero:{self.genero}")
        print(f"edad:{self.edad}")
        print(f"fecha de nacimiento:{self.fecha_de_nacimiento}")
        print(f"nombre completo:{self.nombre_completo}")
        print(f"matricula:{self.matricula}")
        print(f"estatura:{self.estatura}")
        print(f"nombre de la carrera que cursa:{self.nombre_carrera}")
        print(f"cuatrimestre:{self.cuatrimestre}")

    def reprobar(self):
        print("Reprobar al alumno")
    def aprobar(self):
        print("Aprobar al alumno")
    def baño(self):
        print("darle permiso al alumno para ir al baño")
    def examen(self):
        print("Hacer examen al alumno")
    def nivelación(self):
        print("realizar nivelación al alumno")

Alejandro = Alumno("70 kg", "Mexicano", "Masculino", "18", "2007-05-04", "Alejandro", "1725110551", "1.73 m", "Tics", "tercer cuatrimestre")

Alejandro.reprobar()
Alejandro.aprobar()
Alejandro.baño()
Alejandro.examen()
Alejandro.nivelación()