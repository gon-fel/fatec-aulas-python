'''
Você foi contratado para implementar o módulo de faturamento de uma 
concessionária de energia elétrica. Crie uma função chamada 
'calcular_fatura_energia' que receba dois parâmetros: o consumo mensal 
em quilowatt-hora ('consumo_kwh') e o código da bandeira tarifária 
vigente ('bandeira' - string: "VERDE", "AMARELA" ou "VERMELHA").

Dentro da função, o cálculo deve seguir as seguintes regras:
1. O valor base da tarifa é de R$ 0,65 por kWh consumido.
2. Utilize uma estrutura condicional (if-elif-else) para calcular o 
   acréscimo da bandeira tarifária sobre cada 100 kWh consumidos 
   (use math.ceil(consumo_kwh / 100) para determinar as frações de 100 kWh):
   - Bandeira "VERDE": sem acréscimo (R$ 0,00).
   - Bandeira "AMARELA": acréscimo de R$ 1,88 por fração de 100 kWh.
   - Bandeira "VERMELHA": acréscimo de R$ 4,46 por fração de 100 kWh.
3. Some o valor base com o acréscimo da bandeira, arredonde o total 
   para 2 casas decimais com round() e armazene na variável local 'total_fatura'.

Devolva 'total_fatura' em um único ponto de saída utilizando 'return'. 
No programa principal, solicite o consumo e a bandeira ao usuário, 
chame a função e exiba o valor total a pagar.
'''
import math
def calcular_fatura_energia(consumo_kwh, bandeira):
    
    base_tarifa = consumo_kwh * 0.65

    acrescimo = math.ceil(consumo_kwh / 100)

    if bandeira == "VERDE":
        acrescimo *= 0
    elif bandeira == "AMARELA":
        acrescimo *= 1.88
    else: 
        acrescimo *= 4.46

    total_fatura = round(base_tarifa + acrescimo, 2)
    return total_fatura

bandeira = input('Informe a bandeira tarifária (VERDE, AMARELA ou VERMELHA): ').upper()

while bandeira not in ("VERDE", "AMARELA", "VERMELHA"):

    print("\nVocê não digitou uma bandeira válida. Escolha entre VERDE, AMARELA ou VERMELHA.")

    bandeira = input('\nInforme a bandeira tarifária (VERDE, AMARELA ou VERMELHA): ').upper()    

fatura = float(input('Informe o consumo de energia em kWh: '))


total = calcular_fatura_energia(fatura, bandeira)
print(f'\nO valor total a pagar é: R$ {total:.2f}')



