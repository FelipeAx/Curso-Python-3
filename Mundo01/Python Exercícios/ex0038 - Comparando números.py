print('-=-'*10)
n1 = int ( input ('Digite um Número: '))
n2 = int ( input ('Digite Outro Número: '))
print('-=-'*10)
if n1 > n2:
    print('\033[33mO Primeiro Número é Maior\033[m')
elif n1 < n2:
    print('\033[33mO Segundo Número é Maior\033[m')
else:
    print('\033[33mOs Dois Valores São Iguais\033[m')
print('-=-'*10)


'''Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais'''