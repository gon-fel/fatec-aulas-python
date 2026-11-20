# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 4 - Tarefa de Casa 3: Controle de Viagem de Carro
# ==============================================================================

# Criar um programa que descubra quantos kms ainda faltam para chegar em determinado lugar.

# Entrada de Dados

print("-" * 30,"\nCONTROLE DE VIAGEM DE CARRO\n","-" *30)

nome_motorista = input("Informe o nome do motorista: ")
cidade_origem = input("Informe a cidade de origem: ")
destino_final = input("Informe a cidade de destino: ")
km_total = int(input("Informe a quilometragem total da viagem: "))
km_percorrido = int(input("Informe quantos Km já foi percorrido: "))

# Processamento dos dados

km_restante = km_total - km_percorrido

# Saída dos Dados
print(f"O motorista {nome_motorista}, saiu de {cidade_origem} com destino a {destino_final}. Essa viagem possuí {km_total} de Km totais. Ele(a) já percorreu {km_percorrido} Km faltando {km_restante} Km até chegar ao destino final.")