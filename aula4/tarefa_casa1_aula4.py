# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 4 - Tarefa de Casa 1: Organização da Festa de Aniversário
# ==============================================================================

'''
Tarefa Para Casa 01 - Para Aula 04

Organização da Festa de Aniversário
Vamos criar um programa simples para ajudar a planejar a quantidade de docinhos de uma festa, usando apenas textos e números inteiros!

O que o seu programa deve fazer:
1. Pedir 5 informações ao usuário (Entrada de Dados):
Nome do aniversariante
Nome do responsável pela festa
Tipo do doce (ex: Brigadeiro, Beijinho, Coxinha)
Total de doces encomendados (número inteiro)
Total de doces que já foram comidos (número inteiro)

2. Fazer uma conta simples (Processamento):
Descobrir quantos doces ainda restam:
doces_restantes =  doces_encomendados - doces_comidos

3. Mostrar o resultado na tela (Saída de Dados):
Exibir todas as informações cadastradas e a quantidade final que sobrou.
'''
# Entrada de dados

nome_aniversariante = input("Informe o nome do aniversáriante: ")
responsavel_festa = input("Informe o nome do responsável pela festa: ")
tipo_doce = input("Informe o tipo de doce encomendado: ")
total_doce_encomenda = int(input("Informe a quantidade de doces encomendados: "))
total_doce_comidos = int(input("Informe a quantidade de doces comidos: "))

# Processamento dos dados

doces_restantes = total_doce_encomenda - total_doce_comidos

# Saída dos dados

print(f"\n FESTA ANIVERSÁRIO DO (A) {nome_aniversariante}", "\n", "-" *30)
print(f"Foram encomendados {total_doce_encomenda} {tipo_doce} pelo(a) {responsavel_festa}, para a festa de aninversário do {nome_aniversariante}.\nDurante a festa foi comido {total_doce_comidos} unidades de {tipo_doce}, sobrando {doces_restantes} unidades do doce.")