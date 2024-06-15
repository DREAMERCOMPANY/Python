from producto import Producto
from ingrediente import Ingrediente

class Heladeria:
    def __init__(self, producto1:Producto, producto2:Producto, producto3:Producto, producto4:Producto, ingrediente:Ingrediente):
        self._producto1 = producto1
        self._producto2 = producto2
        self._producto3 = producto3
        self._producto4 = producto4
        self._productos = [producto1, producto2, producto3, producto4]
        self.__ingredientes = []
        self._ingrediente = ingrediente
    
    def get_ingrediente(self):
        return self.__ingredientes
    
    def add_ingrediente(self, ingrediente: Ingrediente):
        if ingrediente in self.__ingredientes:
            print(f"El ingrediente {ingrediente._nombre} ya ha sido añadido.")
        else:
            self.__ingredientes.append(ingrediente)
            print(f"Ingrediente {ingrediente._nombre} añadido correctamente.")
    
    def vender(self, nombreProducto:Producto) -> bool:
        for producto in self._productos:
            if(nombreProducto in producto._nombre):

