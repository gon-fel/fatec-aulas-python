# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 6 - Atividade 5: Radar de Velocidade
# ==============================================================================

'''
Exercício: Radar de Velocidade (60km/h)
Crie um programa que leia a velocidade de um carro e informe se o motorista ultrapassou o limite permitido na via (60 km/h).

Requisitos
1. Entrada (o que ler):
velocidade: Velocidade registrada do veículo em km/h (int)

2. Condição (Decisão):

Se velocidade > 60: o motorista foi multado.
Senão (else): a velocidade está dentro do limite permitido.

3. Saída:

Exibir a mensagem: "MULTADO: Acima do limite permitido!" ou "Dentro do limite permitido.".
Exemplo de Entrada e Saída

Cenário 1:
Digite a velocidade do carro (km/h): 75
MULTADO: Acima do limite permitido!

Cenário 2:
Digite a velocidade do carro (km/h): 50
Dentro do limite permitido.
'''

# 1. Entrada dos dados:
print("--- RADAR DE VELOCIDADE")
print('='*20, '\n')

velocidade = int(input("Velocidade registrada do veículo em km/h: "))

# 2. Condicional: 

if velocidade >= 60: # motorista multado
    print("MULTADO: Acima do limite permitido!")

else:
    print('Dentro do limite permitido.')