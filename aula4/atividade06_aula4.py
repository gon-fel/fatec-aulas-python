# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 4 - Atividade 6: Cálculo da Base Média do Trapézio
# ==============================================================================

'''Cálculo da Média das Diagonais de um Trapézio
Criar um programa de geometria plana com duas etapas: primeiro calculamos a soma das duas bases de um trapézio e, em seguida, calculamos o tamanho da sua base média.

Contexto do Problema
A base média de um trapézio é o segmento que liga os pontos médios dos lados não paralelos. Para encontrá-la:
Cálculo Preliminar (X - Soma das Bases): Somar a base maior com a base menor.
Cálculo Final (Y - Base Média): Dividir essa soma (X) por 2.

O que o seu programa deve fazer:
1. Entrada de Dados:
Comprimento da Base Maior em cm (int)
Comprimento da Base Menor em cm (int)

2. Processamento (2 Etapas de Cálculo):
Cálculo Preliminar (X): Soma das duas bases: X = base_maior + base_menor
Cálculo Final (Y): Tamanho da base média (divisão real): Y = X / 2

3. Saída de Dados:
Exibir a soma das bases (X) e o valor final da base média (Y).
'''

# 1. Entrada de Dados
print("--- CÁLCULO DA MÉDIA DAS DIAGONAIS DE UM TRAPÉZIO ---\n")

comprimento_base_maior = int(input("Informe o comprimento da base maior em cm: "))
comprimento_base_menor = int(input("Informe o comprimento da base menor em cm: "))

# 2. Processamento
soma_bases = comprimento_base_maior + comprimento_base_menor
tamanho_base_media = soma_bases / 2

# 3. Saída dos Dados
print("=" * 30)
print("CÁLCULO DA MÉDIA DAS DIAGONAIS DE UM TRAPÉZIO")
print("=" * 30)
print(f"O comprimento da base maior é de: {comprimento_base_maior}cm.")
print(f"O comprimento da base menor é de: {comprimento_base_menor}.cm")
print(f"A soma das bases são de: {soma_bases}cm. E o comprimento médio é de {int(tamanho_base_media)}cm")