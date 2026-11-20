# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 10 - Tarefa de Casa 2.2: Gratuidades de Passageiros
# ==============================================================================

# 1. ENTRADA DE DADOS:
total_passageiros = int(input("Digite o total de passageiros: "))
print(" ")

# 2. CONTAGEM DAS GRATUIDADES:
idoso = 0
for i in range(1, total_passageiros + 1):
    idade = int(input(f"Idade do passageiro {i}: "))
    

    if idade >= 65:
        idoso = idoso + 1

# 3. SAÍDA DE DADOS:
print(f"\nTotal de gratuidades concedidas: {idoso}")
