class NombreClase:

    def __init__(self):
        print("Constructor")

    def metodoUno(self):
        print("Metodo uno")

    def metodoUno(self, variable_uno:int, variable_dos:float)->int:
        suma = variable_uno + variable_dos
        return suma

nombre_objeto = NombreClase()
nombre_objeto.metodoUno()