# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 12 - Atividade 3: Cálculo do Raio de uma Tampa Circular
# ==============================================================================

# 1. IMPORTAÇÃO DA BIBLIOTECA:
# Importa math para utilizar a constante pi e a função de raiz quadrada.
import math

# 2. ENTRADA DE DADOS:
# Lê a área da tampa circular em metros quadrados.
area = float(input("Informe o valor da área da tampa metálica em (m²): "))

# 3. PROCESSAMENTO MATEMÁTICO:
# Isola o raio na fórmula da área do círculo: raio = raiz(area / pi).
divisao = area / math.pi
raio = math.sqrt(divisao)

# 4. SAÍDA FORMATADA:
# Exibe o raio calculado com duas casas decimais.
print(f"O valor do raio é: {raio:.2f}")