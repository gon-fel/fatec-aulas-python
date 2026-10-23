# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 3 - Atividade 4: Controle de Empréstimo
# ==============================================================================

print("\n--- CONTROLE DE EMPRÉSTIMO DA BIBLIOTECA ---\n")

# 1. Entrada de dados (strings):
nome_aluno = input("Digite o nome do aluno: ")
titulo_livro = input("Informe o título do livro: ")
bibliotecario_responsavel = input("Bibliotecário responsável: ")

# 2. Entrada com conversão para número inteiro (str -> int):
prazo_total = int(input("O empréstimo foi para quantos dias?: "))
dias_utilizados = int(input("Ficou quantos dias com o livro: "))

# 3. Processamento:
dias_restantes = prazo_total - dias_utilizados

# 4. Estrutura condicional (if / else) e operador relacional (>=):
if dias_utilizados >= dias_restantes:
    print(f"\nO aluno {nome_aluno} está com o livro '{titulo_livro}' em atraso!")
else:
    print(f"\nO aluno {nome_aluno} devolveu o livro '{titulo_livro}' dentro do prazo.")
    print(f"Empréstimo finalizado por {bibliotecario_responsavel}. Dias restantes: {dias_restantes}")
