from math import factorial
n = int ( input ('Digite um valor: '))
f = factorial(n)
print('O fatorial de {} é: {}'.format(n, f)) 


# Outra maneira mais prática de fazer
n = int ( input ('Digite um valor: '))
fat = 1
print('Calculando {}! = '.format(n), end = '')
while n > 0:
    print('{}'.format(n), end = '')
    print(' x ' if n > 1 else ' = ', end = '')
    fat = fat * n
    n = n - 1
print('{}'.format(fat))

 

'''Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120'''