import numpy as np
import matplotlib.pyplot as plt

# Parâmetros da simulação
A = 100  # Amplitude da aceleração (m/s²)
omega = 2 * np.pi  # Frequência angular (rad/s)
t_max = 10  # Tempo máximo da simulação (s)
dt = 0.01  # Intervalo de tempo (s)

# Vetor de tempo
t = np.arange(0, t_max, dt);

# Função de aceleração variando com o tempo
a = A * np.sin(omega * t)

# Integração numérica para encontrar a velocidade e a posição
v = np.cumsum(a) * dt  # Velocidade como a integral de a(t)
x = np.cumsum(v) * dt  # Posição como a integral de v(t)

# Plot dos gráficos
plt.figure(figsize=(10, 8))

# Gráfico da aceleração
plt.subplot(3, 1, 1)
plt.plot(t, a, label='Aceleração (a)', color='blue')
plt.ylabel('Aceleração (m/s²)')
plt.legend(loc="upper right")
plt.grid(True)

# Gráfico da velocidade
plt.subplot(3, 1, 2)
plt.plot(t, v, label='Velocidade (v)', color='green')
plt.ylabel('Velocidade (m/s)')
plt.legend(loc="upper right")
plt.grid(True)

# Gráfico da posição
plt.subplot(3, 1, 3)
plt.plot(t, x, label='Posição (x)', color='red')
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.legend(loc="upper right")
plt.grid(True)

plt.tight_layout()
plt.show()
