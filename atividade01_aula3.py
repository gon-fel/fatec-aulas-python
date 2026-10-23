# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 3 - Atividade 1: Conversão de Tipos (Casting) e Interpolação (f-strings)
# ==============================================================================

# 1. ENTRADA DE TEXTO (String):
nome = input("Digite o seu nome: ")

# 2. ENTRADA COM CASTING (str -> int):
# A função input() retorna 'str'. O invólucro int() converte o valor para inteiro,
# permitindo operações matemáticas na memória.
idade = int(input("Digite a sua idade: "))

# 3. PROCESSAMENTO:
# Subtração simples de inteiros para estimativa de ano:
ano_nascimento = 2026 - idade

# 4. SAÍDA FORMATADA (f-string):
# O prefixo f antes das aspas permite interpolação direta de variáveis com {}:
print(f"Nome: {nome}. Ano de nascimento aproximado: {ano_nascimento}")
