# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 7 - Lista de Exercícios, Questão 2: Monitoramento de Tensão
# ==============================================================================

# 1. Entrada de Dados
print("=" * 20,"\nMONITORIZAMENTO DE TENSÃO DE REDE\n","=" * 20)

tensao = int(input("Informe o valor instantÂneo da tensão em volts: "))

print(f"Entrada (V): {tensao}")

if tensao > 135:
      print("1 - Alarme ativado.")
else:
     print("0 - Operação normal.")

print("_" * 30)
