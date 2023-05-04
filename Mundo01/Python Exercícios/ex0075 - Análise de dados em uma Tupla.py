n1 = int (input('Digite primeiro valor: '))
n2 = int (input('Digite segundo valor: '))
n3 = int (input('Digite terceiro valor: '))
n4 = int (input('Digite quarto valor: '))
numeros = (n1, n2, n3, n4)
print(f'Os números digitados foram: {numeros}')
print(f'O número 9 aparece {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O primeiro número 3 aparece na posição {numeros.index(3)}.')
cont = 0
print('Os números pares são: ', end = ' ')
for n in numeros:
    if n % 2 == 0:
        cont += 1
        print(n, end = ' ')
print(f'\nForam {cont} par digitados.')

    
   

'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. 
No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''