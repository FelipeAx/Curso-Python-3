ano = int ( input ('Digite o ano que deseja saber se é Bissexto: '))
#print(ano%4)
if ano % 4 == 0:
    print('O ano {} é Bissexto'.format(ano))
else:
    print('O ano {} não é Bissexto'.format(ano))


'''Faça um programa que leia um ano qualquer e mostre se ele é bissexto.'''