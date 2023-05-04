numeros = list()
cont = 1
while True: 
    num = int(input(f'Digite valor {cont}: '))
    if num not in numeros:
        numeros.append(num)
        print('Valor Adicionado...')
        cont = cont + 1
    else:
        print('Valor duplicado!, não vou adicionar...')
    opção = ' '
    while opção not in 'SN':
        opção = str(input('Deseja continuar?[S/N] ')).upper().strip()[0]
    if opção == 'N':
        break
numeros.sort()
print(f'Você digitou os valores: {numeros}')


'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
Caso o número já exista lá dentro, ele não será adicionado. No final, 
serão exibidos todos os valores únicos digitados, em ordem crescente.'''