# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 9 - Atividade 3: Contagem entre Dois Valores
# ==============================================================================

# 1. ENTRADA DE DADOS:
n1 = int(input("Digite o valor inicial: "))
n2 = int(input("Digite o valor final: "))

print("-" * 10)

print(f"O valor inicial foi: {n1}. \nO valor final foi: {n2}.")

print("-" * 10)

# 2. CONTAGEM E SAÍDA:
for i in range(n1, n2 + 1):
    print(f"O valor da variável i= {i}")

