# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 10 - Tarefa de Casa 4: Organização de Livros
# ==============================================================================

'''Tarefa Para Casa 04 - Para Aula 10

Um bibliotecário está organizando uma prateleira temática. 
O programa deve solicitar a quantidade de livros que já estão arrumados na prateleira e o número de novos livros devolvidos que serão guardados nela. 

No meio do programa, utilize a estrutura de repetição for para registrar a colocação de cada livro, contando um a um. Ao término, após o laço, o programa calcula a quantidade adicionada e exibe o total final de livros disponíveis na estante.

EXEMPLO DE ENTRADA E SAÍDA: 
Digite a quantidade de livros já na estante: 15 
Digite a quantidade de livros a guardar: 3 
Livros já organizados: 15 

Guardando livro 1 na estante... 
Guardando livro 2 na estante... 
Guardando livro 3 na estante... 
Livros adicionados: 3 

Total final na prateleira: 18 livros.'''

# 1. ENTRADA DE DADOS:
livros_estante = int(input("Digite a quantidade de livros já na estante: "))
livros_guardar = int(input("Digite a quantidade de livros a guardar: "))
print(f"Livros já organizados: {livros_estante}\n")

# 2. REGISTRO DOS LIVROS:
for i in range(1, livros_guardar + 1):
    print(f"Guardando livro {i} na estante...")

print(f"Livros adicionados: {livros_guardar}\n")

# 3. CÁLCULO E SAÍDA DO TOTAL:
total_livros = livros_estante + livros_guardar
print(f"Total final na prateleira: {total_livros} livros.")