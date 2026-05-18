class Libro:

    def __init__(self,portada,numero_de_hojas,color_de_portada,tipos_de_letras,autor,clasificacion,editorial,indice,dedicatoria,año_de_publicacion):
        self.portada=portada
        self.numero_de_hojas=numero_de_hojas
        self.color_de_portada=color_de_portada
        self.tipos_de_letras=tipos_de_letras
        self.autor=autor
        self.clasificacion=clasificacion
        self.editorial=editorial
        self.indice=indice
        self.dedicatoria=dedicatoria
        self.año_de_publicacion=año_de_publicacion
        
        print(f"portada:{self.portada}")
        print(f"Número de hojas:{self.numero_de_hojas}")
        print(f"Color de portada:{self.color_de_portada}")
        print(f"Tipos de letras:{self.tipos_de_letras}")
        print(f"Autor:{self.autor}")
        print(f"Clasificación:{self.clasificacion}")
        print(f"Editorial:{self.editorial}")
        print(f"Índice:{self.indice}")
        print(f"Dedicatoria:{self.dedicatoria}")
        print(f"Año de publicación:{self.año_de_publicacion}")

    def leer(self):
        print("Leer el libro")
    def aventarlo(self):
        print("Aventarlo el libro")
    def aprender(self):
        print("Aprender con el libro")
    def imaginar(self):
        print("Imaginar")
    def pisar(self):
        print("Pisar el libro")

los_hornos_de_hitler = Libro("portada.jpg","260","gris claro","garamond, times roman","Olga Lenyel","autobiografía,testimonio","Editorial Diana","la deportación, la selección","victimas del holocausto","1947")

los_hornos_de_hitler.leer()
los_hornos_de_hitler.aventarlo()
los_hornos_de_hitler.aprender()
los_hornos_de_hitler.imaginar()
los_hornos_de_hitler.pisar()