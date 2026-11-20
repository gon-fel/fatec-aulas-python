'''
Você deve criar um sistema de avaliação física para uma clínica de 
nutrição. Desenvolva uma função chamada 'avaliar_imc' que receba dois 
parâmetros: o peso em quilogramas ('peso') e a altura em metros ('altura').

Dentro da função, calcule o Índice de Massa Corporal utilizando a 
função math.pow():
imc = peso / math.pow(altura, 2)

Em seguida, utilize uma estrutura condicional (if-elif-else) para 
classificar o resultado armazenando o texto correspondente em uma 
variável local ('classificacao'):
- imc < 18.5: "Abaixo do peso"
- 18.5 <= imc < 25.0: "Peso normal"
- 25.0 <= imc < 30.0: "Sobrepeso"
- imc >= 30.0: "Obesidade"

Ao final da função, devolva a classificação em um único ponto de saída 
utilizando o comando 'return'. No programa principal, solicite o peso 
e a altura, chame a função que você criou e exiba a classificação 
retornada na tela.
'''
import math

def avaliar_imc (peso, altura):
    imc = peso / math.pow(altura, 2)

    if imc < 18.5:
        classificacao = "Abaixo do peso"

    elif imc < 25.0:
        classificacao = "Peso Normal"

    elif imc < 30.0: 
        classificacao = "Sobrepeso"

    else:
        classificacao = "Obesidade"

    return classificacao

peso_coporal = float(input("Informe o seu peso: "))
altura_corporal = float(input("Informe sua altura: "))

resultado = avaliar_imc(peso_coporal, altura_corporal)

print(resultado)


