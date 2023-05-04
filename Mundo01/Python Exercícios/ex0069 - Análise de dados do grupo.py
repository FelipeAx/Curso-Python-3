idadeCont = somaM = somaF = 0
c = 1
while True:
    idade = int ( input ('Idade: '))
    if idade >= 18:
        idadeCont += 1
    sexo = ' '
    opção = ' '
    while sexo not in 'MF':
        sexo = str ( input ('Gênero: [M/F] ')).upper().strip() [0]
    if sexo == 'M':
        somaM += 1
    else:
        if idade < 20:
            somaF += 1
    while opção not in 'SN':
        opção = str ( input ('Deseja continuar? [S/N] ')).upper().strip() [0]
    if opção == 'S':
        c += 1
    else:
        break
print('-='*20)
print(f'Pessoas com mais de 18 anos: {idadeCont}')
print(f'Homens cadastrados: {somaM}')
print(f'Mulheres com menos de 20 anos: {somaF}')
print(f'Quantas pessoas foi cadastrado: {c}')
print('-='*20)
        





'''Crie um programa que leia a idade e o sexo de várias pessoas. 
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.'''