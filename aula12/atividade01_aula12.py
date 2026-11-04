# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 12 - Atividade 1: Cálculo de Raiz Quadrada com a Biblioteca math
# ==============================================================================

import math

# 1. ENTRADA DE DADOS:
# Lê o número informado para o cálculo da raiz quadrada.
numero = float(input("Digite um número positivo: "))

# 2. PROCESSAMENTO MATEMÁTICO:
# Calcula a raiz quadrada usando a função sqrt() do módulo math.
raiz = math.sqrt(numero)

# 3. SAÍDA FORMATADA:
# Exibe o resultado com duas casas decimais.
print(f"A raiz quadrada de {numero} é {raiz:.2f}")