# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 4 - Atividade 3: Média Aritmética e Formatação de Floats (:.2f)
# ==============================================================================
# Enunciado:
# 1. Peça o nome do aluno e as notas do Trabalho, Seminário e Prova (inteiros).
# 2. Calcule a média aritmética garantindo precedência por parênteses.
# 3. Exiba o relatório com a média formatada em duas casas decimais.
# ==============================================================================

# 1. ENTRADA DE DADOS:
print("--- MÉDIA ESCOLAR ---")
nome_aluno = input("Informe o seu nome: ")
nota_trabalho = int(input("Informe a nota do Trabalho: "))
nota_seminario = int(input("Informe a nota do Seminário: "))
nota_prova = int(input("Informe a nota da Prova: "))

# 2. PROCESSAMENTO:
# O operador '/' sempre promove o resultado para float.
media = (nota_trabalho + nota_seminario + nota_prova) / 3

# 3. SAÍDA:
print("\n" + "=" * 30)
print(f"Aluno: {nome_aluno}")
print(f"Nota do Trabalho: {nota_trabalho}")
print(f"Nota do Seminário: {nota_seminario}")
print(f"Nota da Prova: {nota_prova}")
print("=" * 30)
# :.2f formata a exibição do float com duas casas decimais:
print(f"{nome_aluno}, sua média final é: {media:.2f}\n")
