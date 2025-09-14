#variaveis
#nome, celular, endereco

velocidade_internet = 400 
print(velocidade_internet)
# numeros inteiros int
idade = 17
# decimais float
nota = 7.5
#textos string
nome_completo = 'joao guilherme'
#booleanos bool
sou_lindo = True
#condicionais - if elif else 

salario_mensal = input('qual é o seu salario mensal: ')
horas_trabalhadas = input('quantas horas trabalha por mês: ')
valor_hora = float(salario_mensal) / int(horas_trabalhadas)
print(valor_hora)


atrasos = int(input('quantas faltas voce tem?'))
if atrasos >= 3:
    print('voce esta suspenso')
elif atrasos == 2:
    print('mais uma falta esta suspenso')
elif atrasos == 1: 
    print('mais duas voce esta suspenso')   

else: 
    print('entre!') 