# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 4 - Atividade 5: Divisão da Conta da Pizzaria
# ==============================================================================

'''Divisão da Conta da Pizzaria
Vamos criar um programa que simula uma situação clássica do cotidiano: calcular o valor total de uma conta de pizzaria (com refrigerantes) e depois dividir esse valor igualmente entre os amigos da mesa.

Contexto do Problema
Cálculo Inicial (X - Conta Total): Somar o valor total das pizzas com o total das bebidas.
Cálculo Final (Y - Valor por Pessoa): Dividir a conta total (X) pela quantidade de pessoas na mesa.

O que o seu programa deve fazer:
1. Entrada de Dados:
Valor total gasto com as pizzas em reais (int)
Valor total gasto com os refrigerantes em reais (int)
Quantidade de amigos que vão dividir a conta (int)

2. Processamento (2 Etapas de Cálculo):
Cálculo Preliminar (X): Valor total da mesa: 
X = gasto_pizzas + gasto_refrigerantes
Cálculo Final (Y): Valor que cada um deve pagar (divisão real):
Y = X / total_amigos

3. Saída de Dados:
Exibir o total da conta (X) e o valor que cabe a cada amigo (Y).
'''

# 1. Entrada dos Dados
print("--- DIVISÃO DA CONTA DA PIZZARIA ---\n")

valor_total_pizzas = int(input("Informe o valor total gasto em pizzas: R$ "))
valor_total_refrigerante = int(input("Informe o valor total gasto com refrigerante: R$"))
quantidade_amigos = int(input("Será dividido entre quantos amigos?: "))

# 2. Processamento
gasto_total1 = valor_total_pizzas + valor_total_refrigerante
gasto_total2 = gasto_total1 / quantidade_amigos

# 3. Resultado
print("=" * 30)
print("DIVISÃO DA CONTA DA PIZZARIA")
print("=" * 30)
print(f"O valor total consumido em pizzas foi: R${valor_total_pizzas:.2f}")
print(f"O valor total consumido em refrigerantes foi: R${valor_total_refrigerante:.2f}")
print(f"O valor total da conta foi R${gasto_total1:.2f} e será dividida entre {quantidade_amigos} amigos.")
print(f"Cada um pagará R${gasto_total2:.2f}.")

