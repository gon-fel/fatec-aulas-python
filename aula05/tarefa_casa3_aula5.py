# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 5 - Tarefa de Casa 3: Força Resultante e Aceleração
# ==============================================================================

'''
Cálculo da Força Resultante e Aceleração 
Criar um programa de mecânica clássica que calcula a aceleração de um bloco sujeito a duas forças horizontais opostas.

1. Entrada de Dados:
Força principal para a direita em Newtons (variável forca_direita - int)
Força contrária/atrito para a esquerda em Newtons (variável forca_esquerda - int)
Massa do bloco em kg (variável massa - int)

2. Processamento (2 Etapas de Cálculo):
Cálculo Preliminar (X): Força resultante: X = forca_direita - forca_esquerda
Cálculo Final (Y): Aceleração gerada (divisão real): Y = X / massa

3. Saída de Dados:
Exibir a força resultante (X) e o valor final da aceleração (Y) em m/s².
'''

# 1. ENTRADA DE DADOS:
print("--- CÁLCULO DA FORÇA RESULTANTE E ACELERAÇÃO ---")
forca_direita = int(input("Informe a força da direita em N: "))
forca_esquerda = int(input("Informe a força da esquerda em N: "))
massa = int(input("Informe a massa do bloco em kg: "))

# 2. PROCESSAMENTO:
forca_resultante = forca_direita - forca_esquerda
aceleracao = forca_resultante / massa

# 3. SAÍDA DE DADOS:
print("\n" + "=" * 20)
print("CÁLCULO DA FORÇA RESULTANTE E ACELERAÇÃO")
print("=" * 20)
print(f"Força resultante: {forca_resultante}N")
print(f"Aceleração final: {aceleracao:.2f}m/s²")
