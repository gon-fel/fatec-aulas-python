# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 11 - Atividade 3: Velocidade de Queda
# ==============================================================================

import math

# 1. ENTRADA DE DADOS:
altura = float(input("Digite a altura da queda (metros): "))

# 2. CÁLCULO DA VELOCIDADE:
velocidade = math.sqrt(2*10*altura)

# 3. SAÍDA DE DADOS:
print(" ")

print(f"A velocidade ao tocar o solo é: {velocidade:.1f} m/s")