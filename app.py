from modelos.jurado import Jurado
from modelos.aluno import Aluno


def main():
    caua = Aluno('Caua', 'TI', 'Mister')
    jurado = Jurado('Carléia', 'Educacional')

    jurado.atribuir_nota(caua, 5, 5, 5, 5)
    jurado.atribuir_nota(caua, 6, 6, 6, 6)

    print(caua)

if __name__ == "__main__":
    main()