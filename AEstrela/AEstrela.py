from No import No
import Aresta


class AEstrela:

    def buscaAEstrela(self,noOrigem: No, noDestino: No):
        prioridades = []
        explorados = []
        if noOrigem != noDestino:
            # filaPrioridades adiciona origem
            noOrigem.setFuncaoG(0)
            prioridades.append(noOrigem)
            # Enquanto filaPrioridades não vazia e destino não encontrado
            noAtual = prioridades[0]
            while len(prioridades) > 0 and (noAtual != noDestino):
                # Fila explorados adiciona nó atual
                explorados.append(noAtual)
                #Se no atual == destino -> parar
                # Para cada aresta adjacente do no atual
                for aresta in noAtual.getAdjacentes():
                    # No filho = aresta.alvo
                    noFilho = aresta.getAlvo()
                    # funcaoGTemp = noAtual.FuncaoG() + aresta.custo;
                    funcaoGTemp = noAtual.getFuncaoG() + aresta.getCusto()
                    # funcaoFTemp = funcaoGTemp + noFilho.FuncaoH()
                    funcaoFTemp = funcaoGTemp + noFilho.getFuncaoH()
                    # Se caso o nó filho já tenha sido explorado e
                    # seu valor de função f é maior que a função f do pai,
                    # então ele é desconsiderado
                    if not (noFilho in explorados and funcaoFTemp > noAtual.getFuncaoF()):
                        if noFilho not in prioridades or noFilho.getFuncaoF() > funcaoFTemp:
                            noFilho.setNoAntecessor(noAtual)
                            noFilho.setFuncaoG(funcaoGTemp)
                            noFilho.setFuncaoF(funcaoFTemp)
                            prioridades.append(noFilho)
                # No atual = no com menor função f
                noAtual = self.menorFuncaoF(prioridades)



    def menorFuncaoF(self,prioridades):
        noMenorCusto = prioridades[0]
        for no in prioridades:
            if no.getFuncaoF() < noMenorCusto.getFuncaoF():
                noMenorCusto = no
        prioridades.remove(noMenorCusto)
        return noMenorCusto

    def percorrerCaminho(self, alvo: No):
        caminho = ']'
        while not (alvo is None):
            caminho = ', ' + alvo.getNome() + caminho
            alvo = alvo.getNoAntecessor()
        caminho = '[' + caminho
        return caminho
