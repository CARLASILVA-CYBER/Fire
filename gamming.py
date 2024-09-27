import numpy as np
import matplotlib.pyplot as plt
import random

# Configurações do ambiente de simulação
grid_size = 20  # tamanho do mapa (20x20 células)
mapa = np.zeros((grid_size, grid_size))  # mapa inicial (sem fogo)
prob_fogo_inicial = 0.05  # probabilidade de uma célula começar com fogo
vento = (1, 0)  # vento soprando para a direita
inflamabilidade = 0.6  # taxa de inflamabilidade (0 a 1)
umidade = 0.3  # umidade do solo (0 a 1)

# Inicializar o mapa com fogo aleatório
def inicializar_mapa(mapa, prob_fogo_inicial):
    for i in range(grid_size):
        for j in range(grid_size):
            if random.random() < prob_fogo_inicial:
                mapa[i, j] = 1  # célula com fogo
    return mapa

# Função para simular a propagação do fogo
def simular_propagacao(mapa, vento, inflamabilidade, umidade):
    novo_mapa = np.copy(mapa)
    for i in range(grid_size):
        for j in range(grid_size):
            if mapa[i, j] == 1:  # célula com fogo
                # O fogo pode se espalhar para células vizinhas
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # vizinhos
                    ni, nj = i + di, j + dj
                    if 0 <= ni < grid_size and 0 <= nj < grid_size and mapa[ni, nj] == 0:
                        # Calcular a chance de o fogo se espalhar
                        chance_fogo = inflamabilidade * (1 - umidade)
                        # Ajuste pela direção do vento
                        if (di, dj) == vento:
                            chance_fogo *= 1.5  # vento favorece a propagação
                        elif (di, dj) == (-vento[0], -vento[1]):
                            chance_fogo *= 0.5  # vento contrário dificulta
                        if random.random() < chance_fogo:
                            novo_mapa[ni, nj] = 1  # nova célula pega fogo
    return novo_mapa

# Função para visualizar o mapa
def visualizar_mapa(mapa):
    plt.imshow(mapa, cmap='hot', interpolation='nearest')
    plt.title("Simulação de Combate ao Fogo")
    plt.show()

# Inicializar o mapa e visualizar o estado inicial
mapa = inicializar_mapa(mapa, prob_fogo_inicial)
visualizar_mapa(mapa)

# Simular a propagação do fogo em várias etapas
for t in range(10):  # simular 10 etapas
    mapa = simular_propagacao(mapa, vento, inflamabilidade, umidade)
    visualizar_mapa(mapa)
