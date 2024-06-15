from ingrediente import Ingrediente

class Complemento(Ingrediente):
    def __init__(self, precio: float, calorias: float, nombre: str, es_vegetariano: bool):
        super().__init__(precio, calorias, nombre, es_vegetariano)
    
    #implementacion clase abstracta

    def abastecer(self):
        self._inventario += 10
    
    def renovar_inventario(self):
        self._inventario = 0

    