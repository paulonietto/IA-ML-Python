import numpy as np
from genetico import Genetico

if __name__ == '__main__':
    np.random.seed(42)
    # itens da casa
    numero_itens = 10
    itens_id = np.arange(1, numero_itens + 1)
    pesos = np.random.randint(1, 15, size=numero_itens)
    valores = np.random.randint(10, 750, size=numero_itens)
    limite_mala = 41
    numero_cromossomos = 8
    tamanho_populacao = (numero_cromossomos, numero_itens)
    print(tamanho_populacao)
    algoritmo_genetico = Genetico(tamanho_populacao)
    #teste= algoritmo_genetico.fitness(pesos, valores, algoritmo_genetico.populacao_interna,limite_mala)
    algoritmo_genetico.executar(pesos,valores, 10, limite_mala)
    print("Ultima Geracao")
    print(algoritmo_genetico.populacao_interna)

