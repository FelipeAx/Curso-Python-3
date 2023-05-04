lista = []
for cont in range (1,6):
    lista.append(int (input (f'Digite valor {cont}: ')))
print('-='*20)
print(f'O maior valor é {max(lista)} que está na posição', end = ' ')
for i, v in enumerate(lista):
    if v == max(lista):
        print(f'{i+1}... ', end = '')
print()
print(f'O menor valor é {min(lista)} que está na posição', end = ' ')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'{i+1}... ', end = '')
print()
print('-='*20)

'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, 
mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''