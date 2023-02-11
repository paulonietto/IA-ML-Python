class No:
    def __init__(self, nome, funcaoH):
        self.nome = nome
        self.funcaoH = funcaoH
        self.funcaoF = 0
        self.funcaoG = 0
        self.noAntecessor = None


    def getNome(self):
        return self.nome

    def getFuncaoH(self):
        return self.funcaoH

    def getFuncaoG(self):
        return self.funcaoG

    def setFuncaoG(self, funcaoG):
        self.funcaoG = funcaoG

    def getFuncaoF(self):
        return self.funcaoF

    def setFuncaoF(self, funcaoF):
        self.funcaoF = funcaoF

    def getNoAntecessor(self):
        return self.noAntecessor

    def setNoAntecessor(self, noAntecessor):
        self.noAntecessor = noAntecessor

    def getAdjacentes(self):
        return self.adjacentes

    def setAdjacentes(self, adjacentes):
        self.adjacentes = adjacentes



