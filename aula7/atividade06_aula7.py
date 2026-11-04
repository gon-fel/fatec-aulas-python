# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 7 - Atividade 6: Tarifação de Energia e Nível de Alerta
# ==============================================================================

# 1. APRESENTAÇÃO DO EXERCÍCIO:
# Exibe o título da atividade no terminal.
print("-" * 30, "\n TARIFAÇÃO DE ENERGIA E NÍVEL DE ALERTA\n", "-" * 30)

# 2. ENTRADA DE DADOS:
# Lê o consumo mensal de energia em quilowatts-hora.
consumo_kwh = int(input("Digite o consumo mensal (Kwh): "))

# 3. PROCESSAMENTO CONDICIONAL:
# Define a tarifa, o nível e a mensagem de alerta para a faixa de consumo.
if consumo_kwh > 300:
    tarifa = 3
    nivel = 3
    alerta = "Alerta Vermelho: Consumo excessivo"
elif consumo_kwh <= 300 and consumo_kwh > 100:
    tarifa = 2
    nivel = 2
    alerta = "Alerta Amarelo: Consumo moderado"
else:
    tarifa = 1
    nivel = 1
    alerta = "Alerta Verde: Consumo econômico"

# 4. SAÍDA DE DADOS:
# Exibe a tarifa e o nível de alerta definidos.
print(f"Tarifa R$ {tarifa} por Kwh.\nNível de Alerta: {nivel}\n{alerta}")