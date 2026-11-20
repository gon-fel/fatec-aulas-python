'''Escreva um programa em Python para simular a autenticação de um sistema bancário:
Defina uma senha numérica padrão (por exemplo: 1234).
O seu programa deve solicitar a senha e continuar dentro do laço while enquanto você (ou o usuário) digitar um valor incorreto, emitindo uma mensagem de alerta a cada erro.
Assim que a senha correta for digitada, encerre o laço e exiba a mensagem: "Acesso liberado!".
'''

senha_padrao = '1234'
senha = ''

while senha != senha_padrao:
    senha = input('Digite a senha: ')
    if senha != senha_padrao:
        print('Senha incorreta. Tente novamente.')

print('Senha correta. Acesso Liberado.')    
    