pp = ('Camisa', 50, 'Calça', 100, 'Shorts', 80)
print('-='*20)
print(f'{"LISTAGEM DE PREÇO":^40}')
print('-='*20)
for pos in range(0, len(pp)):
    if pos % 2 == 0:
        print(f'{pp[pos]:.<30}', end = '')
    else:
        print(f'R$ {pp[pos]:>4.2f}')
print('-='*20)
'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''