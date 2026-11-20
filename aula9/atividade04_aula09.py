# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 9 - Atividade 4: Tabuada
# ==============================================================================

# 1. ENTRADA DE DADOS:
numero = int(input("Digite o número da Tabuada: "))

# 2. CÁLCULO E SAÍDA DA TABUADA:
for tabuada in range(0,10):
    resultado = numero * tabuada
    print(f"{numero} x {tabuada}= {resultado}")