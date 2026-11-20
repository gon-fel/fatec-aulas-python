# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 10 - Tarefa de Casa 01: Inspeção de Temperatura
# ==============================================================================

print('-' * 30)
print("INSPEÇÃO DE TEMPERATURA")
print('-' * 30)


# 1. ENTRADA DE DADOS:
qtd_motores = int(input("Digite a quantidade de motores: "))
temperaturas = []


for motor in range (1, qtd_motores + 1):
    temperatura = int(input("Digite a temperadura: "))
    temperaturas.append(temperatura)

# 2. INSPEÇÃO E SAÍDA:
for motor in range (1, qtd_motores +1):
    temperatura = temperaturas[motor - 1]

    if temperatura > 80:
        print(f"Temperatura do Motor {motor}: {temperatura}ºC")
        print(f"Motor {motor} -> ALERTA: Superaquecimento.")
         
    else: 
        print(f"Temperatura do Motor {motor}: {temperatura}ºC")
        print(f"Motor: {motor} -> Status: Temperatura Normal.")