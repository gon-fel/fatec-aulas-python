# ==========================================
# Atividade 03 - Aula 07: Cálculo de Alíquota IRPF
# Descrição: Determina a situação ou alíquota aplicável conforme o salário.
# ==========================================

# 1. Entrada de Dados
salario = float(input("Informe o seu salário: R$"))

# 2. Estrutura Condicional para faixas de imposto de renda
if salario <= 2259.20:
    aliquota = "Situação: Isento de IRPF"
elif salario <= 2826.65:
    aliquota = "Alíquota aplicada: 7.5%"
elif salario <= 3751.05:
    aliquota = "Alíquota aplicada: 15.0%"
elif salario <= 4664.68:
    aliquota = "Alíquota aplicada: 22.5%"
else:
    aliquota = "Alíquota aplicada: 27.5%"

# 3. Saída de Dados
print(aliquota)