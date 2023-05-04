n = int( input('Digite um valor: '))
lista = [n]
cont = 0
total = n
m = 0
while n != 0:
    n = int ( input ('Digite um valor: '))
    cont += 1
    total += n
    if n != 0:
        lista += [n]
m = total / cont        
print('-='*20)
print('Você digitou {} valores e a média dos valores é {}'.format(cont, m))
print('O menor valor é {}'.format(min(lista)))
print('O maior valor é {}'.format(max(lista)))
print('-='*20)

#Outra forma de se fazer
resp = 'S'
soma = quant = média = menor = maior = 0
while resp in 'Ss':
    n = int (input ('Digite um número: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str ( input ('Quer continuar? [S/N]: ')).upper().strip() [0]
média = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, média))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))




'''Crie um programa que leia vários números inteiros pelo teclado. 
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''