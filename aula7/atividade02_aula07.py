# ==========================================
# Atividade 02 - Aula 07: Tabela Completa de Idades
# Descrição: Define a faixa etária detalhada com base na idade.
# ==========================================

# 1. Entrada de Dados
idade = int(input("Digite sua idade: "))

# 2. Estrutura Condicional em cascata
if idade < 3:
    classificacao = "Classificacao: Bebê"

elif idade < 12:
    classificacao = "Classificacao: Criança"

elif idade < 18:
    classificacao = "Classificacao: Adolescente"

elif idade < 59:
    classificacao = "Classificacao: Adulto"

elif idade >= 60:
    classificacao = "Classificacao: Idoso"

# 3. Saída de Dados
print(classificacao)