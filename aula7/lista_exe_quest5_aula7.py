# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 7 - Lista de Exercícios, Questão 5: Classificação de Pressão
# ==============================================================================

# 1. Entrada de dados

pressao_psi = int(input("Informe a pressão em PSI: "))

print(f"Entrada (PSI): {pressao_psi}")

if pressao_psi < 50:
    print("Saída: 1")
elif pressao_psi <= 120:
    print("Saída: 2")
else:
    print("Saída: 3")