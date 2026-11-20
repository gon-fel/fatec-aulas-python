# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 10 - Tarefa de Casa 3: Depósito de Moedas no Cofre
# ==============================================================================

''' Tarefa Para Casa 03 - Para Aula 10
Uma pessoa decide guardar moedas em um cofrinho. 
O programa deve receber o valor em dinheiro (R$) que o cofrinho já possui guardado e a quantidade de moedas de 2 reais que serão depositadas nessa etapa. 

No meio do programa, utilize a estrutura de repetição for para registrar a inserção de cada moeda no cofre, contando uma a uma. Ao final, após o laço, o programa calcula o montante total adicionado e exibe o saldo final acumulado.

Digite o saldo inicial do cofre (R$): 30 
Digite a quantidade de moedas de R$ 2 a guardar: 4 
Saldo inicial no cofre: R$ 30 

Inserindo moeda 1 de R$ 2 no cofre... 
Inserindo moeda 2 de R$ 2 no cofre... 
Inserindo moeda 3 de R$ 2 no cofre... 
Inserindo moeda 4 de R$ 2 no cofre... 

Moedas guardadas: 4 
Total adicionado: R$ 8 
Saldo final no cofre: R$ 38'''

# 1. ENTRADA DE DADOS:
saldo_inicial = int(input("Digite o saldo inicial do cofre (R$): "))
qtd_moedas = int(input("Digite a quantidade de moedas de R$ 2 a guardar: "))

print(f"Saldo inicial no cofre: R${saldo_inicial}\n")

# 2. REGISTRO DAS MOEDAS:
for i in range(1, qtd_moedas + 1):
    print(f"Inserindo moeda {i} de R$ 2 no cofre...")

print(f"\nMoedas guardadas: {qtd_moedas}")

# 3. CÁLCULO E SAÍDA DO SALDO:
total_adicionado = qtd_moedas * 2
print(f"Total adicionado: R$ {total_adicionado}")

saldo_final = saldo_inicial + total_adicionado
print(f"Saldo final no cofre: R$ {saldo_final}")