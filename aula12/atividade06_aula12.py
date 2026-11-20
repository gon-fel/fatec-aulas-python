# ==========================================
# Atividade 06 - Aula 12: Seno e Coseno usando a biblioteca math.
# Descrição: Crie um programa que solicite ao operador o comprimento da escada em metros e o ângulo de inclinação em relação ao chão (em graus). Converta o ângulo para radianos com math.radians() e, utilizando a função math.cos(), calcule a distância horizontal do pé da escada até a parede.
# ==========================================
import math

# 1. Entrada dos Dados:
comprimento_escada = float(input("Informe o comprimento da escada em metros: "))
angulo_grau = float(input("Informe o angulo de inclinação da escada em relaçao ao chão em graus: "))

# 2. Processamento: 
angulo_rad = math.radians(angulo_grau)
distancia = comprimento_escada * math.cos(angulo_rad)

# 3. Saída: 
print('-' * 30)
print(f"A distância horizontal do pé da escada até a parede é de: {distancia:.2f} metros.\n") # esse \n é apenas para visualização ficar melhor no terminal.
