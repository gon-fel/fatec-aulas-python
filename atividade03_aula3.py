# Entrada dos Dados
nome_produto = input("Informe o nome do produto: ")
funcionario_responsavel = input("Informe o nome do funcinário responsável: ")
setor_estoque = input("Informe o setor que o produto vai ficar: ")
estoque_inicial = int(input("Informe a quantidade comprada (ex: 10, 20...): "))
itens_vendidos = int(input("Informe a quantidade de itens vendidas hoje: "))

# Processamento dos Dados

vendas_do_dia = estoque_inicial - itens_vendidos


# Saída dos Dados
print("=" * 30 ,"\n")
print(f"Nome do produto: {nome_produto}")
print(f"Funcinário responsável: {funcionario_responsavel}")
print(f"Setor do estoque: {setor_estoque}")
print(f"Quantidade Inicial: {estoque_inicial}")
print(f"Quantidade vendida hoje: {itens_vendidos}")
print("=" * 30, "\n")
print(f"Foi vendido: {itens_vendidos} itens do(a) {nome_produto}. O funcionário responsável pelas vendas foi o(a) {funcionario_responsavel}.\nHaviam {estoque_inicial} itens do {nome_produto} no setor {setor_estoque}.")
print(f"Foram vendidos {itens_vendidos} itens. Permanecendo no estoque {vendas_do_dia} unidades do produto {nome_produto}")


