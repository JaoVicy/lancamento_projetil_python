import formulas
import numpy as np
import matplotlib.pyplot as plt

try:
    t = float(input("Digite o Tempo de Observação do Objeto:").strip())
    V0 = float(input("Digite V0:").strip())
    alpha = float(input("Digite Alpha:").strip())

except ValueError:

    print("Digite um número válido.")
    exit(1)

t_total = formulas.tempo_total_voo(V0, alpha)

print(f"Tempo total de voo: {t_total:.2f}")