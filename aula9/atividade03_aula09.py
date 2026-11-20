# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 9 - Atividade 3: Contador de Páginas
# ==============================================================================

# 1. Entrada de Dados
print("-" * 30)
print("CONTADOR DE PÁGINAS")
print("-" * 30)


pagina_inicial = int(input("Digite a página inicial: "))
pagina_final = int(input("Digite a página final: "))

# 2. CONTAGEM E SAÍDA:
for i in range(pagina_inicial, pagina_final + 1):
    print(f"pagina {i}")
print("-" * 30)