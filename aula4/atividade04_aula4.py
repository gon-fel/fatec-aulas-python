# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 4 - Atividade 4: Custo de Combustível da Viagem
# ==============================================================================

'''Cálculo do Custo de Combustível da Viagem
Criar um programa para calcular o valor total gasto com combustível em um passeio, usando multiplicação simples com números inteiros.

O que o seu programa deve fazer:
1. Entrada de Dados:

Ler a quantidade de litros abastecidos (variável litros - número inteiro).
Ler o preço de cada litro em reais inteiros (variável preco - número inteiro).

2. Processamento (Cálculo Simples):

Multiplicar a quantidade de litros pelo preço de cada litro:

custo_total =  litros * preco
3. Saída de Dados:

Exibir a quantidade abastecida, o preço unitário e o valor total a pagar.
'''

# 1. Entrada dos Dados
print("--- CÁLCULO DO CUSTO DE COMBUSTÍVEL DA VIAGEM ---\n")
litros_abastecido = int(input("Informe quantos litros foi abastecido (ex 3): "))
preco_litro = int(input("Informe o valor do litro (R$ 5): R$")) 

# 2. Processamento dos Dados 
custo_total = litros_abastecido * preco_litro

# 3. Resultado
print(f"Foi abastecido: {litros_abastecido} litros de combustível")
print(f"O preço do litro é de: R$ {preco_litro:.2f}")
print(f"O valor total pago foi: R$ {custo_total:.2f}")