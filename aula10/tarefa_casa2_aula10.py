# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 10 - Tarefa de Casa 2: Abastecimento de Reservatório
# ==============================================================================

''' Tarefa Para Casa 02 - Para Aula 10

Um operador precisa completar o nível de um reservatório de água. 

O programa deve receber a quantidade de litros que o reservatório já contém antes de iniciar o abastecimento e o número de baldes de água (com capacidade fixa de 10 litros cada) que serão despejados. 

No meio do programa, utilize a estrutura for para registrar o despejo de cada balde, contando um a um. Ao término, após o laço, o programa calcula o volume total adicionado e exibe o nível final do reservatório.'''

# 1. ENTRADA DE DADOS:
volume_inicial = int(input("Digite o volume inicial do reservatório (litros): "))
qtd_baldes = int(input("Digite a quantidade de baldes a despejar: "))
print(f"Nível inicial: {volume_inicial} litros.\n")

# 2. REGISTRO DOS BALDES:
for i in range(1, qtd_baldes + 1):
    print(f"Despejando balde {i}... Concluído!")

print(f"\nBaldes adicionados: {qtd_baldes}")

# 3. CÁLCULO E SAÍDA DO VOLUME:
volume_adicionado = qtd_baldes * 10
print(f"Volume de água adicionada: {volume_adicionado} litros.")

volume_final = volume_inicial + volume_adicionado
print(f"Volume final no reservatório: {volume_final} litros.")