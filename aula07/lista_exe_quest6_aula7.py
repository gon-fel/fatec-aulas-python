# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 7 - Lista de Exercícios, Questão 6: Faixas de Consumo de Água
# ==============================================================================

# 1. Entrada de dados

consumo_m3 = int(input("Informe o volume total faturado no mês: "))

print(f"Entrada (m³): {consumo_m3}")


# 2. Condicional e saída de dados

if consumo_m3 <= 10:
    print("Saída: R$ 5/m³")
elif consumo_m3 <= 30:
    print("Saída: R$ 8/m³")
elif consumo_m3 <=60:
    print("Saída: R$ 12/m³")
else:
    print("Saída: R$ 15/m³")

