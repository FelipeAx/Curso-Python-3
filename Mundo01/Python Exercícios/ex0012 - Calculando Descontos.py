n=float(input('Qual é o preço do produto? R$ '))
d=float(input('Quantos por cento de desconto? '))
p=n-(n*(d/100))
print('\nO preço do produto é R$ {} e com o desconto de {}% vai ficar por R$ {:.2f}\n'.format(n,d,p))


'''Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.'''