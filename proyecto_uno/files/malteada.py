from producto import Producto
from funciones import *
from ingrediente import Ingrediente

class Malteada(Producto):
    def __init__(self, nombre: str, precio_publico: float, ingrediente1: Ingrediente, ingrediente2: Ingrediente, ingrediente3: Ingrediente, volumen:float):
        super().__init__(nombre, precio_publico, ingrediente1, ingrediente2, ingrediente3)
        self.__volumen = volumen
        self._calorias = [ingrediente1._calorias, ingrediente2._calorias, ingrediente3._calorias ]

         #getters y setters
    def get_volumen(self)->str:
        return self.__volumen
    
    def set_volumen(self, volumen:str):
        self.__volumen = volumen
    
    #Implementacion metodos clase abastracta Producto

    def calcular_calorias(self):
        return contar_calorias([self._calorias])
    
    def calcular_costo(self):
        costoIngrediente1 = {"nombre":self._ingrediente1._nombre , "precio": self._ingrediente1._precio}
        costoIngrediente2 = {"nombre": self._ingrediente2._nombre , "precio":self._ingrediente2._precio}
        costoIngrediente3 = {"nombre": self._ingrediente3._nombre , "precio": self._ingrediente3._precio}
        return calcular_costo(costoIngrediente1,costoIngrediente2 ,costoIngrediente3)
    
    def calcular_rentabilidad(self):
        costoIngrediente1 = {"nombre":self._ingrediente1._nombre , "precio": self._ingrediente1._precio}
        costoIngrediente2 = {"nombre": self._ingrediente2._nombre , "precio":self._ingrediente2._precio}
        costoIngrediente3 = {"nombre": self._ingrediente3._nombre , "precio": self._ingrediente3._precio}
        return calcular_rentabilidad(self._precio,costoIngrediente1,costoIngrediente2,costoIngrediente3 ) 


