from producto import Producto
from funciones import *
from ingrediente import Ingrediente

class Copa(Producto):
    def __init__(self, nombre: str, precio_publico: float, ingrediente1: Ingrediente, ingrediente2: Ingrediente, ingrediente3: Ingrediente, tipo_vaso:str):
        super().__init__(nombre, precio_publico, ingrediente1, ingrediente2, ingrediente3)
        self.__tipoVaso = tipo_vaso
        self._calorias = [ingrediente1._calorias, ingrediente2._calorias, ingrediente3._calorias ]

         #getters y setters
    def get_tipoVaso(self)->str:
        return self.__tipoVaso
    
    def set_tipoVaso(self, vaso:str):
        self.__tipoVaso = vaso
    
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



        

   
