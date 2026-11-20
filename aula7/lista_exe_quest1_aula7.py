# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 7 - Lista de Exercícios, Questão 1: Controle de Acesso por Altura
# ==============================================================================

# 1. Entrada de dados
print("=" * 30 , "\nCONTROLE DE ACESSO POR ALTURA\n","=" *30)
altura = int(input("Informe a sua Altura em centímetro (ex: 172): "))

# 2. Estrutura Condicional

if altura < 135:
    print(f"Entrada (cm): {altura}.\nSaída: 0 - Bloquear Acesso")
else:
    print(f"Entrada (cm): {altura}.\nSaída: 1 - Permitir Acesso")
