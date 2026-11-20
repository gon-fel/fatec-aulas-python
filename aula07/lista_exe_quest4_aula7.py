# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 7 - Lista de Exercícios, Questão 4: Código de Segurança
# ==============================================================================

# 1. Entrada de Dados

print("=" * 30, "\nCÓDIGO NÚMERICO DE SEGURANÇA\n", "=" * 30)

codigo_digitado = int(input("Informe o seu código: "))

print(f"Entrada: {codigo_digitado}")

if codigo_digitado == 4829:
    print("Saìda: 1 - Trava destrancada")
else:
    print("Saída: 0 - Acesso negado")