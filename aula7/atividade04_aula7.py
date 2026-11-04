# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 7 - Atividade 4: Conceito Escolar por Faixa de Nota
# ==============================================================================

# 1. APRESENTAÇÃO DO EXERCÍCIO:
# Exibe o título antes de solicitar a nota.
print("=" * 30)
print("Conceito de Nota Escolar")
print("=" * 30)

# 2. ENTRADA DE DADOS:
# Lê a nota como número decimal.
nota = float(input("Informe sua nota: "))

# 3. PROCESSAMENTO CONDICIONAL:
# Compara a nota com os intervalos definidos para cada conceito.
if nota <= 3.0:
    conceito = "Conceito F"
elif nota >= 3.0 and nota <= 4.5:
    conceito = "Conceito D"
elif nota >= 5.0 and nota <= 6.5:
    conceito = "Conceito C"
elif nota >= 7.0 and nota <= 8.5:
    conceito = "Conceito B"
else:
    conceito = "Conceito A"

# 4. SAÍDA DE DADOS:
# Exibe o conceito selecionado.
print(conceito)