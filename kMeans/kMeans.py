from dado import Dado
from typing import List
from grupo import Grupo
from agrupamento import Agrupamento
import random
import math


class KMeans:
    def __init__(self, k: int, conjunto_dados: List[Dado]):
        self.__k__ = k
        self.__dados__ = conjunto_dados
        self.__agrupamento__: Agrupamento = Agrupamento()

    def __selecionar_centroides_aleatorios__(self):
        for i in range(self.__k__):
            dado_escolhido = random.choice(self.__dados__)
            novo_grupo: Grupo = Grupo(dado_escolhido.get_atributos().copy())
            self.__agrupamento__.adicionar_grupo(novo_grupo)

    def __adicionar_grupo_mais_proximo__(self, dado_conjunto: Dado):
        dicionario = {}
        for grupo_atual in self.__agrupamento__.get_grupos():
            dicionario[grupo_atual] = self.__distancia_eucliana__(
                dado_conjunto.get_atributos(), grupo_atual.get_centroide())
        grupo_mais_proximo = min(dicionario, key=dicionario.get)
        grupo_mais_proximo.adicionar_dado(dado_conjunto)
        '''for i in range(self.__k__):
            grupo_temporario = agrupamento[i]
            dicionario[i] = self.__distancia_eucliana__(dado_conjunto.get_atributos(), grupo_temporario.get_centroide())
        indice_grupo_proximo = min(dicionario, key=dicionario.get)
        grupo_mais_proximo = agrupamento[indice_grupo_proximo]
        grupo_mais_proximo.adicionar_dado(dado_conjunto)'''

    def __distancia_eucliana__(self, atributos_dado: List[float], atributos_centroide: List[float]):
        somatorio: float = 0
        for atributo_dado, atributo_centroide in zip(atributos_centroide, atributos_dado):
            somatorio += math.pow((atributo_dado - atributo_centroide), 2)
        return math.sqrt(somatorio)

    def __verificar_centroides__(self):
        alteracao_centroide = False
        for grupo_atual in self.__agrupamento__.get_grupos():
            if grupo_atual.centroide_alterado():
                alteracao_centroide = True
        if alteracao_centroide:
            self.__zerar_grupos__()
        return alteracao_centroide

    def __zerar_grupos__(self):
        for grupo_atual in self.__agrupamento__.get_grupos():
            grupo_atual.zerar_grupo()


    def executar(self):
        # selecionar k centroides aleatoriamente
        self.__selecionar_centroides_aleatorios__()
        # enquanto houver alteração de centroides
        novos_centroides: bool = True
        while novos_centroides:
            # atribuir o dado ao grupo de centroide mais proximo
            for dado_conjunto in self.__dados__:
                self.__adicionar_grupo_mais_proximo__(dado_conjunto)
            # verificar alteração de centroid
            novos_centroides = self.__verificar_centroides__()
        return self.__agrupamento__
