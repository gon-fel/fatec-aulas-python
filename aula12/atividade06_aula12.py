# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 12 - Atividade 6: Distância Horizontal de uma Escada com Cosseno
# ==============================================================================

# 1. IMPORTAÇÃO DA BIBLIOTECA:
# Importa math para converter ângulos e calcular o cosseno.
import math

# 2. ENTRADA DE DADOS:
# Lê o comprimento da escada e seu ângulo de inclinação em graus.
comprimento_escada = float(input("Informe o comprimento da escada em metros: "))
angulo_grau = float(input("Informe o angulo de inclinação da escada em relaçao ao chão em graus: "))

# 3. PROCESSAMENTO TRIGONOMÉTRICO:
# Converte o ângulo para radianos e calcula a distância horizontal.
angulo_rad = math.radians(angulo_grau)
distancia = comprimento_escada * math.cos(angulo_rad)

# 4. SAÍDA FORMATADA:
# Exibe a distância horizontal calculada.
print('-' * 30)
print(f"A distância horizontal do pé da escada até a parede é de: {distancia:.2f} metros.\n")
