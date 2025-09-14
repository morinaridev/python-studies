#laços de repetição

for item in range(3):
    print(item)
#for item in colecao
    #comandos

for item in range(2,12,2):
    print(item)
    #range nunca inclui o ultimo numero

# lista de nomes

nomes = ['joao', 'guilherme', 'arthur', 'isabela']
dados = [1, 'joao', False]
for nome in nomes:
    print(nome)

    for dado in dados: 
        print(dado)

        idades = [13, 15, 18, 30, 42]

        for idade in idades:
            if idade >= 18:
                print(f'{idade} é maior de idade')
            else:
                print(f'{idade} é menor de idade')

# exemplo pratico

#validador de senhas

#len

senhas = ['abc', 'segura123', '12345', 'python123', 'oi']
for senha in senhas: 
    if len(senha) >= 6:
        print(f'a {senha} é valida')
    else: 
        print(f'a senha deve possuir no minimo 6 caracteres')