total = cont = contTotal = 0
lista = []
print('-='*30)
while True:
    produto = str ( input ('Nome do produto: '))
    preço = float ( input ('Digite o valor do produto: R$ '))
    total += preço
    contTotal += 1
    opção = ' '
    lista = [produto]
    if preço > 1000:
        cont += 1
    while opção not in 'SN':
        opção = str ( input ('Deseja continuar? [S/N]: ')).strip().upper() [0]
    if opção == 'N':
        break
    print('-='*30)
print(f'Você comprou {contTotal} produtos e gastou um total de R$ {total}')
print(f'{cont} produto(s) custa mais de R$ 1000')
print(f'Produto mais barato: {min(lista)}')
print('-='*30)
    

'''Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''