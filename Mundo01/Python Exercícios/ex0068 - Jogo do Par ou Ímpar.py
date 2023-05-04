from random import randint
from time import sleep
print('-=-'*20)
v = 0
while True:
    n = int ( input ('Diga um valor: '))
    c = randint(0, 11)
    total = n + c
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('\033[1;33mPar ou Ímpar? [P/I]: \033[m')).upper().strip() [0]
    print(f'\033[1;44m Você jogou {n} e o computador jogou {c} \033[m.')
    print(f'\033[1;43m Total: {total} \033[m')
    if tipo == 'P':
        if total % 2 == 0:
            print('\033[1;42m O resultado foi PAR. Você venceu! \033[m')
            v += 1
        else:
            print('\033[1;41m O resultado foi IMPAR. Você perdeu! \033[m')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('\033[1;42m O resultado foi IMPAR. Você venceu! \033[m')
            v +=1
        else:
            print('\033[1;41m O resultado foi PAR .Você perdeu! \033[m')
            break
    print('\033[1;33mVamos jogar novamente...\033[m')
print('\033[1;31m GAME OVER! \033[m')
print(f'\033[1;42m Você venceu {v} vezes \033[m')




'''Faça um programa que jogue par ou ímpar com o computador. 
O jogo só será interrompido quando o jogador perder, 
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''