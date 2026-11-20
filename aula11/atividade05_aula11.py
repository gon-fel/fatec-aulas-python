# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 11 - Atividade 5: Energia Cinética
# ==============================================================================

import math

# 1. Entradas:
massa = float(input("Digite a massa do veículo (kg): "))
velocidade = float(input("Digite a velocidade (m/s): "))

# 2. Processamento:
velocidade_quadrado = math.pow(velocidade, 2)
energia = (massa * velocidade_quadrado) / 2

# 3. Saída:
print(f"Energia cinética: {energia:.2f} Joules")