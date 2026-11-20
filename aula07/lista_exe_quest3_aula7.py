# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 7 - Lista de Exercícios, Questão 3: Volume do Reservatório
# ==============================================================================

# 1. Entrada de Dados
print("=" * 30, "\nBALANÇO HÍDRICO DE RESERVATÓRIO\n", "=" * 30)

volume_litros = int(input("Informe o volume medido no reservatário em litros: "))

print(f"Volume (L): {volume_litros}")

if volume_litros < 500:
    print("Saída: 1")
else:
    print("Saída: 0")