from time import sleep
print('-='*20)
valor = int ( input('Digite um valor inteiro a ser sacado: R$ '))
cédula = 100
totalCédula = 0
print('Processando.', end = '')
sleep(1)
print('.', end = '')
sleep(1)
print('.', end = '')
sleep(1)
print(' ')
print('-='*20)
while True:
    if valor >= cédula:
        valor -= cédula
        totalCédula += 1
    else:
        sleep(0.75)
        if totalCédula > 0:
            print(f'Total de {totalCédula} cédulas de R$ {cédula}')
        if cédula == 100:
            cédula = 50
        elif cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 5
        elif cédula == 5:
            cédula = 2
        elif cédula == 2:
            cédula = 1
        totalCédula = 0
        if valor == 0:
            break
print('-='*20)
print('Volte Sempre!')
print('-='*20)




   


'''Crie um programa que simule o funcionamento de um caixa eletrônico. 
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) 
e o programa vai informar quantas cédulas de cada valor serão entregues. 

OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''