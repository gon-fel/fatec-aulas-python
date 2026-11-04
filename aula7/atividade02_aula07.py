# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 7 - Atividade 2: Classificação Detalhada por Faixa Etária
# ==============================================================================

# 1. ENTRADA DE DADOS:
# Lê a idade informada como um número inteiro.
idade = int(input("Digite sua idade: "))

# 2. PROCESSAMENTO CONDICIONAL:
# A cadeia de condições verifica as faixas etárias em ordem crescente.
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

# 3. SAÍDA DE DADOS:
# Exibe a classificação correspondente à idade.
print(classificacao)