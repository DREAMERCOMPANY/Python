from abc import ABC, abstractmethod

class Iproducto(ABC):
     
     @abstractmethod
     def calcular_costo():
          pass
     
     @abstractmethod
     def calcular_rentabilidad():
          pass
     
     @abstractmethod
     def calcular_calorias():
          pass