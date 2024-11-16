import formulas as fl
import numpy as np
import matplotlib.pyplot as plt


try:
    t = float(input("Digite o Tempo de Observação:").strip())
    V0 = float(input("Digite V0:").strip())
    alpha = float(input("Digite Alpha:").strip())

except ValueError:
    print("Digite um número válido: :(")
    exit(1)

# Convertendo o angulo para radianos:
alpha_rad = np.radians(alpha)

# Calculando os dados:
try:

    t_total = fl.tempo_total_voo(V0, alpha)
    h_maxima = fl.altura_maxima(V0, alpha)
    d_maxima = fl.distancia_maxima(V0, alpha)

    # Gerando dados para a tragetória:
    t_values = np.linspace(0, t_total, num = 500)
    x_values = [fl.posicao_horizontal(V0, alpha, t) for t in t_values]
    y_values = [fl.posicao_vertical(V0, alpha, t) for t in t_values]

    # Destaques do gráfico:
    pontos_tempo = np.linspace(0, t_total, num = 5)
    pontos_x = [fl.posicao_horizontal(V0, alpha, t) for t in pontos_tempo]
    pontos_y = [fl.posicao_vertical(V0, alpha, t) for t in pontos_tempo]
    velocidades_vx = [fl.velocidade_horizontal(V0, alpha) for t in pontos_tempo]
    velocidades_vy = [fl.velocidade_vertical(V0, alpha, t) for t in pontos_tempo]
    velocidades_resultantes = [fl.velocidade_resultante(V0, alpha, t) for t in pontos_tempo]

except Exception as e:
    print(f"Erro ao calcular {e}")
    exit(1)

