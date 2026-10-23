"""Cálculo do Perímetro de um Terreno Retangular

1. Entrada de Dados:
Peça a medida da largura do terreno (variável largura - número inteiro).

Peça a medida do comprimento do terreno (variável comprimento - número inteiro).

2. Processamento (Cálculo):

Como o retângulo tem 4 lados (dois de largura e dois de comprimento), calcule o perímetro usando a fórmula:

perimetro = 2*largura + 2*comprimento
3. Saída de Dados:

Mostre na tela o valor final do perímetro calculado.
"""

# 1. Entrada de Dados
print("\n--- CÁLCULO DO PERÍMETRO DE UM TERRENO RETANGULAR ---") # Inseri o "\n" no ínicio desta linha para a visualização ser melhor no terminal.
largura = int(input("Informe a largura do terreno: "))
comprimento = int(input("Informe o comprimento do terreno: "))

# 2. Processamento dos Dados
#perimetro = 2 * (largura + comprimento) # Achei melhor realizar o cálculo dessa forma para garantir a ordem de precedência. 
perimetro = 2 * largura + 2 * comprimento # Depois observei que a fórmula apresentada já respeita a ordem de precedência rsrs.

# 3. Exibição dos Resultados
print("\n" + "=" * 30)
print(f"O perimetro do terreno retangular é: {perimetro}")
print("=" * 30)
