# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 12 - Atividade 7: Classificação e Consolidação de Cargas de Caminhões
# ==============================================================================
'''Descrição: Uma cooperativa agrícola recebe caminhões de grãos e precisa triar o peso líquido das cargas. Crie um programa que solicite a quantidade total de caminhões que serão descarregados no turno.

No meio do programa, utilize a estrutura de repetição for para ler o peso bruto (em kg) e o peso do veículo vazio/tara (em kg) de cada caminhão. Para cada veículo, o programa realiza o cálculo da carga líquida: carga_liquida = peso_bruto - tara

Em seguida, utilizando a estrutura condicional if-elif-else, classifique e contabilize a carga em uma das três categorias operacionais:
- Leve: carga_liquida < 10000 kg
- Padrão: 10000 kg <= carga_liquida <= 25000 kg
- Pesada: carga_liquida > 25000 kg

Ao término do laço for, o programa calcula o peso líquido total recebido e a média de carga por caminhão (arredondada com round()), exibindo o consolidado das categorias e os valores totais.

1. Entradas:
- total_caminhões: quantidade de veículos avaliados no lote (int)
- peso_bruto: Peso total na balança em kg (lido a cada iteração) (float)
- tara: Peso do caminhão vazio em kg (lido a cada iteração)(float)

2. Saídas:
Cargas Leves: 1
Cargas Padrão: 1
Cargas Pesadas: 1
Peso líquido total descarregado: 58000.0 kg
Média de carga líquida por veículo: 19333.33 kg
'''

# 1. ENTRADA DE DADOS:
# Lê a quantidade de caminhões que será processada.
qtd_caminhoes = int(input("Informe quantos caminhões serão descarregados neste turno: "))

# 2. INICIALIZAÇÃO DOS ACUMULADORES:
# Prepara contadores por categoria e o acumulador do peso líquido total.
carga_leve = 0
carga_padrao = 0
carga_pesada = 0
peso_liquido_total = 0

# 3. PROCESSAMENTO DAS CARGAS:
# Para cada caminhão, calcula o peso líquido e atualiza sua categoria.
try:
    for i in range(1, qtd_caminhoes + 1):
        peso_bruto = float(input(f"Informe o peso total do caminhão {i}: ")) #----
        tara = float(input(f"Informe o peso do caminhão {i} vazio: "))
        print('')
        peso_liquido = peso_bruto - tara
        peso_liquido_total += peso_liquido

        if peso_liquido < 10000:
            carga_leve += 1
        elif 10000 <= peso_liquido <= 25000:
            carga_padrao += 1

        else:
            carga_pesada += 1

    # 4. CÁLCULO DA MÉDIA:
    # Divide o peso líquido total pela quantidade de caminhões e arredonda para duas casas.
    media_carga = round(peso_liquido_total / qtd_caminhoes, 2)

    # 5. SAÍDA CONSOLIDADA:
    # Apresenta os totais por categoria, o peso líquido e a média calculada.
    print('-' * 30)
    print(f"Cargas Leves: {carga_leve}")
    print(f"Cargas Padrão: {carga_padrao}")
    print(f"Cargas Pesadas: {carga_pesada}")
    print('-' * 30)
    print(f"Peso líquido total descarregado: {peso_liquido_total} kg.")
    print(f"Média de carga líquida por veículo: {media_carga} kg.")
except:
    print("Erro: Entrada inválida. Por favor, insira valores numéricos válidos para peso e tara.")
