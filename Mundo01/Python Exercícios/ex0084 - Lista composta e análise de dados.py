pessoas = list()
peso = list()
cont = 0
opção = ''
MaisPesada = MaisLeve = 0
while opção in 'S':
    peso.append(str(input('Nome: ')))
    cont += 1
    peso.append(float(input('Peso: ')))
    pessoas.append(peso[:])
    peso.clear()
    opção = str(input('Deseja Adicionar mais alguém? [S/N] ')).upper().strip()[0]
print('-='*20)
for c in pessoas:
    print(f'{c[0]} tem {c[1]}kg')
    if c[1] == min(c[1]):
        print(f'''Abaixo do peso! 
        {c[0]}''')
    elif c[1] == max(c[1]):
        print(f'''Acima do peso! 
        {c[0]}''')
        MaisPesada += 1
    else:
        print('Peso Normal!')
        MaisLeve += 1
    print('-='*20)
print(f'Pessoas Cadastradas: {cont}')
print(f'Pessoas Acima do Peso: {MaisPesada}')
print(f'Pessoas Abaixo do Peso: {MaisLeve}')
print('-='*20)






'''Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
 A) Quantas pessoas foram cadastradas.
 B) Uma listagem com as pessoas mais pesadas.
 C) Uma listagem com as pessoas mais leves.'''