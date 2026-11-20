'''
Você está criando um simulador financeiro para calcular o rendimento de 
aplicações de renda fixa. Crie uma função chamada 'calcular_rendimento' 
que receba dois parâmetros: o valor do aporte ('valor_aplicado') e o 
prazo em meses ('meses').

Dentro da função, calcule o montante final utilizando juros compostos 
com uma taxa fixa de 1,2% ao mês (0.012), empregando math.pow():
montante = valor_aplicado * math.pow(1 + 0.012, meses)

Arredonde o montante para 2 casas decimais com round() e retorne esse 
valor em um único ponto de saída com 'return'.

No programa principal, construa um menu controlado por um laço 'while' 
com as opções:
[1] Simular novo investimento
[2] Encerrar simulador

Enquanto o usuário não escolher "2", solicite o valor a investir e a 
quantidade de meses, chame a função 'calcular_rendimento' e exiba o 
montante final e o lucro obtido (montante - valor_aplicado). Ao escolher 
"2", encerre o laço com uma mensagem de despedida.
'''

# Função para calcular o rendimento do investimento 
import math
def calcular_rendimento (valor_aplicado, meses):
    montante = valor_aplicado * math.pow(1 + 0.012, meses) # montante recebe math.pow(1 + 0,012, meses) 1 = 100% do valor aplicado + 1,2% (0.012) de juros elevado ao número de meses aplicado, portanto o cálculo seria (1 + 0.012)**meses.

    valor_final = round(montante, 2) # arredondamento do valor para 2 casas decimais.

    return valor_final



print('\n --- MENU DE OPÇÕES ---')
print('[1] Simular novo investimento')
print('[2] Encerrar simulador')

menu = int(input('Escolha uma opção: '))
while menu != 2: # início do laço de repetição lógico.

    if menu == 1: # Estrutura condicional para validar a escolha do usuário, caso tenha escolhido um número diferente de "1 ou 2", o else mostrar um erro, garantindo que o programa continue rodando.
        valor_investimento = float(input('Informe o valor do aporte: R$'))
        meses = int(input('Informe a quantidade de meses: '))

        aplicacao = calcular_rendimento(valor_investimento, meses)
        print(f"Montante final: R${aplicacao:.2f}")
    
        lucro = aplicacao - valor_investimento

        print(f"Juros acumulados: R${lucro:.2f}")

    else:
        print("Opção errada!")


    print('\n --- MENU DE OPÇÕES ---')
    print('[1] Simular novo investimento')
    print('[2] Encerrar simulador')
    menu = int(input('Escolha uma opção: '))

print("Simulador encerrado.")

 