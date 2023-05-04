cont = total = n = 0
while n != 999:
    n = int ( input ('Digite um valor: '))
    if n != 999:
        cont += 1
        total = total + n
print('Você digitou {} vezes e a soma dos valores foi {}'.format(cont, total))





'''Crie um programa que leia vários números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''