# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 7 - Lista de Exercícios, Questão 8: Peso e Distância da Carga
# ==============================================================================

# 1. Entrada de dados

peso_kg = int(input("Informe o peso da carga em Kg: "))
distancia_km = int(input("Informe a km total "))

print(f"Peso (kg): {peso_kg}\nDistância (km): {distancia_km}")
print("-" * 30, "\n")

# 2. Estrutura Condicional 1 e Saída de Dados
if peso_kg <= 5:
    print("Modal: 1")
elif peso_kg <= 30:
    print("Modal: 2")
else:
    print("Modal: 3") 

# 2. Estrutura Condicional 2 e Saída de Dados
if distancia_km <= 50:
    print("Zona: 10")
elif distancia_km <= 250:
    print("Zona: 20")
else:
    print("Zona: 30")