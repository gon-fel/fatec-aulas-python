# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 9 - Atividade 4: Carregamento de Caixas
# ==============================================================================

# 1. ENTRADA DE DADOS:
numero_caixa = int(input("Digite o total de caixas: "))
print("-" * 20)

# 2. CONTAGEM E SAÍDA:
for i in range(1, numero_caixa + 1):
    print(f"Carregando Caixa: {i}")
print("-" * 20)

print(f"O total de caixas carregadas foram: {numero_caixa}")