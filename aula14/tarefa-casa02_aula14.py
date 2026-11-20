# ==========================================
# Tarefa Casa 02 - Aula 14: Controle do While + Estrutura condicional
# Descrição: Implemente um menu interativo com as opções "[C] Calcular" e "[S] Sair" controlado por um laço while. Ao escolher "C", o programa deve solicitar a área de uma placa circular em metros quadrados e, utilizando a constante math.pi e a função math.sqrt(), calcular o raio correspondente da peça, classificando-o com if-elif-else em "Pequeno" (raio < 1 m), "Médio" (1 a 3 m) ou "Grande" (raio > 3 m); o programa só deve finalizar a execução quando a opção "S" for digitada.
# ==========================================

import math

print("\n--- MENU ---")
print("[C] Calcular")
print("[S] Sair")

menu = input("Escolha uma opção: ").upper()

while menu != 'S':   
    
    if menu == 'C':    
        area = float(input("Informe a área da placa em m²: "))

        raio_area = area / math.pi
        raio = math.sqrt(raio_area)

        print(f"Raio: {raio:.2f}")
        
        if raio < 1:
            print("Pequeno")
        elif raio <= 3:
            print('Médio')
        else:
            print("Grande")

    else:
        print("Escolha inválida.")

    print("\n--- MENU ---")
    print("[C] Calcular")
    print("[S] Sair")

    menu = input("Escolha uma opção: ").upper()

print("Programa encerrado.")