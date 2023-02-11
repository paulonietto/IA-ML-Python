from No import No
class Aresta:
    def __init__(self,  alvo:No, custo:float):
        self.custo = custo
        self.alvo = alvo

    def getCusto(self):
        return self.custo

    def getAlvo(self):
        return self.alvo