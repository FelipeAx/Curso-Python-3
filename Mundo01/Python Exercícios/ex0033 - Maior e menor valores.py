n1 = int ( input ('Digite o Primeiro Número: '))
n2 = int ( input ('Digite o Segundo Número: '))
n3 = int (input ('Digite o Terceiro Número: '))
menor = n1 #
if n2 < n1 and n2 < n3:
    menor = n2
maior = n1
if n3 > n1 and n3 > n2:
    maior = n3
print('-=-'*10)
print('O menor valor é: {}'.format(menor))
print('O maior valor é: {}'.format(maior))

print('-=-'*10)

# Outro exemplo mais prático
print('O menor valor é: {}'.format(min(n1,n2,n3)))
print('O maior valor é: {}'.format(max(n1,n2,n3)))

print('-=-'*10)


''' Faça um programa que leia três números e mostre qual é o maior e qual é o menor. '''