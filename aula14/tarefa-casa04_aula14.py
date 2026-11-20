numero = int(input("Digite um número: "))
   
while numero >= 0:
    print("\n--- TABUADA ---")
    for i in range (1, 11):   
          
        resultado = numero * i
        
        print(f"{numero}x{i}: {resultado}")
    
    numero = int(input("\nDigite um número: "))
    
print("Programa finalizado. Até a próxima.")

    