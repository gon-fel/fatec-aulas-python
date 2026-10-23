# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 3 - Atividade 3: Controle de Estoque (I/O, Casting e Processamento)
# ==============================================================================

# 1. ENTRADA DE DADOS:
nome_produto = input("Informe o nome do produto: ")
funcionario_responsavel = input("Informe o nome do funcionário responsável: ")
setor_estoque = input("Informe o setor em que o produto vai ficar: ")

# Casting obrigatório (str -> int) para permitir cálculo aritmético:
estoque_inicial = int(input("Informe a quantidade comprada/inicial: "))
itens_vendidos = int(input("Informe a quantidade de itens vendidos hoje: "))

# 2. PROCESSAMENTO ARITMÉTICO:
# Cálculo do saldo restante em estoque após as saídas do dia:
estoque_final = estoque_inicial - itens_vendidos

# 3. SAÍDA FORMATADA (Relatório de Fechamento):
print("\n" + "=" * 35)
print("     RELATÓRIO DE ESTOQUE")
print("=" * 35)
print(f"Produto: {nome_produto}")
print(f"Funcionário: {funcionario_responsavel}")
print(f"Setor de Armazenamento: {setor_estoque}")
print(f"Quantidade Inicial: {estoque_inicial} unidades")
print(f"Saídas no Dia: {itens_vendidos} unidades")
print(f"Saldo em Estoque: {estoque_final} unidades")
print("=" * 35 + "\n")

# Síntese textual com interpolação de strings:
print(f"Foram vendidos {itens_vendidos} itens do produto '{nome_produto}'.")
print(f"Responsável pelo fechamento: {funcionario_responsavel}.")
print(f"Havia {estoque_inicial} unidades no setor {setor_estoque}; restam {estoque_final} no estoque.")
