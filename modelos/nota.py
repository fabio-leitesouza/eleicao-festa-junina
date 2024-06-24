class Nota:
    def __init__(self, elegancia, desenvoltura, simpatia, reciclagem):
        self._elegancia = elegancia
        self._desenvoltura = desenvoltura
        self._simpatia = simpatia
        self._reciclagem = reciclagem
        
    def calcular_media():
        pass
    
    def __str__(self) -> str:
        return f' Elegância: {self._elegancia} | Desenvoltura: {self._desenvoltura} | Simpatia: {self._simpatia} | Reciclagem: {self._reciclagem}'