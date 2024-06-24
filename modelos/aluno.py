class Aluno:
    def __init__(self, nome, turma, categoria):
        self._nome = nome
        self._turma = turma
        self._categoria = categoria
        self._notas = []
        
    def __str__(self) -> str:
        notas_str = '\n'.join(str(nota) for nota in self._notas)
        return f'Aluno: {self._nome} | Turma: {self._turma} | Categoria: {self._categoria} | Notas:\n{notas_str}'
    
    
        