# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 9 - Atividade 8: Entrada de Caixas no Estoque
# ==============================================================================

# 1. ENTRADA DE DADOS:
estoque_inicial = int(input("Digite o estoque inicial: "))
qtd_caixas_novas = int(input("Digite a quantidade de caixas novas: "))


print(f"\nEstoque inicial confirmado: {estoque_inicial} caixas.\n")

# 2. REGISTRO DAS CAIXAS:
for i in range(1, qtd_caixas_novas + 1):
    print(f"Registrando entrada: Caixa {i}")

# 3. CÁLCULO E SAÍDA DO ESTOQUE FINAL:
estoque_final = estoque_inicial + qtd_caixas_novas

print(f"\nTotal de caixas adicionadas: {qtd_caixas_novas}")
print(f"Estoque final atualizado: {estoque_final} caixas")
