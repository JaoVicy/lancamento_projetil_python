import numpy as np
import matplotlib.pyplot as plt

# Tempo de voo (Teste):
# Constantes:

g = 9.8 

def tempo_voo(h):
    return np.sqrt((2 * h) / g)


# Testes para alturas diferentes:

alturas = np.linspace(0 , 100, 150, 200)
tempos = tempo_voo(alturas)


plt.figure(figsize=(10, 6))
plt.plot(alturas, tempos, label="Tempo de voo", color="blue")
plt.xlabel("Altura de lançamento (m)")
plt.ylabel("Tempo de voo (s)")
plt.title("Tempo de voo em função da altura de lançamento")
plt.legend()
plt.grid(True)
plt.show()