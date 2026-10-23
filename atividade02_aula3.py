# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 3 - Atividade 2: Formulário de Cadastro, Escape (\n) e Replicação de String
# ==============================================================================

# 1. ENTRADA DE DADOS (Coleta sequencial):
print("\n--- CADASTRO DE USUÁRIO ---\n")

nome = input("Digite o seu nome completo: ")
idade = int(input("Digite a sua idade: "))  # Casting str -> int
email = input("Digite o seu e-mail: ")
cidade = input("Digite a sua cidade: ")
profissao = input("Digite a sua profissão: ")

# 2. SAÍDA FORMATADA (Relatório estruturado):
# O operador '*' com string replica o caractere N vezes para criar separadores visuais:
print("\n" + "=" * 30)
print("   DADOS CADASTRADOS")
print("=" * 30)

# Interpolação de valores formatados via f-string:
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"E-mail: {email}")
print(f"Cidade: {cidade}")
print(f"Profissão: {profissao}")

print("=" * 30 + "\n")
