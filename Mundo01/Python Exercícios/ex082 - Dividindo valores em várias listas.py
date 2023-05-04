lista = []
par = []
impar = []
cont = 1
while True:
    n = int(input(f'Digite um valor {cont}: '))
    cont+=1
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    opção = ' '
    while opção not in 'SN':
        opção = str(input('Deseja inserir outro número? [S/N] ')).upper().strip()[0]
    if opção in 'N':
        break
print(f'Lista de todos os números digitados: {sorted(lista)}')
print(f'Lista números pares: {sorted(par)}')
print(f'Lista de números ímpares: {sorted(impar)}')


'''Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, 
respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''