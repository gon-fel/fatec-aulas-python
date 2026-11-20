# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 7 - Tarefa de Casa 3: Comparação entre Dois Números
# ==============================================================================

'''
Exercício: Comparação Entre Dois Números (Maior Valor)
Crie um programa que leia dois números inteiros diferentes e informe qual deles é o maior.

Requisitos
1. Entradas (o que ler):

numero1: Primeiro número inteiro (int)
numero2: Segundo número inteiro (int)

2. Condição (Decisão):

Se numero1 > numero2: o primeiro é o maior.
Senão (else): o segundo é o maior.

3. Saída:

Exibir a mensagem informando qual dos dois valores é o maior.
Exemplo de Entrada e Saída

Cenário 1:
Digite o primeiro número: 45
Digite o segundo número: 12
O maior número é: 45

Cenário 2:
Digite o primeiro número: 7
Digite o segundo número: 20
O maior número é: 20
'''

# 1. ENTRADA DE DADOS:
numero1 = int(input("Informe o número 1: "))
numero2 = int(input("Informe o numero 2: "))

# 2. CONDIÇÕES E SAÍDA:
if numero1 > numero2:
    print(f"O número maior é: {numero1}")
elif numero2 > numero1:
    print(f"O número maior é: {numero2}")
else:
    print("")
