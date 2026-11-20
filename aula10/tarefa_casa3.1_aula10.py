# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 10 - Tarefa de Casa 3.1: Multas por Velocidade
# ==============================================================================

# 1. ENTRADA DE DADOS:
total_veiculos = int(input("Digite o total de veículos: "))
print(' ')

# 2. VERIFICAÇÃO DAS VELOCIDADES:
multa = 0
for i in range(1, total_veiculos + 1):
    velocidade = int(input(f"Velocidade do veículo {i} (km/h): "))

    if velocidade > 60:
        multa = multa + 1
        
# 3. SAÍDA DE DADOS:
print(f"\nTotal de multas aplicadas: {multa}")