# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 4 - Atividade 1: Cálculo de Área de Retângulo (Operadores Aritméticos)
# ==============================================================================
# Enunciado:
# 1. Peça a medida da base do retângulo (inteiro).
# 2. Peça a medida da altura do retângulo (inteiro).
# 3. Calcule a área multiplicando os valores (area = base * altura).
# 4. Exiba o resultado com saída formatada.
# ==============================================================================

# 1. ENTRADA DE DADOS:
print("--- CÁLCULO DE ÁREA DE RETÂNGULO ---")
base = int(input("Digite a medida da base: "))
altura = int(input("Digite a medida da altura: "))

# 2. PROCESSAMENTO:
area = base * altura

# 3. SAÍDA:
print("\n" + "=" * 30)
print(f"A área do retângulo é: {area}")
print("=" * 30)
