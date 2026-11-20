# ==========================================
# Atividade 02 - Aula 14: Criando funções
# Descrição: Você deve desenvolver uma função em Python para avaliar o desempenho de um estudante. Crie uma função chamada 'verificar_situacao' que receba três notas (n1, n2 e n3) como parâmetros. Dentro da função, calcule a média aritmética simples das três notas. Em seguida, utilize uma estrutura condicional (if-else) para avaliar o resultado: se a média for maior que 6, atribua o texto "Aprovado" a uma variável auxiliar de situação; caso contrário, atribua o texto "Reprovado". Ao final da função, retorne essa variável em um único ponto de saída com o comando 'return'. No programa principal, solicite as três notas do estudante, chame a função que você criou passando essas notas como argumentos e exiba na tela a situação final retornada.
# ==========================================

def verificar_situacao (a, b, c):
    media = (a + b + c) / 3

    if media > 6:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    return situacao


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

resultado = verificar_situacao(nota1, nota2, nota3)

print(f"\nSituação final do aluno: {resultado}")
