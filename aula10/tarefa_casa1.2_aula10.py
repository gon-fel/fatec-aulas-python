# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 10 - Tarefa de Casa 1.2: Inspeção de Peças
# ==============================================================================

# 1. ENTRADA DE DADOS:
total_peca = int(input("Digite a quantidade de peças a inspecionar: "))
print(" ")

# 2. INSPEÇÃO DAS PEÇAS:
aprovadas = 0
for i in range(1, total_peca + 1):
    nota = int(input(f"Nota da peça {i} (0 a 10): "))

    if nota >= 7:
        aprovadas = aprovadas + 1
# 3. SAÍDA DE DADOS:
print(f"\nTotal de peças aprovadas {aprovadas}")