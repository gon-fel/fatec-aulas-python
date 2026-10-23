# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 4 - Atividade 2: Perímetro de Terreno Retangular (Precedência de Operadores)
# ==============================================================================
# Enunciado:
# 1. Peça a medida da largura do terreno (inteiro).
# 2. Peça a medida do comprimento do terreno (inteiro).
# 3. Calcule o perímetro aplicando a fórmula do retângulo.
# 4. Exiba o resultado com saída formatada.
# ==============================================================================

# 1. ENTRADA DE DADOS:
print("\n--- CÁLCULO DO PERÍMETRO DE UM TERRENO RETANGULAR ---")

largura = int(input("Informe a largura do terreno: "))
comprimento = int(input("Informe o comprimento do terreno: "))

# 2. PROCESSAMENTO ARITMÉTICO:
# Mecânica de precedência:
# Opção A: 2 * largura + 2 * comprimento (2 multiplicações precedem 1 soma)
# Opção B: 2 * (largura + comprimento)   (parênteses forçam a soma antes de 1 multiplicação)
perimetro = 2 * (largura + comprimento)

# 3. SAÍDA FORMATADA:
print("\n" + "=" * 30)
print(f"O perímetro do terreno retangular é: {perimetro}")
print("=" * 30 + "\n")
