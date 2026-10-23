'''Média Escolar
Vamos calcular a média das avaliações de um aluno, somando as notas das três atividades e calculando a média inteira.

O que o seu programa deve fazer:
1. Entrada de Dados:

Ler a nota do Trabalho (número inteiro).
Ler a nota do Seminário (número inteiro).
Ler a nota da Prova (número inteiro).

2. Processamento (Cálculo):

Somar as três notas usando parênteses para garantir a ordem correta da soma.
total = trabalho + seminario + prova

Dividir o total por 3 utilizando a divisão / :

media = total / 3
3. Saída de Dados:

Exibir a média final do aluno.
'''

# 1. Entrada de Dados
print("--- MÉDIA ESCOLAR ---")
nome_aluno = input("Informe o seu nome: ")
nota_trabalho = int(input("Informe a nota do Trabalho: "))
nota_seminario = int(input("Informe a nota do Seminário: "))
nota_prova = int(input("Informe a nota da Prova: "))

# 2. Processamento dos dados
media = (nota_trabalho + nota_seminario + nota_prova) / 3

# 3. Exibição do Resultado
print("\n--- MÉDIA ESCOLAR ---")
print(nome_aluno)
print(f"Nota do Trabalho: {nota_trabalho}")
print(f"Nota do Seminário: {nota_seminario}")
print(f"Nota da Prova: {nota_prova}")
print("=" * 30)
print(f"{nome_aluno} sua média é: {media:.2f}")


      