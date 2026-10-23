# 1. Entrada de dados do formulário

print("\n--- CADASTRO DE USUÁRIO ---\n")
nome = input("Digite o seu nome completo: ")
idade = int(input("Digite a sua idade: "))
email = input("Digite o seu e-mail: ")
cidade = input("Digite a sua cidade: ")
profissao = input("Digite a sua profissão: ")

# 2. Exibição dos dados coletados.

print("\n" + "=" * 30)
print("   DADOS CADASTRADOS")
print("=" * 30)
print(f"Nome {nome}")
print(f"Idade: {idade} anos")
print(f"e-mail: {email}")
print(f"Cidade: {cidade}")
print(f"Profissão: {profissao}")
print("\n" + "=" * 30)
