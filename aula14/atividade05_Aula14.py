# ==========================================
# Atividade 05 - Aula 14: Criando funções
''' Você deve desenvolver o módulo de folha de pagamento responsável por calcular o Imposto de Renda Retido na Fonte (IRRF) mensal de um 
trabalhador no Brasil. Para isso, crie uma função chamada 'calcular_ir' 
que receba como parâmetro o salário base tributável ('salario').

Dentro da função, utilize uma estrutura condicional encadeada 
(if-elif-else) para aplicar a tabela progressiva oficial da Receita 
Federal (base de cálculo mensal), multiplicando o salário pela alíquota 
da respectiva faixa e subtraindo a parcela a deduzir correspondente:

- Faixa 1: Salário até R$ 2.259,20
  -> Isento (Imposto = R$ 0,00)
- Faixa 2: De R$ 2.259,21 até R$ 2.826,65
  -> Alíquota de 7,5% e parcela a deduzir de R$ 169,44
- Faixa 3: De R$ 2.826,66 até R$ 3.751,05
  -> Alíquota de 15,0% e parcela a deduzir de R$ 381,44
- Faixa 4: De R$ 3.751,06 até R$ 4.664,68
  -> Alíquota de 22,5% e parcela a deduzir de R$ 662,77
- Faixa 5: Acima de R$ 4.664,68
  -> Alíquota de 27,5% e parcela a deduzir de R$ 896,00

Fórmula do cálculo em cada faixa:
imposto = (salario * aliquota) - deducao

Armazene o valor calculado em uma variável local ('valor_imposto') 
dentro da estrutura condicional e devolva esse resultado em um único 
ponto de saída no final da função utilizando o comando 'return'.

No programa principal, solicite a você (ou ao usuário) o valor do 
salário tributável, chame a função 'calcular_ir' passando esse dado 
como argumento e exiba o valor do imposto devido e o salário líquido 
após o desconto, ambos formatados com duas casas decimais.'''
# ==========================================

def calcular_ir (salario):
    if salario <= 2259.20:
        aliquota = 0

    elif salario <= 2826.65:
        aliquota = (salario * 0.075) - 169.44

    elif salario <= 3751.05:
        aliquota = (salario * 0.15) - 381.44

    elif salario <= 4664.68:
        aliquota = (salario * 0.225) - 662.77
    
    else:
        aliquota = (salario * 0.275) - 896

    valor_imposto = aliquota

    return valor_imposto

salario_tributavel = float(input("\nInforme o seu salário: R$"))

valor_ir = calcular_ir(salario_tributavel)

salario_liquido = salario_tributavel - valor_ir

print("\n--- Cálculo IRRF ---")
print(f"O seu salário é de: R${salario_tributavel:.2f}")
print(f"Seu desconto de IRRF é de: {valor_ir:.2f}")
print(f"Você irá receber: R${salario_liquido:.2f}")

