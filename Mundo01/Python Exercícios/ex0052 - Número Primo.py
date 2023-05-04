tot = 0
n = int ( input ('DIGITE UM NÚMERO: '))
print('-='*30)
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[1;33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} → \033[m'.format(c), end='')
print('\033[1mO número\033[m \033[1;33m{}\033[m \033[1mfoi divisível \033[1;33m{}\033[m \033[mvezes\033[m'.format(n,tot))
if tot <= 2:
    print('\033[1;37;44m Número Primo \033[m')
print('-='*30)
'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''