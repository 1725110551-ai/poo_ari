class Telefono:

    def __init__(self,color,materiales,componentes,peso,precio,resistencia_al_agua,almacenamiento,voltaje,modelo):
        self.color=color
        self.materiales=materiales
        self.componentes=componentes
        self.peso=peso
        self.precio=precio
        self.resistencia_al_agua=resistencia_al_agua
        self.almacenamiento=almacenamiento
        self.voltaje=voltaje
        self.modelo=modelo
        
        print(f"color del telefono:{self.color}")
        print(f"Materiales:{self.materiales}")
        print(f"Componentes:{self.componentes}")
        print(f"Peso:{self.peso}")
        print(f"Precio:{self.precio}")
        print(f"Resistencia al agua:{self.resistencia_al_agua}")
        print(f"Almacenamiento:{self.almacenamiento}")
        print(f"Voltaje:{self.voltaje}")
        print(f"Modelo:{self.modelo}")

    def llamar(self):
        print("llamar al telefono")
    def tomar_fotos(self):
        print("Tomar fotos con el telefono")
    def enviar_mensajes(self):
        print("Enviar mensajes con el telefono")
    def escribir(self):
        print("Escribir con el telefono")
    def reproducir_musica(self):
        print("Reproducir musica con el telefono")

iphone_14_pro = Telefono("negro mate","acero inoxisable,vidrio mate","chip A16, super retins XDR","6 gr","$7900","6 metros hasta 30 minutos","128 GB","20 V","iPhone 14 Pro")

iphone_14_pro.llamar()
iphone_14_pro.tomar_fotos()
iphone_14_pro.enviar_mensajes()
iphone_14_pro.escribir()
iphone_14_pro.reproducir_musica()