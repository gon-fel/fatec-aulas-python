# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 7 - Tarefa de Casa 4: Controle de Estoque Mínimo
# ==============================================================================

"""
Exercício: Controle de Estoque Mínimo
Crie um programa para uma loja que leia a quantidade atual de um produto em estoque e verifique se o nível está abaixo da quantidade mínima recomendada de segurança (10 unidades).

Requisitos
1. Entrada (o que ler):
quantidade_estoque: Quantidade de unidades do produto no estoque (int)

2. Condição (Decisão):
Se quantidade_estoque < 10: nível crítico, precisa repor.
Senão (else): estoque dentro do nível seguro.

3. Saída:
Exibir a mensagem: "ALERTA: Estoque baixo! Fazer reposição." ou "Estoque suficiente.".

Exemplo de Entrada e Saída

Cenário 1:
Digite a quantidade em estoque: 6
ALERTA: Estoque baixo! Fazer reposição.


Cenário 2:
Digite a quantidade em estoque: 25
Estoque suficiente.
"""


# 1. Entrada de Dados:
quantidade_estoque = int(input("Informe a quantidade de produto em estoque: "))

# 2. Condições:
if quantidade_estoque < 10:
    print("Estoque baixo! Fazer reposição.")

else:
    print("Estoque suficiente.")