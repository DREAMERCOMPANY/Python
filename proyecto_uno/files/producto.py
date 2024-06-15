from iproducto import Iproducto
from abc import ABC, abstractmethod
from ingrediente import Ingrediente

class Producto(ABC, Iproducto):
    def __init__(self, nombre:str, precio_publico:float, ingrediente1:Ingrediente, ingrediente2:Ingrediente, ingrediente3:Ingrediente):
        super().__init__()
        self._nombre = nombre
        self._precio = precio_publico
        self._ingrediente1 = ingrediente1
        self._ingrediente2 = ingrediente2
        self._ingrediente3 = ingrediente3
    
    
    # Llamado metodos abstractos de Iproducto
    @abstractmethod
    def calcular_calorias():
        pass

    @abstractmethod
    def calcular_costo():
        pass

    @abstractmethod
    def calcular_rentabilidad():
        pass

    #getters y setters
    def get_nombre(self)->str:
        return self._nombre
    
    def set_nombre(self, nombre:str)->str:
        self._nombre = nombre

    def get_precio(self)->float:
        return self._precio
    
    def set_precio(self, precio):
        self._precio = precio