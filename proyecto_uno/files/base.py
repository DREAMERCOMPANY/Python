from ingrediente import Ingrediente

class Base(Ingrediente):
    def __init__(self, precio: float, calorias: float, nombre: str, es_vegetariano: bool, sabor:str):
        super().__init__(precio, calorias, nombre, es_vegetariano)
        self.__sabor = sabor
    
    #getters y setters nuevo atributo 'sabor'

    def get_sabor(self)->str:
        return self.__sabor
    
    def set_sabor(self, sabor:str)->str:
        self.__sabor = sabor
    
    #Implementacion metodo abstracto
    def abastecer(self):
        self._inventario += 5