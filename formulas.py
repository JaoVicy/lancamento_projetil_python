import numpy as np

G = 9.81

# Tempo total de voo:
def tempo_total_voo(V0, alpha):
    return (2 * V0 * np.sin(np.radians(alpha))) / G

# Altura Máxima:
def altura_maxima(V0, alpha):
    return(V0**2 * (np.sin(np.radians(alpha))**2)) / (2 * G)

# Distância Máxima:
def distancia_maxima(V0, alpha):
    return(V0**2 * np.sin(np.radians(2 * alpha))) / G

# Posição Horizontal:
def posicao_horizontal(V0, alpha, t):
    return V0 * np.cos(np.radians(alpha)) * t

# Posição na vertical:
def posicao_vertical(V0, alpha, t):
    return(V0 * np.sin(np.radians(alpha)) * t) - (0.5 * G * t**2)

# Velocidade na horizontal:
def velocidade_horizontal(V0, alpha):
    return V0 * np.cos(np.radians(alpha))

# Velocidade na vertical:
def velocidade_vertical(V0, alpha, t):
    return (V0 * np.sin(np.radians(alpha)) - G * t)

# Velocidade resultante:
def velocidade_resultante(V0, alpha, t):
    Vx = velocidade_horizontal(V0, alpha)
    Vy = velocidade_vertical(V0, alpha, t)
    return np.sqrt(Vx**2 + Vy**2)

# Ângulo da velocidade em relação à horizontal:
def angulo_velocidade(V0, alpha, t):
    Vx = velocidade_horizontal(V0, alpha)
    Vy = velocidade_vertical(V0, alpha, t)
    return np.degrees(np.arctan(Vy / Vx))
