usuario = ''
senha = ''
tentativas = 0

while (usuario != 'joao' and senha != 'senha123') and tentativas < 3:
    usuario = input('digite seu usuario')
    senha = input('digite sua senha')
    tentatativa += 1 

if usuario != 'joao' and senha != 'senha123':
    print('aguarda 30 mins antes de tentar novamente')
else: 
    print('login feito com sucesso')

