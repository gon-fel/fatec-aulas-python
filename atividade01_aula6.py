# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 6 - Atividade 1: Consumo Médio de Combustível (I/O, Casting e Operadores)
# ==============================================================================

# 1. ENTRADA DE DADOS:
# Casting obrigatório (str -> int) conforme especificação do exercício:
distancia_km = int(input("Informe a distância total percorrida (km): "))
litros_gastos = int(input("Informe a quantidade total de combustível gasta (litros): "))

# 2. PROCESSAMENTO ARITMÉTICO:
# Cálculo do consumo médio: razão entre espaço percorrido e volume de combustível
consumo_medio = distancia_km / litros_gastos

# 3. SAÍDA FORMATADA (Relatório de Consumo):
print("\n" + "=" * 40)
print("       RELATÓRIO DE CONSUMO MÉDIO       ")
print("=" * 40)
print(f"Distância Percorrida: {distancia_km} km")
print(f"Combustível Gasto   : {litros_gastos} litros")
print("-" * 40)
print(f"Consumo Médio       : {consumo_medio:.1f} km/l")
print("=" * 40 + "\n")