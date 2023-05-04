from time import sleep
n = 0
while True:
    n = int (input ('Digite o valor referente a Tabuada que quer saber: '))
    if n < 0:
        break
    for c in range(1,11):
        print('\033[1;33m {} x {:2} = {:2} \033[m'.format(n,c, n*c))
print('Finalizando.',end='')
sleep(0.75)
print('.',end='')
sleep(0.75)
print('.')
sleep(0.75)
print('Programa Finalizado!')
sleep(0.5)
print('Volte sempre!')



'''Faça um programa que mostre a tabuada de vários números, um de cada vez, 
para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.'''