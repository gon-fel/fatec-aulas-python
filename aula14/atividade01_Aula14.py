# ==========================================
# Atividade 01 - Aula 14: Criando funções
# Descrição: Você deve criar a sua própria função em Python para comparar dois valores numéricos. Desenvolva uma função chamada 'encontrar_maior' que receba dois números como parâmetros (a e b). Dentro da função, utilize uma estrutura condicional (if-else) para identificar qual dos dois valores é o maior e devolva esse resultado utilizando o comando 'return'. No programa principal, solicite dois números ao usuário, chame a função que você criou passando esses valores como argumentos e exiba o maior número retornado na tela.
# ==========================================

def encontrar_maior(a, b): 
    if a > b:
        resultado = a
    else:
        resultado = b

    return resultado

num1 = float(input("\nDigite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

maior = encontrar_maior(num1, num2)

print(f"\nO maior número digitado foi: {maior}")

