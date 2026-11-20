# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 4 - Tarefa de Casa 4: Controle de Economia
# ==============================================================================

# Crie um programa de controle de Economia

# Entrada de Dados

nome = input("Diga o seu nome: ")
nome_item = input(f"{nome} o que você deseja comprar? ")
loja = input(f"{nome} em que loja você encontrou o {nome_item}: ")
valor_total = int(input(f"Qual é o valor do {nome_item} (ex: R$15): R$"))
valor_guardado = int(input(f"{nome} quanto em R$ você já tem guardado (ex: R$50): R$"))

# Processamento dos Dados
valor_restante = valor_total - valor_guardado

# Saída do Dados

print(f"{nome} você deseja o(a) item: {nome_item} da loja: {loja} que está custando R${valor_total}. No momento você tem R${valor_guardado}, faltando R${valor_restante}.")