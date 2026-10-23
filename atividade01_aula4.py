'''Criar o programa abaixo e estudar conforme a solução.
Faça um programa que calcule a área do retângulo

1. Entrada de Dados:
Peça a medida da base do retângulo  - variável base(número inteiro).
Peça a medida da altura do retângulo  - variável altura (número inteiro).

2. Processamento (Cálculo):
Calcule a área multiplicando os dois valores:
area = base * altura

3. Mostre o resultado com mensagem adequada (print)

# 1. Entrada de dados
print("--- CÁLCULO DE ÁREA DO RETÂNGULO ---")
base = int(input("Digite a medida da base: "))
altura = int(input("Digite a medida da altura: "))

# 2. Processamento (Cálculo direto)
area = base * altura

# 3. Exibição do resultado
print("\n==============================")
print("A área do retângulo é:", area)
print("==============================")
'''

# 1. Entrada de Dados
print("--- CÁLCULO DE ÁREA DE RETÂNGULO ---")
base = int(input("Digite a medida da base: "))
altura = int(input("Digite a medida da altura: "))

# 2. Processamento 
area = base * altura

# 3. Exibição do resultado
print("\n" + "=" *30)
print(f"A área do retângulo é: {area}")
print("=" *30)
