# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 12 - Atividade 4: Média Aritmética de Três Notas
# ==============================================================================

# 1. ENTRADA DE DADOS:
# Lê as três notas como números decimais.
nota1 = float(input("Informe a nota 1: "))
nota2 = float(input("Informe a nota 2: "))
nota3 = float(input("Informe a nota 3: "))

# 2. PROCESSAMENTO ARITMÉTICO:
# Calcula a média simples e arredonda o resultado para uma casa decimal.
media = (nota1 + nota2 + nota3) / 3
media_arredondada = round(media, 1)

# 3. SAÍDA DE DADOS:
# Exibe a média arredondada.
print(f"A média final é: {media_arredondada}")
