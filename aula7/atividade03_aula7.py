# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 7 - Atividade 3: Faixas de Alíquota do IRPF (Estruturas Condicionais)
# ==============================================================================

# 1. ENTRADA DE DADOS:
# Lê o salário como número decimal para verificar sua faixa de tributação.
salario = float(input("Informe o seu salário: R$"))

# 2. PROCESSAMENTO CONDICIONAL:
# Seleciona a situação ou a alíquota associada à faixa salarial.
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

# 3. SAÍDA DE DADOS:
# Exibe a situação ou a alíquota selecionada.
print(aliquota)