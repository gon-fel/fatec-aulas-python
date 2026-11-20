# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 9 - Atividade 2: Contador de Chamada
# ==============================================================================

print("-" * 30)
print("CONTADOR DE CHAMADA")
print("-" * 30)

# 1. ENTRADA DE DADOS:
senha_inicio = int(input("Digite senha inicial: "))
senha_final = int(input("Digite a senha final: "))

# 2. CONTAGEM E SAÍDA:
for i in range(senha_inicio, senha_final + 1):
    print(f"Chamando senha {i}")