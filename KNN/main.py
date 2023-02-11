from dado import Dado
from novo_dado import NovoDado
from k_nearest_neighbors import KNN
from typing import List

if __name__ == '__main__':
    conjunto_dados: List[Dado] = []
    with open('.\\iris.txt') as arquivo:
        for linha in arquivo.readlines():
            atributos = linha.rstrip().split(',')
            classe = atributos[-1]
            atributos = list(map(float, atributos[:-1]))
            dado_arquivo: Dado = Dado(atributos, classe)
            conjunto_dados.append(dado_arquivo)
    arquivo.close()
    dado_teste: NovoDado = NovoDado([7.6, 3, 6.6, 2.1])
    kvizinhos = KNN(3, conjunto_dados)
    kvizinhos.executar(dado_teste)
    print(dado_teste.get_classe())
