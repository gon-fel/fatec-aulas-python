# ==========================================
# Atividade 01 - Aula 07: Classificação Etária
# Descrição: Classifica a idade informada pelo usuário.
# ==========================================

# 1. Entrada de dados
idade = int(input("Digite a sua idade: "))

# 2. Estrutura Condicional para verificação de faixa etária
if idade > 18:
    classificacao = "Classificaço: Adulto"  

elif idade < 18 and idade > 12:
    classificacao = "Classificação: Adolescente"

else:
    classificacao = "Classificação: Criança"

# 3. Saída de Dados
print(classificacao)