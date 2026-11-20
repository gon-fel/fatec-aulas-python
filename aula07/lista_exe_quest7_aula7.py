# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 7 - Lista de Exercícios, Questão 7: Temperatura do Núcleo
# ==============================================================================

# 1. Entrada de dados
temperatura = int(input("Informe a temperatura medida no núcleo em ºC: "))
print("Entrada (ºC):",temperatura)

# 2. Condicional e saída de dados
if temperatura < 45:
    print("Saída: 0%")
elif temperatura <= 65:
    print("Saída: 50%")
elif temperatura <= 80:
    print("Saída: 80%")
else:
    print("Saída: 100%")