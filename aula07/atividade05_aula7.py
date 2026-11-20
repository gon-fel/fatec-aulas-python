# ==========================================
# Atividade 05 - Aula 07: Cálculo de Frete e Prazo
# Descrição: Calcula o valor do frete por faixa de valor de compra e prazo por distância.
# ==========================================

# 1. Entrada de Dados
valor_compra = int(input("Valor total da compra: R$"))
distancia_km = int(input("Informe o Km total: "))

# 2. Estrutura Condicional 1: Cálculo do Frete
if valor_compra >= 200:
    valor_frete = 0
elif valor_compra >= 100:
    valor_frete = 15
else:
    valor_frete = 30

# 3. Estrutura Condicional 2: Cálculo do Prazo de Entrega
if distancia_km > 500:
    prazo_entrega = 10
elif distancia_km > 100:
    prazo_entrega = 5
else:
    prazo_entrega = 2

# 4. Saída de dados formatada
print(f"Valor do frete R${valor_frete}. Prazo de entrega: {prazo_entrega} dias")