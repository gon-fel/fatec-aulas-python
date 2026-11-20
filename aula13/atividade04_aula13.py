# ==========================================
# Atividade 04 - Aula 13: Controle do While
# Descrição: Criar um programa que utilize a estrutura de repetição while para calcular a média de notas de uma turma. O sistema deve exibir um menu textual interativo com duas opções: [1] para "Digitar nota" e [2] para "Finalizar". Se ao menos uma nota tiver sido digitada, o programa calcula e exibe a média aritmética final com duas casas decimais. Caso seja encerrado sem digitar nenhuma nota, exiba uma mensagem indicando que nenhuma nota foi registrada.
# ==========================================

opcao = 0
soma_notas = 0
quantidade_notas = 0
escolha = ''

while opcao != 3:
    try:
        print('--- MENU DE NOTAS ---')
        print("[1] Digitar nota")
        print('[2] Média aritmética final')
        print('[3] Finalizar')
    
        opcao = int(input('\nEscolha uma opção: '))
        
        if opcao == 1:
            nota = float(input('Digite a nota (0 a 10): '))
            
            if 0 <= nota <=10:
                soma_notas += nota
                quantidade_notas += 1

            else:
                print('Nota Inválida.')

            escolha = input('Deseja digitar outra nota? (S/N): ').upper()
            
            if escolha == 'S':
                 while escolha == 'S':
                    nota = float(input('Digite a nota (0 a 10): '))
                    
                    if 0 <= nota <=10:
                        soma_notas += nota
                        quantidade_notas += 1
                        
                        escolha = input('Deseja digitar outra nota? (S/N): ').upper()
        elif opcao == 2:
                if quantidade_notas > 0:
                    media = soma_notas / quantidade_notas
                    print(f'A média aritmética final é: {media:.2f}')
                else:
                    print('Nenhuma nota foi registrada')
                
        elif opcao == 3:
            if quantidade_notas <=0:
                print('Nenhuma nota foi digitada.')        
                

    except ValueError:
        print('Opção inválida. Por favor, escolha uma opção válida.')

        continue

print('Programa encerrado.')