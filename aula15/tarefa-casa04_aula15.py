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

import math
def calcular_rendimento (valor_aplicado, meses):
    montante = valor_aplicado * math.pow(1 + 0.012, meses)

    valor_final = round(montante, 2)

    return valor_final

print('\n --- MENU DE OPÇÕES ---')
print('[1] Simular novo investimento')
print('[2] Encerrar simulador')

menu = int(input('Escolha uma opção: '))
while menu != 2:
    
    valor_investimento = float(input('Informe o valor do aporte: R$'))
    meses = int(input('Informe a quantidade de meses: '))

    aplicacao = calcular_rendimento(valor_investimento, meses)

    print('\n --- MENU DE OPÇÕES ---')
    print('[1] Simular novo investimento')
    print('[2] Encerrar simulador')
    menu = int(input('Escolha uma opção: '))

    print(aplicacao)