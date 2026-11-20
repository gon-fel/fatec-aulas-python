# ==============================================================================================
# Atividade 03 - Aula 12: Divisão com pi usando a biblioteca math.
# Descrição: Crie um programa que solicite ao operador a área da tampa metálica (m²). Utilizando a constante math.pi e a função math.sqrt() do módulo math, calcule o raio correspondente da peça e exiba o resultado.
# ===============================================================================================

import math

# 1. Entrada dos Dados:
area = float(input("Informe o valor da área da tampa metálica em (m²): "))

# 2. Processamento: 
divisao = area / math.pi
raio = math.sqrt(divisao)

# 3. Saída: 
print(f"O valor do raio é: {raio:.2f}")