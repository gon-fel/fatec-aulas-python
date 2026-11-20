# ==========================================
# Tarefa Casa 01 - Aula 14: Controle do While + Estrutura condicional
# Descrição: Crie um sistema de fechamento de caixa que solicite a você o valor de vendas consecutivas até que o número 0 (sentinela de parada) seja digitado para encerrar o laço while. Durante a execução, utilize if para ignorar valores negativos; ao término, calcule e exiba o total acumulado, a quantidade de vendas válidas e a média das vendas arredondada para 2 casas decimais com a função round().
# ==========================================


soma_vendas = 0
quantidade_vendas = 0

vendas = float(input('Informe o valor da venda: R$'))    

while vendas != 0:
    if vendas > 0:
        soma_vendas += vendas
        quantidade_vendas += 1

        print(f"\nVenda de R${vendas:.2f} registrada.")   
    
    elif vendas < 0: 
        print("Valor negativo ignorado.")

    vendas = float(input('Informe o valor da venda (ou 0 para fechar): R$'))
    
if quantidade_vendas > 0:
    media_vendas = round(soma_vendas / quantidade_vendas, 2)
    print(f"\nTotal acumuado: R$ {soma_vendas:.2f}")
    print(f"Quantidade de vendas válidas {quantidade_vendas}")
    print(f'Média das vendas: {media_vendas:.2f}')
else:
    print("Nenhuma venda foi computada.")