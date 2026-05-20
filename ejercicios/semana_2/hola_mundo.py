class NombreClase:

    def __init__(self):
        print("Constructor")

    def metodoUno(self):
        """
        Este metodo no recibe variables

        Print:
        El metodo imprimira variables cuando se le sean asignadas y
        definidas
        """
        print("Metodo uno")

    def metodoDos(self, variable_uno:int, variable_dos:float)->int:
        """
        Este metodo recibe 2 variables enteras, las suma y regresa el
        resultado  de la suma

        Args:

        variable_uno:int - Primer numero entero
        variable_dos:int - Segundo numero entero
        
        Return:
        
        suma : int - Suma de los dos numeros enteros
        """
        suma = variable_uno + variable_dos
        return suma
    
    def metodoTres(self, variable_tres:str)->None:
        """
        Este metodo recibe una variable que solo recibira datos
        tipo string
        
        print:
        Imprime en la consola la cantidad de caracteres de la cadena 
        recibida
        """
        print(f"Numero de caracteres: {len(variable_tres)}")

nombre_objeto = NombreClase()
nombre_objeto.metodoUno()