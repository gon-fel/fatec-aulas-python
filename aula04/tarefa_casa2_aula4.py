# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 4 - Tarefa de Casa 2: Painel de Pontuação de Videogame
# ==============================================================================

'''
Tarefa Para Casa 02 - Para Aula 04

Exercício: Painel de Pontuação de Videogame
Vamos criar um programa simples para calcular a pontuação de uma partida em um jogo eletrônico, usando apenas textos e números inteiros!

O que o seu programa deve fazer:
1. Pedir 5 informações ao usuário (Entrada de Dados):
Nome do jogador
Nome do jogo
Nome do personagem escolhido
Pontos ganhos na fase (número inteiro)
Pontos perdidos por penalidades (número inteiro)

2. Fazer uma conta simples (Processamento):
Descobrir a pontuação final da partida:
pontos_finais = pontos_ganhos - pontos_perdidos

3. Mostrar o resultado na tela (Saída de Dados):
Exibir todas as informações cadastradas e a pontuação final calculada.
'''
# Entrada de Dados
print("PAINEL DE PONTUAÇÃO DE VÍDEOGAME \n", "=" * 30, "\n")

nome_jogador = input("Informe o nome do Jogador: ")
nome_jogo = input("Informe o nome do jogo: ")
personagem_escolhido = input("Informe o nome do personagem: ")
pontos_ganhos = int(input("Quantos ponto ganhou na partida? "))
pontos_perdidos = int(input("Quantos pontos perdeu na partida? "))

# Processamento dos Dados
pontos_finais = pontos_ganhos - pontos_perdidos

#Saída de Dados
print("\n","=" * 30,"\nPAINEL DE PONTUAÇÃO DE VÍDEOGAME\n","=" * 30,"\n")
print(f"O jogador {nome_jogador} jogou o jogo {nome_jogo} com o personagem {personagem_escolhido}. Ganhou {pontos_ganhos} pontos e perdeu {pontos_perdidos} pontos durante a partida. Finalizando com {pontos_finais} pontos.")

