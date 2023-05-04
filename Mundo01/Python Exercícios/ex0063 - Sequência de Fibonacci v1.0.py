N = int ( input ('Digite quantos termos: '))
t1 = 0
t2 = 1
print('{} → {}'.format(t1, t2), end = '')
cont = 3
while cont <= N:
    t3 = t1 + t2
    print(' → {}'.format(t3), end = '')
    cont = cont + 1
    t1 = t2 #1 #1 #2 #3 #5 ...
    t2 = t3 #1 #2 #3 #5 #8 ...
print(' → FIM')

#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N 
# primeiros elementos de uma Sequência de Fibonacci. Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8