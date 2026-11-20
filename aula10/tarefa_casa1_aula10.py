# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 10 - Tarefa de Casa 1: Recarga de Cartão
# ==============================================================================

# 1. ENTRADA DE DADOS:
saldo_cartão = int(input("Digite o saldo atual do cartão: "))
credito = int(input("Digite a quantidade de créditos a recarregar: "))

print(f"Saldo inicial: R${saldo_cartão}")
print(" ")

# 2. REGISTRO DOS CRÉDITOS:
total = 0
for i in range(1, credito + 1):
    print(f"Validando crédito {i}... ok!")
    total = total + 1

print(f"\nCreditos adicionados: {credito}")

# 3. CÁLCULO E SAÍDA DA RECARGA:
valor_recarga = credito * 5
print(f"Valor total da recarga: R${valor_recarga}")

saldo_final = saldo_cartão + valor_recarga
print(f"Saldo final atualizado: R${saldo_final}")

print (total)
