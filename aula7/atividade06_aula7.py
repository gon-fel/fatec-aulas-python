# ==========================================
# Atividade 06 - Aula 07: Tarifação de Energia e Alerta
# Descrição: Calcula tarifa e nível de alerta com base no consumo mensal em kWh.
# ==========================================

print("-" * 30, "\n TARIFAÇÃO DE ENERGIA E NÍVEL DE ALERTA\n", "-" * 30)

# 1. Entrada de dados
consumo_kwh = int(input("Digite o consumo mensal (Kwh): "))

# 2. Estrutura Condicional para tarifação e níveis de alerta
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

# 3. Saída de dados
print(f"Tarifa R$ {tarifa} por Kwh.\nNível de Alerta: {nivel}\n{alerta}")