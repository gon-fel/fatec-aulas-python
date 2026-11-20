# ==========================================
# Atividade 04 - Aula 14: Criando funções
''' Descrição: Você foi contratado para desenvolver o módulo de cálculo de frete de uma transportadora regional. Para organizar o sistema, você deve criar uma função chamada 'calcular_frete' que receba dois parâmetros: o peso da encomenda em quilogramas ('peso_kg') e a distância do transporte em quilômetros ('distancia_km').

Dentro da função, calcule o valor do frete seguindo as regras tarifárias da empresa:

1. Toda entrega possui uma taxa fixa de despacho de R$ 15,00.
2. Soma-se R$ 2,50 por cada quilograma do peso da encomenda.
3. Soma-se R$ 0,40 por cada quilômetro da distância percorrida.
4. Além disso, utilize uma estrutura condicional (if-else) dentro da função para aplicar uma taxa adicional de carga pesada: se o peso da encomenda for maior que 20 kg, adicione R$ 30,00 ao valor do frete; caso contrário, não adicione nada.

Armazene o valor final do frete em uma variável local e devolva esse
resultado em um único ponto de saída utilizando o comando 'return'.

No programa principal, solicite a você (ou ao usuário) o peso da carga
e a distância da entrega. Em seguida, chame a função 'calcular_frete'
passando esses valores como argumentos e exiba o custo total do frete
formatado com duas casas decimais.'''
# ==========================================

def calcular_frete(peso_kg, distancia_km):
    custo_peso = peso_kg * 2.50
    custo_distancia = distancia_km * 0.40
    valor_frete = custo_peso + custo_distancia + 15

    if peso_kg > 20:
        valor_frete += 30
    else:
        valor_frete += 0

    return valor_frete


peso = float(input("Informe o peso da carga: "))
distancia = float(input("Informe a distancia em Km: "))

total_frete = calcular_frete(peso, distancia)

print("\n--- CÁLCULO DO FRENTE ---")
print(f"O peso total da carga é de: {peso:.2f}kg")
print(f"A distância a ser percorrida é de: {distancia:.0f}km")
print(f"O custo total do frente é de {total_frete:.2f}")