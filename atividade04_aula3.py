print("\n--- CONTROLE DE EMPRÉSTIMO  DA BIBLIOTECA --- \n")

# Captura dos Dados
nome_aluno = input("Digite o nome do aluno: ")
titulo_livro = input("Informe o título do livro: ")
bibliotecario_responsavel = input("Bibliotecário responsável: ")
prazo_total = int(input("O empréstimo foi para quantos dias?: "))
dias_utilizados = int(input("Ficou quantos dias com o livro: "))

# Processamento dos Dados

dias_restantes = prazo_total - dias_utilizados

# Saída dos Dados


if dias_utilizados >= dias_restantes:
    print("Você devolveu o livbro em atrasado. Isso gerará uma multa.")

else:
    print(f"O aluno(a) {nome_aluno}, emprestou o livro {titulo_livro} por {prazo_total} dias. Esse empréstimo foi efetivado pelo bibliotecário {bibliotecario_responsavel}, permanecendo com o livro por {dias_utilizados} dias. ")
