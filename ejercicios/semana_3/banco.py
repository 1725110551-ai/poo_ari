class Banco:

    def __init__(self,nombre_del_banco,ubicacion,pais,moneda_principal,cantidade_de_sucursales,num_de_clientes,fondos_totales,estado_de_operacion,id_banco,telefono_de_contacto):
        self.nombre_del_banco=nombre_del_banco
        self.ubicacion=ubicacion
        self.pais=pais
        self.moneda_principal=moneda_principal
        self.cantidade_de_sucursales=cantidade_de_sucursales
        self.num_de_clientes=num_de_clientes
        self.fondos_totales=fondos_totales
        self.estado_de_operacion=estado_de_operacion
        self.id_banco=id_banco
        self.telefono_de_contacto=telefono_de_contacto
        
        print(f"nombre del banco:{self.nombre_del_banco}")
        print(f"ubicacion:{self.ubicacion}")
        print(f"pais:{self.pais}")
        print(f"moneda principal:{self.moneda_principal}")
        print(f"cantidad de sucursales:{self.cantidade_de_sucursales}")
        print(f"numero de clientes:{self.num_de_clientes}")
        print(f"fondos totales:{self.fondos_totales}")
        print(f"estado de operacion:{self.estado_de_operacion}")
        print(f"id del banco:{self.id_banco}")
        print(f"telefono de contacto:{self.telefono_de_contacto}")

    def asaltar(self):
        print("asaltar el banco")
    def prestamo(self):
        print("pedir un prestamo al banco")
    def sacar(self):
        print("sacar dinero del banco")
    def meter(self):
        print("meter dinero al banco")
    def consultar(self):
        print("consultar el estado de cuenta en el banco")

BBVA = Banco("BBVA", "Ciudad de México", "México", "Peso Mexicano", 100, 1000, 1000000, "Operativo", "BBVA001", "55-1234-5678")

BBVA.asaltar()
BBVA.prestamo()
BBVA.sacar()
BBVA.meter()
BBVA.consultar()