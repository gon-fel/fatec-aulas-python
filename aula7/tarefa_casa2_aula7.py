# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 7 - Tarefa de Casa 2: Altura Mínima para Brinquedo
# ==============================================================================

'''
Exercício: Altura Mínima para Brinquedo no Parque
Crie um programa para a entrada de uma montanha-russa que leia a altura de uma pessoa (em centímetros) e informe se ela tem a altura mínima necessária de 140 cm para entrar.

Requisitos
1. Entrada (o que ler):
altura: Altura da pessoa em centímetros (int)

2. Condição (Decisão):
Se altura >= 140: entrada liberada no brinquedo.

Senão (else): entrada bloqueada por segurança.

3. Saída:
Exibir a mensagem: "Entrada permitida! Divirta-se!" ou "Entrada não permitida: altura abaixo do mínimo.".

Exemplo de Entrada e Saída

Cenário 1:
Digite a altura em cm: 155
Entrada permitida! Divirta-se!


Cenário 2:
Digite a altura em cm: 132
Entrada não permitida: altura abaixo do mínimo.
Meu trabalho
'''

# 1. Entrada de Dados:
altura = int(input("Informe sua altura em cm: (ex: 172): "))

# 2. Condicional:
if altura < 140:
    print("Entrada não permitida: Altura abaixo do mínimo.")

else:
    print("Entrada permitida! Divirta-se!")