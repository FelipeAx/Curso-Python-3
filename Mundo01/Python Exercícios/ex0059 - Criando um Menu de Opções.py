from time import sleep
print('-='*20)
n1 = int ( input ('Digite valor 1: '))
n2 = int ( input ('Digite valor 2: '))
print('-='*20)
lista = [n1,n2]
opção = 0
while opção != 5:
    print('''Digite a opção desejada conforme o que deseja fazer com seus valores:
            [ 1 ] Somar
            [ 2 ] Multiplicar
            [ 3 ] Achar o Maior
            [ 4 ] Add Novos Números
            [ 5 ] Sair do Programa''')
    print('-='*20)
    opção = int ( input ('Digite aqui sua opção: '))
    print('-='*20)
    if opção == 1:
        print('A soma dos {} e {} valores é {}'.format(n1, n2, (n1+n2)))
        print('-='*20)
        sleep(2)
    elif opção == 2:
        print('Os valores {} e {} multiplicados é {}'.format(n1, n2, (n1*n2)))
        print('-='*20)
        sleep(2)
    elif opção == 3:
        print('O maior valor entre {} e {} é {}'.format(n1, n2, max(lista)))
        print('-='*20)
        sleep(2)
    #Outra maneira de fazer pra achar o maior
       #if n1 > n2:
            #maior = n1
        #else:
            #maior = n2'''
    elif opção == 4:
        print('Digite os valores novamente!')
        sleep(1)
        n1 = int ( input ('Valor 1: '))
        n2 = int ( input ('Valor 2: '))
    elif opção == 5:
        print('Finalizando.',end='')
        sleep(0.75)
        print('.',end='')
        sleep(0.75)
        print('.')
        sleep(0.75)
        print('Programa Finalizado!')
        sleep(0.5)
        print('Volte sempre.')
    else:
        print('Opção inválida, tente novamente...')
        sleep(1)
        n1 = int ( input ('Digite o valor 1 novamente: '))
        n2 = int ( input ('Digite o valor 2 novamente: '))
print('-='*20)





'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''