# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 10 - Tarefa de Casa 02: Inspeção de Peso de Caixas
# ==============================================================================

# 1. ENTRADA DE DADOS:
qta_caixas = int(input("Digite a quantidade de caixas: "))

# 2. INSPEÇÃO E SAÍDA:
for i in range(1, qta_caixas + 1):
    peso = int(input(f"Peso da Caixa {i}: "))
   
    if peso <= 50:
        print(f"Caixa {i} -> Carga Liberada para embarque")
    else:
        print(f"Caixa {i} -> ALERTA: Peso Excedido")
