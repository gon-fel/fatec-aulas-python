'''
ENUNCIADO:
Você deve desenvolver um sistema de caixa para uma loja de eletrônicos. 
Primeiro, crie uma função chamada 'calcular_preco_final' que receba o 
valor de um produto ('valor_produto') como parâmetro.

Dentro da função, utilize if-elif-else para aplicar o desconto conforme 
a faixa de preço:
- Valor menor que R$ 100,00: sem desconto (0%).
- Valor de R$ 100,00 até R$ 500,00: desconto de 10%.
- Valor acima de R$ 500,00: desconto de 20%.

Armazene o valor já com o desconto aplicado na variável local 'preco_com_desconto' 
e devolva-o em um único 'return' no final da função.

No programa principal, solicite quantos produtos o cliente está comprando. 
Utilize um laço 'for' para ler o preço de cada produto, chame a função 
'calcular_preco_final' para obter o valor com desconto de cada item, 
exiba o preço com desconto individual e acumule o total geral da compra 
para exibir ao final do laço.
'''

def calcular_preco_final (valor_produto):
    if valor_produto < 100:
        valor_desconto = 0
    elif valor_produto <= 500:
        valor_desconto = valor_produto * 0.10
    else:
        valor_desconto = valor_produto * 0.20

    preco_com_desconto = valor_produto - valor_desconto
    return preco_com_desconto

total_produto = 0
qtd_produto = int(input('Informe quantos produtos irá comprar: '))

for i in range(qtd_produto):
    valor = float(input(f'\nInforme o valor do produto {i+1}: R$'))

    preco_com_desconto = calcular_preco_final(valor)
    print(f'Preço com desconto do produto {i+1}: R${preco_com_desconto:.2f}')

    total_produto += preco_com_desconto

print(f"\nVocê irá comprar {qtd_produto} produtos.")
print(f'Total da compra: R${total_produto:.2f}')