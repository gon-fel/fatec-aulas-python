# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 11 - Atividade 6: Raio da Base de uma Coluna
# ==============================================================================

import math

# 1. Entradas:
area = float(input("Digite a área da base da coluna (m²): "))

# 2. CÁLCULO DO RAIO:
raio = math.sqrt(area / math.pi)

# 3. SAÍDA DE DADOS:
print(f"O raio da coluna é: {raio:.2f} metros")