from random import randint
#import random
from time import sleep
print('-=-'*20)
print('Vou pensar em um número de 0 a 5, tente adivinhar...')
print('-=-'*20)
u = int(input('Qual o seu palpite: ')) #Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(4) #Faz com que crie um suspense de 4 segundos antes de aparecer o que o PC pensou.
#n = random.randint(0,5)
n = randint(0,5)   #Faz o computador pensar em um número
print('-=-'*20)
print('O computador pensou no número {}'.format(n))
print('-=-'*20)
if u == n: 
    print('Você Venceu!')
else:
    print('Você Perdeu!')
print('-=-'*20)


'''Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e 
peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
O programa deverá escrever na tela se o usuário venceu ou perdeu.'''