# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 12 - Atividade 2: Teorema de Pitágoras com a Biblioteca math
# ==============================================================================

# 1. IMPORTAÇÃO DA BIBLIOTECA:
# Importa math para calcular a raiz quadrada da soma dos quadrados.
import math

# 2. ENTRADA DE DADOS:
# Lê os comprimentos dos dois catetos.
numeroA = float(input("Digite o valor do primeiro angulo: "))
numeroB = float(input("Digite o valor do segundo angulo: "))

# 3. PROCESSAMENTO MATEMÁTICO:
# Aplica o teorema de Pitágoras para obter o comprimento da hipotenusa.
soma_dos_quadrados = (numeroA * numeroA) + (numeroB * numeroB)
hipotenusa = math.sqrt(soma_dos_quadrados)

# 4. SAÍDA FORMATADA:
# Exibe o comprimento calculado com duas casas decimais.
print(f"O valor da hipotenusa é: {hipotenusa:.2f}")