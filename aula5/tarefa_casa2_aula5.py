# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 5 - Tarefa de Casa 2: Delta da Equação do Segundo Grau
# ==============================================================================

'''Cálculo do Delta da Equação do 2º Grau
Criar um programa que calcula o valor do Delta em uma equação do segundo grau. 

A fórmula matemática do discriminante é: $ \ Delta = b^2 - 4 \ cdot a \ cdot c$
1. Entrada de Dados:
Ler o Coeficiente a (número inteiro)
Ler o Coeficiente b (número inteiro)
Ler o Coeficiente c (número inteiro)

2. Cálculos:
Cálculo Preliminar (X): Quadrado de b:
X = b * b
Cálculo Final (Y): Valor de Delta:
Delta = X - (4 * a * c)

3. Saída de Dados:
Exibir os coeficientes digitados, o valor de b e o resultado final do Delta.
'''

# 1. Entrada de Dados
print("--- CÁLCULO DO DELTA ---\n")
coeficiente_a = int(input("Informe o valor do coeficiente 'a': "))
coeficiente_b = int(input("Informe o valor do coeficiente 'b': "))
coeficiente_c = int(input("Informe o valor do coeficiente 'c': "))

# 2. Processamento dos Dados
coeficiente_b2 = coeficiente_b * coeficiente_b
delta = coeficiente_b2 - (4 * coeficiente_a * coeficiente_c)

# 3. Saída dos Dados
print("\n--- CÁLCULO DO DELTA ---")
print(f"Coeficiente 'a' informado: {coeficiente_a}")
print(f"Coeficiente 'b' informado: {coeficiente_b}")
print(f"Coeficiente 'c' informado: {coeficiente_c}")
print(f"O coeficiente b² é: {coeficiente_b2} e o valor de delta é: {delta}")