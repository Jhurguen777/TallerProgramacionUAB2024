class Vehiculo:
    def __init__(self, marca, modelo) -> None:
        self.marca = marca
        self.modelo = modelo
        
    def get_marca(self) -> str: 
        return self.marca
    def get_tipo(self) -> str: 
        return self.modelo
    def encender(self) -> None: 
        print("Encendiendo vehículo")
    def detener(self) -> None:
        print("Deteniendo vehículo")  
        
class Clase1(Vehiculo):
    def __init__(self,marca, modelo, puertas) -> None:
        super().__init__(marca, modelo)
        self.puertas = puertas
    def get_puertas(self) -> int: 
        return self.puertas    
       
    
class Clase2(Vehiculo):
    def __init__(self, marca, modelo, amortiguacion) -> None:
        super().__init__(marca, modelo) 
        self.amortiguacion = amortiguacion
        