# ==========================================
# Atividade 04 - Aula 07: Conceito de Nota Escolar
# Descrição: Atribui um conceito conceitual com base em intervalos de notas.
# ==========================================

print("=" * 30)
print("Conceito de Nota Escolar")
print("=" * 30)

# 1. Entrada de dado
nota = float(input("Informe sua nota: "))

# 2. Estrutura Condicional com operadores lógicos (and)
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

# 3. Saída dos Dados
print(conceito)