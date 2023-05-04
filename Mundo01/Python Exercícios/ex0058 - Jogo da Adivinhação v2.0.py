from random import randint
#import random
from time import sleep
print('-=-'*20)
q = 1
print('\033[1;41m Vou pensar em um número de 0 a 10, tente adivinhar... \033[m')
print('-=-'*20)
u = int(input('\033[1;33mQual o seu palpite:\033[m ')) #Jogador tenta adivinhar
n = randint(0,10)
print('\033[1;34mO computador pensou no número:\033[m {}'.format(n))
if n == u:
    print('\033[1;42m Você Venceu! \033[m \033[4mFoi necessário {} jogadas para isso.\033[m'.format(q))
print('-=-'*20)
while u != n:
    u = int ( input ('\033[1;41m Não foi dessa vez, tente outro número:\033[m '))
    n = randint(0,10)   #Faz o computador pensar em um número
    print('\033[1;44m O computador pensou no número:\033[m {}'.format(n))
    print('-=-'*20)
    q += 1
    if n == u:
        print('\033[1;42m Você Venceu! \033[m \033[4mFoi necessário {} jogadas para isso.\033[m'.format(q))
print('-=-'*20)



'''Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites 
foram necessários para vencer.'''