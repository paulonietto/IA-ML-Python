import matplotlib.pyplot as plt
from agrupamento import Agrupamento

class Visualizacao:
    def plotar(novo_agrupamento: Agrupamento):
        indice = 0
        for grupo in novo_agrupamento.get_grupos():
            centroide = grupo.get_centroide()
            x = [centroide[0]]
            y = [centroide[1]]
            for dado in grupo.get_dados():
                atributos = dado.get_atributos()
                x.append(atributos[0])
                y.append(atributos[1])
            plt.scatter(x, y, label="Grupo " + str(indice))
            indice += 1
        plt.xlabel("Eixo X")
        plt.ylabel("Eixo Y")
        plt.title("Agrupamento")
        plt.legend()
        plt.show()
