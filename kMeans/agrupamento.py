from grupo import Grupo
from typing import List

class Agrupamento:

    def __init__(self):
        self.__grupos__: List[Grupo] = []

    def adicionar_grupo(self, novo_grupo: Grupo):
        self.__grupos__.append(novo_grupo)

    def get_grupos(self):
        return self.__grupos__