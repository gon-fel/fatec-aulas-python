# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 9 - Atividade 7: Contagem de Parafusos
# ==============================================================================

# 1. ENTRADA DE DADOS:
parafusos = int(input('Digite o total de parafusos: '))
print(' ')

# 2. CONTAGEM E SAÍDA:
for i in range(1, parafusos + 1):
    print(f"Sensor registrou: parafuso {i}")

print(' ')

print("Lote concluído!")
print(f"Total processado: {parafusos} parafusos.")