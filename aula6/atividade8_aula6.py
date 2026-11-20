# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 6 - Atividade 8: Verificação de Febre
# ==============================================================================

'''
Exercício: Verificação de Febre
Crie um programa para triagem médica que leia a temperatura corporal de um paciente e informe se ele está com febre (temperatura igual ou superior a 38°C).

Requisitos
1. Entrada (o que ler):
temperatura: Temperatura corporal do paciente em °C (int)

2. Condição (Decisão):
Se temperatura >= 38: paciente com estado febril.

Senão (else): temperatura dentro da normalidade.

3. Saída:
Exibir a mensagem: "ALERTA: Paciente com febre!" ou "Temperatura normal.".

Exemplo de Entrada e Saída

Cenário 1:
Digite a temperatura corporal (°C): 39
ALERTA: Paciente com febre!

Cenário 2:
Digite a temperatura corporal (°C): 36
Temperatura normal.
'''

# 1. ENTRADA DE DADOS:
temperatura = int(input("Informe a temperatura corporal: ºC"))

# 2. CONDIÇÃO E SAÍDA:
if temperatura >=38:
    print("ALERTA: Paciente com febre!")


else:
    print("Temperatura normal.")