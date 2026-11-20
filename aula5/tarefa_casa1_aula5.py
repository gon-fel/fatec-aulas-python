# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 5 - Tarefa de Casa 1: Fechamento de Turno de Motorista
# ==============================================================================

'''Fechamento de Turno de um Motorista de Aplicativo
Criar um programa que simula o cálculo financeiro diário de um motorista de aplicativo, passando por três etapas sequenciais de cálculo até chegar no lucro líquido por hora trabalhada.

Contexto do Problema
Um motorista precisa saber:
Valor X (Ganho Bruto): Quanto ele faturou no total com as corridas.
Valor Y (Gasto com Combustível): Quanto ele gastou para abastecer o carro no dia.
Valor Z (Lucro Líquido por Hora): Quanto sobrou no bolso para cada hora trabalhada, após descontar o combustível.

O que o seu programa deve fazer:

1. Entrada de Dados:
Quantidade de corridas realizadas no dia (int)
Valor médio recebido por corrida (int)
Quantidade de litros de combustível gastos (int)
Preço de cada litro de combustível (int)
Total de horas trabalhadas no dia (int)

2. Processamento (3 Etapas de Cálculo):
Cálculo Inicial: Ganho bruto total:
X = corridas * valor_por_corrida
Cálculo Intermediário: Gasto total com combustível:
Y = litros * preco_litro
Cálculo Final: Lucro líquido gerado por hora:
Z = (X - Y) / horas_trabalhadas
3. Saída de Dados:

Exibir o ganho bruto, o gasto, o lucro líquido restante e o rendimento final por hora Z.
'''

# 1. Entrada de Dados
print('--- FECHAMENTO DE TURNO DE UM MOTORISTA DE APLICATIVOA ---\n')
nome_motorista = input("Informe o seu nome: ")
corridas_dia = int(input("Informe quantas corridas foram realizadas hoje: "))
valor_corrida = int(input("Informe o valor médio recebido por cada corrida: R$ "))
litros_gasto_dia = int(input("Informe a quantidade de litros de combustível gasto no dia: "))
preco_combustivel = int(input("Informe o valor do litro de combustível: R$ "))
horas_trabalhadas = int(input("Informe quantas horas você trabalhou hoje: "))

# 2. Processamento dos dados
ganho_bruto = corridas_dia * valor_corrida
gasto_total = litros_gasto_dia * preco_combustivel
lucro_restante = ganho_bruto - gasto_total
rendimento_hora = (ganho_bruto - gasto_total) / horas_trabalhadas

# 3. Resultados
print("\n--- FECHAMENTO DE TURNO ---")
print(f"Olá {nome_motorista}.\nSegue abaixo o seu Fechamento de Turno") 
print(f"Faturamento bruto: R${ganho_bruto}")
print(f"Gasto total: R$ {gasto_total}")
print(f"Faturamento líquido: R$ {lucro_restante}")
print(f"Rendimento por hora: R$ {rendimento_hora:.2f}")

'''Não sei se foi de propósito, mas no enunciado ficou faltando um cálculo, que é o de lucro restante. O professor já colocou direto como rendimento por hora. Acho que foi de propósito, mas também acredito que o resto da turma mandará faltando esse cálculo.'''
