senha = 1234
senha_digitada = 0
contador = 1

while contador <= 3 or senha_digitada != senha:
    senha_digitada = int(input("Digite sua senha: "))
    
    if senha_digitada == senha:
        print("Acesso liberado!")      
        break  

    elif senha_digitada != senha:
        print("Senha inválida. Tente novamente.")
        
        print(f'Tentativa {contador} de 3')
        
        contador += 1

else:
    print(f"Após 3 tentativas o sistema foi bloqueado. Tente novamente mais tarde.")
