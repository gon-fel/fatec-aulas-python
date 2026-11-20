# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 9 - Atividade 5: Registro de Passageiros
# ==============================================================================

# 1. ENTRADA DE DADOS:
qtd_passageiros = int(input("Digite o total de passageiros: "))
print(" ")

# 2. CONTAGEM E SAÍDA:
for i in range(1, qtd_passageiros +1):
    print(f"Passageito {i} passou pela catraca.")

print(" ")
print(f"Total de passageiros registrados: {qtd_passageiros}")