# ==========================================
# Tarefa Casa 05 - Aula 14: Controle do While + Estrutura condicional
# Descrição: Elabore um programa para triagem de múltiplos lotes de carga que opere em um menu com while contendo as opções "[1] Processar Lote" e "[2] Finalizar". Ao selecionar a opção 1, solicite a quantidade de caixas daquele lote e use um laço for para ler o peso de cada caixa, classificando e contando individualmente com if-elif-else quantas caixas são leves (peso < 15 kg), médias (15 a 40 kg) ou pesadas (> 40 kg), exibindo o relatório do lote antes de retornar ao menu principal.
# ==========================================
menu = 0
total_caixas = 0

while menu != 2:
    print("\n--- MENU ---")
    print("[1] Processar Lote")
    print("[2] Finalizar")

    menu = int(input("Escolha uma opção do menu: ")) 

    if menu == 1:
        leves = 0
        medias = 0
        pesadas = 0
        qtd_caixa = int(input("Informe a quantidade de caixas a ser processada nesse lote: "))   
    
        if qtd_caixa > 0:
            for i in range(1, qtd_caixa + 1):
                peso_caixa = float(input(f"Informe o peso da caixa {i}: "))

                if peso_caixa < 15:
                    leves += 1
                elif peso_caixa <= 40:
                    medias += 1
                else:
                    pesadas += 1
                
                total_caixas += qtd_caixa
                
    elif menu == 2:
            
            print("\n--- Fechamento ---")
            print(f"Caixas leves: {leves}")
            print(f"Caixas média: {medias}")
            print(f"Caixas pesadas: {pesadas}")
    
    else:
        print("Ação negada por falta de processamento. Escolha um opção do menu.")

print("\nSistema encerrado.")

    

    

