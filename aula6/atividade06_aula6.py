# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 6 - Atividade 6: Saldo da Conta Bancária
# ==============================================================================

'''Exercício: Saldo da Conta Bancária
Crie um programa que leia o saldo de uma conta bancária e informe se a conta está com saldo positivo/zerado ou no vermelho (negativo).

Requisitos
1. Entrada (o que ler):
saldo: Valor atual do saldo bancário em R$ (int)

2. Condição (Decisão):
Se saldo >= 0: a conta está regular.
Senão (else): a conta está no vermelho.

3. Saída:
Exibir a mensagem: "Saldo positivo ou zerado" ou "Conta no vermelho!".
Exemplo de Entrada e Saída

Cenário 1:
Digite o saldo da conta (R$): 150
Conta no azul. Você não está devendo.

Cenário 2:
Digite o saldo da conta (R$): -45
Conta no vermelho. Você está devendo!
'''

# 1. ENTRADA DE DADOS:
saldo = int(input("Valor atual do saldo bancário: R$"))

# 2. CONDIÇÃO E SAÍDA:
if saldo >= 0:
    print("Conta no azul. Você não está devendo!")

else:
    print("Conta no vermelho. Você está devendo.")
    