primeiro = int ( input ('PRIMEIRO TERMO: '))
razão = int ( input ('RAZÃO: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{}'.format(termo), end = '')
    print(' → ' if cont <= 9 else ' \n', end='')
    termo += razão
    cont += 1
print('ACABOU!')



'''Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, 
mostrando os 10 primeiros termos da progressão usando a estrutura while.'''