# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 9 - Atividade 5: Andares do Elevador
# ==============================================================================

print('-' * 20)
print('ANDARES DO ELEVADOR')
print('-' * 20)

# 1. ENTRADA DE DADOS:
numero_andar = int(input("Digite o andar de destino: "))

# 2. CONTAGEM E SAÍDA:
for andar in range (1, numero_andar + 1):
    print(f"Subindo... Andar {andar}")