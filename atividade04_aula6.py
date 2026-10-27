# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 6 - Atividade 4: Verificação de Maioridade (Estrutura Condicional Simples)
# ==============================================================================

# 1. ENTRADA DE DADOS:
# Casting obrigatório (str -> int) para processamento da idade em anos:
idade = int(input("Informe a sua idade em anos: "))

# 2. CONTROLO DE FLUXO E SAÍDA FORMATADA:
# Avaliação booleana da condição relacional (idade >= 18)
print("\n" + "=" * 40)
print("       VERIFICAÇÃO DE MAIORIDADE        ")
print("=" * 40)
print(f"Idade informada: {idade} anos")
print("-" * 40)

if idade >= 18:
    print("Classificação: Você é MAIOR de idade.")
else:
    print("Classificação: Você é MENOR de idade.")

print("=" * 40 + "\n")