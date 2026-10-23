# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 1: Entrada e Saída Padrão (I/O) e Variáveis Primitivas
# ==============================================================================

# 1. SAÍDA DE DADOS (Output):
# A função print() projeta texto (string) no terminal (na saída padrão).
print("Olá, mundo!")

# 2. ENTRADA DE DADOS (Input) E VARIÁVEIS:
# A função input() interrompe a execução, aguarda a entrada do usuário e
# armazena o dado na memória SEMPRE como string (tipo str).
cidade = input("Qual a sua cidade: ")

# Exibição concatenando texto literal e o valor da variável por argumento:
print("Você digitou", cidade)

# Repetição do fluxo de I/O com novo identificador de memória:
signo = input("Qual o seu signo: ")
print("Você digitou", signo)
