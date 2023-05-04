from random import randint
from time import sleep
print('-='*20)
itens = ('Pedra','Papel','Tesoura')
computador = randint(0,2)
print('''\033[1;44mFaça sua escolha:\033[m
        \033[1;33m[0] Pedra\033[m
        \033[1;33m[1] Papel\033[m
        \033[1;33m[2] Tesoura\033[m''')
jogador = int(input('\033[1;32mDigite aqui o seu Palpite: \033[m')) #Jogador tenta adivinhar
print('{:^40}'.format('\033[1;31mJo\033[m'))
sleep(0.75)
print('{:^40}'.format('\033[1;33m ken\033[m'))
sleep(0.75)
print('{:^40}'.format('\033[1;34m pô!\033[m'))
sleep(0.5) #Faz com que crie um suspense de x segundos antes de aparecer o que o PC pensou.
print('-='*20)
if jogador != 0 and jogador != 1 and jogador != 2:
    print('\033[1;41m Jogada inválida, tente novamente! \033[m')
else:
    print('\033[1mO computador jogou\033[m \033[1;34;43m {} \033[m'.format(itens[computador]))
    print('\033[1mVocê jogou\033[m \033[1;34;43m {} \033[m'.format(itens[jogador]))
    print('-='*20)
    if computador == 0:
        if jogador == 0:
            print('\033[1;34;47m EMPATE! \033[m')
        elif jogador == 1:
            print('\033[1;34;42m VOCÊ GANHOU! \033[m')
        elif jogador == 2:
            print('\033[1;34;41m VOCÊ PERDEU! \033[m')
    elif computador == 1:
        if jogador == 0:
            print('\033[1;34;41m VOCÊ PERDEU! \033[m')
        elif jogador == 1:
            print('\033[1;34;47m EMPATE! \033[m')
        elif jogador == 2:
            print('\033[1;34;42m VOCÊ GANHOU! \033[m')
    elif computador == 2:
        if jogador == 0:
            print('\033[1;34;42m VOCÊ GANHOU! \033[m')
        elif jogador == 1:
            print('\033[1;34;41m VOCÊ PERDEU! \033[m')
        elif jogador == 2:
            print('\033[1;34;47m EMPATE! \033[m')
print('-='*20)

'''Crie um programa que faça o computador jogar Jokenpô com você.'''