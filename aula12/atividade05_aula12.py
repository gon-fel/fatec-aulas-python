# ==========================================
# Atividade 05 - Aula 12: Seno e Coseno usando a biblioteca math.
# Descrição: Crie um programa que solicite o comprimento da rampa em metros e a sua inclinação em graus. Converta o ângulo para radianos e, usando math.sin(), calcule a altura atingida pela rampa.
# ==========================================

import math
# 1. Entrada dos dados:
comprimento_rampa = float(input("Informe o comprimento da rampa em metros: "))
angulo_grau = float(input("Informe a inclinação da rampa em graus: "))

# 2. Processamento: 
angulo_rad = math.radians(angulo_grau)

altura = comprimento_rampa * math.sin(angulo_rad)

# 3. Saída:
print(f"A altura da rampa é de: {altura:.2f} metros")

