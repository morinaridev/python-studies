#while

#criar um programa que permite 3 tentativas antes de fechar

tentativas = 0 
while tentativas < 3:
    print('tente novamente')
    tentativas = tentativas + 1

    #quando queremos que uma açao continue acontecendo ate que um criterio seja satisfeito
    #so pode logar dse digitar a senha correta

    senha = ''
    while senha != '123456':
        senha = input('digite a senha correta: ')

    print('bem vindo ao sistema')
    #garantir que algo esteja preenchido 
    # so deve continuar qunado o usuario informar seu nome 

    nome = ''
    while nome == '':
        nome = input('digite seu nome')
        print(f'bem vindo {nome}')

# contadores

# ser avisado as 17h do por do sol 
# contar de hora em hora ate chegar as 17hrs
# ao chegar 17h, exibir 'hora de ver o por do sol'

horario = 0 
while horario >= 17:
    print(horario)
    horario = horario + 1

    print('hora de ver o por do sol')