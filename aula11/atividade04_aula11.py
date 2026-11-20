# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 11 - Atividade 4: Distância entre Pontos
# ==============================================================================

# 1. Entrada: 
x1 = float(input("Digite x1: "))
y1 = float(input("Digite y1: "))
x2 = float(input("Digite x2: "))
y2 = float(input("Digite y2: "))


# 2. Processamento:
import math
diferencaX = math.sqrt((x2 - x1) * (x2 - x1))
diferencaY = math.sqrt((y2 - y1) * (y2 - y1))

distancia = math.sqrt((diferencaX * diferencaX) + (diferencaY * diferencaY))

# 3. Saída:
print(f"Distância no eixo X: {diferencaX:.1f} m")
print(f"Distância no eixo Y: {diferencaY:.1f} m")
print(f"Distância total em linha reta: {distancia:.1f} m.")