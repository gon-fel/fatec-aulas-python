# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 10 - Tarefa de Casa 4.1: Inspeção de Caixas por Turno
# ==============================================================================

# 1. INSPEÇÃO DO TURNO DA MANHÃ:
print("--- TURNO DA MANHÃ ---")

qtd_caixas_manha = int(input("Quantidade de caixas da manhã: "))

caixas_reprovadas_manha = 0
for i in range(1, qtd_caixas_manha + 1):
    peso_manha = int(input(f"Peso da caixa {i} (kg): "))

    if peso_manha > 50:
        caixas_reprovadas_manha = caixas_reprovadas_manha + 1

# 2. INSPEÇÃO DO TURNO DA TARDE:
print("\n--- TURNO DA TARDE ---")
qtd_caixas_tarde = int(input("Quantidade de caixas da tarde: "))

caixas_reprovadas_tarde = 0
for i in range(1, qtd_caixas_tarde + 1):
    peso_tarde = int(input(f"Peso da caixa {i} (kg): "))

    if peso_tarde > 50:
        caixas_reprovadas_tarde = caixas_reprovadas_tarde + 1

# 3. RESULTADOS DO DIA:
print("\nRESULTADOS DO DIA")
print(f"Caixas acima do peso na manhã: {caixas_reprovadas_manha}")
print(f"Caixas acima do peso a tarde: {caixas_reprovadas_tarde}")

caixas_desaprovadas = caixas_reprovadas_manha + caixas_reprovadas_tarde
print(f"Total de caixas fora do padrão: {caixas_desaprovadas}")
