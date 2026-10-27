# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 6 - Atividade 2: Variação Térmica (I/O, Casting e Operadores Aritméticos)
# ==============================================================================

# 1. ENTRADA DE DADOS:
# Casting obrigatório (str -> int) conforme especificação do exercício:
temp_inicial = int(input("Informe a temperatura inicial registrada pela manhã (°C): "))
temp_final = int(input("Informe a temperatura final registrada à tarde (°C): "))

# 2. PROCESSAMENTO ARITMÉTICO:
# Cálculo do delta de temperatura (variação térmica absoluta entre os dois períodos)
variacao = temp_final - temp_inicial

# 3. SAÍDA FORMATADA (Relatório Meteorológico):
print("\n" + "=" * 40)
print("       RELATÓRIO DE VARIAÇÃO TÉRMICA    ")
print("=" * 40)
print(f"Temperatura Inicial : {temp_inicial}°C")
print(f"Temperatura Final   : {temp_final}°C")
print("-" * 40)
print(f"Variação Térmica    : {variacao}°C")
print("=" * 40 + "\n")