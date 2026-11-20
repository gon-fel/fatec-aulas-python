# ==========================================
# Atividade 03 - Aula 13: Controle do While
# Descrição: Simulação de um sistema bancário com menu de opções
# ==========================================

opcao = ''

while opcao != 'S':
    print('\n--- MENU PRINCIPAL ---')
    print("[A] Consultar Saldo")
    print('[B] Fazer Depósito')
    print('[S] Sair do Sistema')

    opcao = input('\nEscolha uma opção: ').upper()

    if opcao == 'A':
        print('\n>> Seu saldo atual é de: R$ 1.500,00.')
    elif opcao == 'B':
        print('\n>> Opção de depósito selecionada. Insira o envelope.')
    elif opcao == 'S':
        print('\n Saindo do sistema...')
    else:
        print('\n>> Opção inválida. Escolha A, B ou S.')


print('\n>> Sistema finalizado. Até logo!')