# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 7 - Atividade 1: Classificação Etária (Estruturas Condicionais)
# ==============================================================================

# 1. ENTRADA DE DADOS:
# A idade é convertida para inteiro para permitir a comparação com as faixas etárias.
idade = int(input("Digite a sua idade: "))

# 2. PROCESSAMENTO CONDICIONAL:
# A estrutura if/elif/else seleciona uma classificação conforme a idade informada.
if idade > 18:
    classificacao = "Classificaço: Adulto"  # Mantido conforme original do usuário

elif idade < 18 and idade > 12:
    classificacao = "Classificação: Adolescente"

else:
    classificacao = "Classificação: Criança"

# 3. SAÍDA DE DADOS:
# Exibe a classificação selecionada.
print(classificacao)