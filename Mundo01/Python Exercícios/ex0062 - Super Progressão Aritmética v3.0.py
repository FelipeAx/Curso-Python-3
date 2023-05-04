from time import sleep
primeiro = int ( input ('PRIMEIRO TERMO: '))
razão = int ( input ('RAZÃO: '))
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}'.format(primeiro), end = '')
        print(' → ', end='')
        primeiro += razão
        cont += 1
    print('PAUSA!')
    sleep(0.75)
    print('-='*20)
    print('(DIGITE 0 PARA SAIR DO PROGRAMA)')
    mais = int ( input ('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
sleep(3)
print('Finalizando.',end='')
sleep(0.75)
print('.',end='')
sleep(0.75)
print('.')
sleep(0.75)
print('Programa Finalizado!')
sleep(0.5)
print('Volte sempre.')
exit()


'''Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
O programa encerrará quando ele disser que quer mostrar 0 termos.'''