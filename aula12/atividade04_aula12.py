# ==========================================
# Atividade 04 - Aula 12: Média aritmética
# Descrição: Crie um programa que solicite as três notas de um estudante, calcule a média aritmética simples e utilize a função pronta round() para arredondar a nota final para 1 casa decimal, exibindo o resultado.
# ==========================================

# 1. Entrada de Dados:
nota1 = float(input("Informe a nota 1: "))
nota2 = float(input("Informe a nota 2: "))
nota3 = float(input("Informe a nota 3: "))

# 2. Processamento: 
media = (nota1 + nota2 + nota3) / 3

media_arredondada = round(media, 1)

# 3. Saída: 
print(f"A média final é: {media_arredondada}")

    
