# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 12 - Atividade 5: Cálculo da Altura de uma Rampa com Seno
# ==============================================================================

# 1. IMPORTAÇÃO DA BIBLIOTECA:
# Importa math para converter ângulos e calcular o seno.
import math

# 2. ENTRADA DE DADOS:
# Lê o comprimento da rampa e sua inclinação em graus.
comprimento_rampa = float(input("Informe o comprimento da rampa em metros: "))
angulo_grau = float(input("Informe a inclinação da rampa em graus: "))

# 3. PROCESSAMENTO TRIGONOMÉTRICO:
# Converte o ângulo para radianos e calcula a altura usando o seno.
angulo_rad = math.radians(angulo_grau)
altura = comprimento_rampa * math.sin(angulo_rad)

# 4. SAÍDA FORMATADA:
# Exibe a altura calculada com duas casas decimais.
print(f"A altura da rampa é de: {altura:.2f} metros")
