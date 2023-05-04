num = int(input('\nDigite um número: '))
"""n = str(num)
print('\nAnalisando o número {}...'.format(n))
print('\nMilhar: {}'.format(n[:1]))
print('Centena: {}'.format(n[1:2]))
print('Dezena: {}'.format(n[2:3]))
print('Unidade: {}\n'.format(n[3:4]))

print('\nMilhar: {}'.format(n[0]))
print('Centena: {}'.format(n[1]))
print('Dezena: {}'.format(n[2]))
print('Unidade: {}\n'.format(n[3]))"""

m = num // 1000 % 10
c = num // 100 % 10
d = num // 10 % 10
u = num // 1 % 10

print('\nMilhar: {}'.format(m))
print('Centena: {}'.format(c))
print('Dezena: {}'.format(d))
print('Unidade: {}\n'.format(u))


'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.'''