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


# Inicialização de fórmulas:
try:

    t_total = fl.tempo_total_voo(V0, alpha)

    h_maxima = fl.altura_maxima(V0, alpha)

    d_maxima = fl.distancia_maxima(V0, alpha)

    p_horizontal = fl.posicao_horizontal(V0, alpha, t)

    p_vertical = fl.posicao_vertical(V0, alpha, t)

    velocidade_horizontal = fl.velocidade_horizontal(V0, alpha)

    velocidade_vertical = fl.velocidade_vertical(V0, alpha, t)

    v_resultante = fl.velocidade_resultante(V0, alpha, t)

    angulo_velocidade = fl.angulo_velocidade(V0, alpha, t)

except ValueError:
    print("Ocorreu um erro no cálculo:")
    exit(1)


# Testes de Print:
try:
    resultados = {
        "Tempo total de voo": t_total,
        "Altura máxima": h_maxima,
        "Distância máxima": d_maxima,
        "Posição horizontal": p_horizontal,
        "Posição vertical": p_vertical,
        "Velocidade horizontal": velocidade_horizontal,
        "Velocidade vertical": velocidade_vertical,
        "Velocidade resultante": v_resultante,
        "Ângulo da velocidade": angulo_velocidade,
    }
    
    # Exibição dos resultados
    for nome, valor in resultados.items():
        print(f"{nome}: {valor:.2f}")
except ValueError:
    print("Ocorreu um erro no cálculo.")
    exit(1)
