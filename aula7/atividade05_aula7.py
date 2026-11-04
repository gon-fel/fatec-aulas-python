# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 7 - Atividade 5: Cálculo de Frete e Prazo de Entrega
# ==============================================================================

# 1. ENTRADA DE DADOS:
# Lê o valor da compra e a distância de entrega em quilômetros.
valor_compra = int(input("Valor total da compra: R$"))
distancia_km = int(input("Informe o Km total: "))

# 2. PROCESSAMENTO DO FRETE:
# Define o valor do frete de acordo com o total da compra.
if valor_compra >= 200:
    valor_frete = 0
elif valor_compra >= 100:
    valor_frete = 15
else:
    valor_frete = 30

# 3. PROCESSAMENTO DO PRAZO:
# Define o prazo estimado de acordo com a distância.
if distancia_km > 500:
    prazo_entrega = 10
elif distancia_km > 100:
    prazo_entrega = 5
else:
    prazo_entrega = 2

# 4. SAÍDA FORMATADA:
# Apresenta o valor do frete e o prazo calculado.
print(f"Valor do frete R${valor_frete}. Prazo de entrega: {prazo_entrega} dias")