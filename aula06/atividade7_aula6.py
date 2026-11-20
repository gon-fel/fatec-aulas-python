# ==============================================================================
# FATEC Taquaritinga - ADS | Lógica de Programação
# Aula 6 - Atividade 7: Validação de Senha de Acesso
# ==============================================================================

'''Exercício: Validação de Senha de Acesso
Crie um programa que leia uma senha numérica de 4 dígitos e informe se o acesso foi liberado ou negado. Considere que a senha correta cadastrada no sistema é 1234.

Requisitos
1. Entrada (o que ler):
senha_digitada: Senha numérica informada pelo usuário (int)

2. Condição (Decisão):
Se senha_digitada == 1234: liberar o acesso.

Senão (else): bloquear o acesso.

3. Saída:
Exibir a mensagem: "Acesso Permitido" ou "Acesso Negado: Senha Incorreta".
Exemplo de Entrada e Saída

Cenário 1:
Digite a senha de 4 dígitos: 1234
Acesso Permitido

Cenário 2:
Digite a senha de 4 dígitos: 9999
Acesso Negado: Senha Incorreta
'''

# 1. ENTRADA DE DADOS:
senha_digitada = int(input("Informe sua senha: "))

# 2. CONDIÇÃO E SAÍDA:
if senha_digitada == 1234:
    print("Acesso permitido.")

else:
    print('Acesso Negado: Senha Incorreta.')