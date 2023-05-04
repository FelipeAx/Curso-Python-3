s = 0
cont = 0
for c in range(1,501,2):
    if c % 3 == 0:
        s += c       #s = s + c
        cont += 1    #cont = cont + 1 
        print('\033[1;44m O número {} é ímpar \033[m'.format(c))
print('\033[1;34;43m A soma de todos os {} valores solicitados é: {} \033[m'.format(cont,s))



'''Faça um programa que calcule a soma entre todos os números que 
são múltiplos de três e que se encontram no intervalo de 1 até 500.'''