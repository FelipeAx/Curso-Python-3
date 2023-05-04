s = 0
cont = 0
for c in range(1,7):
    n = int(input('Digite o {}º valor: '.format(c)))
    if n % 2 == 0:
        cont += 1
        s += n   # s=s+c
print('\033[1;33m Você digitou {} números PARES e soma é {:2} \033[m'.format(cont,s))


'''Desenvolva um programa que leia seis números inteiros e mostre a 
soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.'''
