class Vehiculo:
    def __init__(self, marca, modelo) -> None:
        self.__marca = marca
        self.__modelo = modelo
        
    def get_marca(self) -> str: 
        return self.__marca
    def get_tipo(self) -> str: 
        return self.__modelo
    def encender(self) -> None: 
        print("Encendiendo vehículo")
    def detener(self) -> None:
        print("Deteniendo vehículo")  
        
# REFACTORIZAR Una clase Hija o SubClase, debe implementar una nueva función que utilice un nuevo arreglo/lista con valores (2020, 2021, 2022, 2023, 2024) para los distintos años Permitidos De Circulación.
# - Esta función debe recibir un parámetro correspondiente al año de fabricación de un coche, así como crear el arreglo mencionado arriba.
# - Si el valor ingresado de las puertas está entre 2-5, continuar con la validación del año, si no, mostrar un mensaje de error como “Revise nuevamente el número de puertas ingresado ya que un automovil/coche no existe uno que tenga [puertas] (valor de puertas, ejemplo: 9)
# - Validar que el año proporcionado está presente en el arreglo, se debe mostrar el mensaje: "El coche con año de fabricación [año] tiene permitido circular." (Donde "[año]" es el valor introducido por el usuario). Si el año NO está en el arreglo, se debe mostrar: "El coche con año de fabricación [año] NO puede circular en Bolivia.”
class Coche(Vehiculo):
    def __init__(self,marca, modelo, puertas, añoFabricacionCoche) -> None:
        super().__init__(marca, modelo)
        self.puertas = puertas
        
        self.añoFabricacionCoche = añoFabricacionCoche
        self.añosValidos = [2020,2021,2022,2023,2024]  # Años de fabricación válidos
    
    def validarAnhoDeCirculacion(self):
        if self.añoFabricacionCoche in self.añosValidos:
            print(f"Este coche fabricado en {self.añoFabricacionCoche} tiene permitida la circulación")
        else:
            print(f"Este coche fabricado en {self.añoFabricacionCoche} ya no puede circular en territorio Boliviano")
        
    def get_puertas(self) -> int: 
        return self.puertas    
    def encender(self) -> None: 
        print("Encendiendo Coche")
    def detener(self) -> None:
        print("Deteniendo Coche")  
       
    
# REFACTORIZAR e Implementar una nueva lógica que utilice el valor de un nuevo parámetro “amortiguación” (que reciba el valor por el usuario) en la otra clase Hija o SubClase.
# - Si la amortiguación es "Simple" o "Doble", se debe mostrar: "La bicicleta tiene una amortiguación [tipo]." (Donde "[tipo]" es el valor ingresado por el usuario).
# - Si no es ninguno de estos valores, se debe mostrar: "No existe una amortiguación [tipo].”
class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, amortiguacion) -> None:
        super().__init__(marca, modelo) 
        self.amortiguacion = amortiguacion
        
    def verificarTipoAmortiguacion(self):
        if self.amortiguacion == "Simple" or self.amortiguacion == "Doble":
            print("La bicicleta tiene una amortiguacion --> " + self.amortiguacion)
        else:
            print("No existe ese tipo de amortiguación --> " + self.amortiguacion)
        
    def encender(self) -> None: 
        print("Encendiendo Bicicleta")
    def detener(self) -> None:
        print("Deteniendo Bicicleta")  
        

marca = input("Ingrese la marca del coche: ")
modelo = input("Ingrese el tipo del coche: ")
puertas = int(input("Ingrese la cantidad de puertas del coche: "))
añoFabricacionCoche = int(input("Ingrese el año de fabricación del coche: "))
        
        
auto = Coche(marca, modelo, puertas, añoFabricacionCoche) #Aqui se esta instanciando una clase creando un "Objeto"
auto.validarAnhoDeCirculacion() # Dicho objeto nos permite reutilizar todos los metodos/funciones de la clase instanciada
auto.get_marca() #llamamos al resto de metodos
auto.get_puertas()
auto.encender()
auto.detener()


bicicleta = Bicicleta("Santosa", "BMX", "Simple")
bicicleta.verificarTipoAmortiguacion()