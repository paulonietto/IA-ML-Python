import numpy as np
import random as rd


class Genetico:

    def __init__(self, tamanho_populacao):
        self.tamanho_populacao = tamanho_populacao
        self.populacao_interna = np.random.randint(2, size=tamanho_populacao)
        rd.seed(42)

    def fitness(self, pesos, valores, populacao, limite_mala):
        numero_individuos = populacao.shape[0]
        print(populacao.shape[0])
        fitness = np.empty(numero_individuos)
        for i in range(numero_individuos):
            somatorio_valores = np.sum(populacao[i] * valores)
            somatorio_pesos = np.sum(populacao[i] * pesos)
            if somatorio_pesos <= limite_mala:
                fitness[i] = somatorio_valores
            else:
                fitness[i] = 0
        return fitness.astype(int)

    def encontrar_melhores(self, quantidade_selecionados, fitness_temp):
        indices_melhores = []
        for i in range(quantidade_selecionados):
            melhor = max(fitness_temp)
            indice = fitness_temp.index(melhor)
            indices_melhores.append(indice)
            fitness_temp[indice] = 0
        return indices_melhores

    def selecionar(self, fitness, quantidade_selecionados, populacao):
        # retornar os melhores - elitista
        fitness_temp = list(fitness)
        indices_melhores = self.encontrar_melhores(quantidade_selecionados, fitness_temp)
        # copia dos melhores cromossomos
        melhores = np.zeros((quantidade_selecionados, populacao.shape[1]))
        self.copia_melhores_cromossomos(quantidade_selecionados, melhores, populacao, indices_melhores)
        return melhores

    def copia_melhores_cromossomos(self, quantidade_selecionados, melhores, populacao, indices_melhores):
        for i in range(quantidade_selecionados):
            melhores[i, :] = populacao[indices_melhores[i], :]

    def cruzamento(self, populacao_atual, melhores, quantidade_filhos):
        nova_geracao = np.empty((quantidade_filhos, populacao_atual.shape[1]))
        ponto_corte = int(populacao_atual.shape[1] / 2)
        taxa_cruzamento = 0.8
        i = 0
        numero_cromossomos = len(melhores)
        while i < quantidade_filhos:
            x = rd.random()
            if x <= taxa_cruzamento:
                pai1 = i % numero_cromossomos
                pai2 = (i + 1) % numero_cromossomos
                nova_geracao[i, 0:ponto_corte] = melhores[pai1, 0:ponto_corte]
                nova_geracao[i, ponto_corte:] = melhores[pai2, ponto_corte:]
                i += 1
        return nova_geracao

    def mutacao(self, geracao):
        taxa_mutacao = 0.4
        for i in range(1, geracao.shape[0]):
            x = rd.random()
            if x <= taxa_mutacao:
                posicao_randomica = rd.randint(0, geracao.shape[1] - 1)
                if geracao[i, posicao_randomica] == 0:
                    geracao[i, posicao_randomica] = 1
                else:
                    geracao[i, posicao_randomica] = 0

    def executar(self, pesos, valores, numero_geracoes, limite_mala):
        quantidade_selecionados = int(self.tamanho_populacao[0] / 2)
        quantidade_filhos = self.tamanho_populacao[0] - quantidade_selecionados
        populacao_atual = self.populacao_interna

        for i in range(numero_geracoes):
            print("\n ***geracao ", i, "***")
            print("\n Populacao atual \n")
            print(populacao_atual)
            # calcular o fitness da populacao atual
            fitness = self.fitness(pesos, valores, populacao_atual, limite_mala)
            print(fitness, "melhor:", max(fitness))
            # seleção dos melhores
            melhores = self.selecionar(fitness, quantidade_selecionados, populacao_atual)
            # realizar o cruzamento
            nova_geracao = self.cruzamento(populacao_atual, melhores, quantidade_filhos)
            self.mutacao(nova_geracao)
            populacao_atual[0:quantidade_selecionados, :] = melhores
            populacao_atual[quantidade_selecionados:, :] = nova_geracao
