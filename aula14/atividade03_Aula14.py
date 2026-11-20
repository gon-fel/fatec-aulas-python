# ==========================================
# Atividade 03 - Aula 14: Criando funções
# Descrição: Você deve desenvolver um sistema de câmbio em Python utilizando duas funções personalizadas independentes.
# 1. Crie uma função chamada 'converter_para_dolar' que receba dois    parâmetros: o valor em reais ('valor_reais') e a cotação do dólar ('cotacao_dolar'). A função deve calcular a conversão, armazenar o resultado em uma variável local e retorná-lo em um único 'return'.

# 2. Crie uma segunda função chamada 'converter_para_euro' que receba dois parâmetros: o valor em reais ('valor_reais') e a cotação do euro ('cotacao_euro'). A função deve calcular a conversão, armazenar o resultado em uma variável local e retorná-lo em um único 'return'.

# No programa principal, solicite a você (ou ao usuário) o montante em reais que deseja converter, a cotação atual do dólar e a cotação atual do euro. Em seguida, chame as duas funções que você criou passando os argumentos correspondentes e exiba ambos os valores convertidos na tela com duas casas decimais.
# ==========================================

def converter_para_dolar (valor_real, cotacao_dolar):
    
    valor_dolares = valor_real / cotacao_dolar
    return valor_dolares

def converter_euro (valor_real, cotacao_euro):
    
    valor_euro = valor_real / cotacao_euro
    return valor_euro

reais = float(input("Digite o valor em reais: R$"))
cot_dolar = float(input("Digite a cotação atual do dolar (R$): "))
cot_euro = float(input("Digite a cotação atual do euro (R$): "))

dolares = converter_para_dolar(reais, cot_dolar)
euros = converter_euro(reais, cot_euro)

print("\n--- RESULTADO DA CONVERSÃO ---")
print(f"Valor em Dolares: US$ {dolares:.2f}")
print(f"Valo em Euros € {euros:.2f}")