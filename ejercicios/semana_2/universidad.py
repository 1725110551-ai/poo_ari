class Universidad:

    def __init__(self,logo,oferta_educativa,localidad,sistema_informativo,modalidad,servicios,ubicación,talleres,cantidad_salones,rector):
        self.logo=logo
        self.oferta_educativa=oferta_educativa
        self.localidad=localidad
        self.sistema_informativo=sistema_informativo
        self.modalidad=modalidad
        self.servicios=servicios
        self.ubicación=ubicación
        self.talleres=talleres
        self.cantidad_salones=cantidad_salones
        self.rector=rector

        print(f"Logotipo de la universidad:{self.logo}")
        print(f"Oferta educativa:{self.oferta_educativa}")
        print(f"Localidad:{self.localidad}")
        print(f"Sistema de la uni:{self.sistema_informativo}")
        print(f"Modalidad:{self.modalidad}")
        print(f"Servicios:{self.servicios}")
        print(f"Ubicacion:{self.ubicación}")
        print(f"Talleres:{self.talleres}")
        print(f"Cantidad de salones:{self.cantidad_salones}")
        print(f"Rector:{self.rector}")

UAEH = Universidad ("logo.jpg","Lic en antropologia social, Lic en arquitectura","pachuca","plataforma garza","presencial","bibloteca,enfermeria,cafeteria","Torres de rectoria Pachuca-Actopan km.45","futboll,basquet","24","Octavio Castillo Acosta")
