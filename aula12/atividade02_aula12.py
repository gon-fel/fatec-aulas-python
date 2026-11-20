# ==============================================================================================
# Atividade 02 - Aula 12: Teorema de Pitágoras usando a biblioteca math.
# Descrição: Crie um programa que leia os valore de a e b e calcule os quadrados de cada um deles.
# ===============================================================================================
import math

numeroA = float(input("Digite o valor do primeiro angulo: "))
numeroB = float(input("Digite o valor do segundo angulo: "))

soma_dos_quadrados = (numeroA * numeroA) + (numeroB * numeroB)

hipotenusa = math.sqrt(soma_dos_quadrados)

print(f"O valor da hipotenusa é: {hipotenusa:.2f}")