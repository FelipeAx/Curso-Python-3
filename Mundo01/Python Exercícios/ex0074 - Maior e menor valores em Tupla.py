from random import randint, randrange
a = (randint(0, 10), randint(0, 10), randint(0, 10),
    randint(0, 10), randint(0, 10))
print('-='*20)
print(f'Valores Sorteados: {a}')
print(f'O menor valor sorteado foi: {min(a)}')
print(f'O menor valor sorteado foi: {max(a)}')
print('-='*20)
'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
'''