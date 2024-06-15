from abc import ABC, abstractmethod
from funciones import *

class Ingrediente:
    def __init__(self, precio:float, caloria:float, nombre:str,  es_vegetariano:bool):
        self._precio = precio
        self._caloria = caloria
        self._calorias = [self._caloria]
        self._nombre = nombre
        self._inventario = 0
        self._vegetariano = es_vegetariano
    
    #metodo abastracto
    @abstractmethod
    def abastecer(self):
        pass
    
    #Metodo llamando a funcion 'es_sano'
    def es_sano(self)->bool:
        es_sano(self._calorias, self._vegetariano)
    
    def get_calorias(self):
        return self._calorias
    
    def add_calorias(self, caloria):
        self._calorias.append(caloria)
    
    # getters, setter

    def get_precio(self)->float:
        return self._precio
    
    def setPrecio(self, precio:float):
        self._precio = precio
    
    def get_calorias(self)->float:
        return self._calorias
    
    def set_calorias(self, caloria:float):
        self._calorias = caloria

    def get_nombre(self)->str:
        return self._nombre
    
    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_inventario(self)->int:
        return self._inventario
    
    def get_esVegetariano(self)->bool:
        return self._vegetariano
    
    def set_esVegetariano(self, vegetariano):
        self._vegetariano = vegetariano