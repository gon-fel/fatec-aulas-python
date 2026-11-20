# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 9 - Atividade 6: Abastecimento de Litros
# ==============================================================================

# 1. ENTRADA DE DADOS:
litros = int(input("Digite a quantidade de litros a abastecer: "))
print(' ')

# 2. CONTAGEM E SAÍDA:
for i in range(1, litros + 1):
    print(f"Abastecendo... {i} litro(s)")

print(' ')

print(f"Abastecimento finalizado!")
print(f"Total: {litros} litros.")
