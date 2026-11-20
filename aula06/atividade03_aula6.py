# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 6 - Atividade 3: Cálculo Salarial Semanal (I/O, Casting e Expressões)
# ==============================================================================

# 1. ENTRADA DE DADOS:
# Casting obrigatório (str -> int) para contagem de horas e valores nominais inteiros:
hora_normal = int(input("Informe a quantidade de horas normais trabalhadas na semana: "))
valor_hora = int(input("Informe o valor pago por cada hora normal (R$): "))
horas_extras = int(input("Informe a quantidade de horas extras trabalhadas na semana: "))
valor_hora_extra = int(input("Informe o valor pago por cada hora extra (R$): "))

# 2. PROCESSAMENTO ARITMÉTICO:
# Cálculo segregado de rendimentos e composição do salário total bruto
ganho_normal = hora_normal * valor_hora
ganho_extra = horas_extras * valor_hora_extra
salario_total = ganho_normal + ganho_extra

# 3. SAÍDA FORMATADA (Demonstrativo de Pagamento Semanal):
print("\n" + "=" * 45)
print("       DEMONSTRATIVO DE SALÁRIO SEMANAL      ")
print("=" * 45)
print(f"Horas Normais     : {hora_normal}h  | Valor Unitário: R$ {valor_hora},00")
print(f"Horas Extras      : {horas_extras}h  | Valor Unitário: R$ {valor_hora_extra},00")
print("-" * 45)
print(f"Total Horas Normais: R$ {ganho_normal},00")
print(f"Total Horas Extras : R$ {ganho_extra},00")
print("-" * 45)
print(f"Salário Total      : R$ {salario_total},00")
print("=" * 45 + "\n")