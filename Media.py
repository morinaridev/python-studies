nome_aluno = (input('qual seu nome?'))
nota1 = int(input('qual sua primeira nota? '))
nota2 = int(input('qual sua segunda nota? '))

media = nota1 + nota2 / 2 

if media >= 7:
    print('Aprovado!')

elif media >= 5 <7:
    print('Recuperaçao')

else: 
    print('Reprovado')
 