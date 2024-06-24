from modelos.nota import Nota

class Jurado:
    def  __init__(self, nome, area):
        self._nome = nome
        self._area = area
        
    def __str__(self) -> str:
        return f'Jurado: {self._nome} | Area: {self._area}'
    
    def atribuir_nota(self, aluno, elegancia, desenvoltura, simpatia, reciclagem):
        avaliacao = Nota(elegancia, desenvoltura, simpatia, reciclagem)
        aluno._notas.append(avaliacao)