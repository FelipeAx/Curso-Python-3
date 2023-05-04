print('-=-'*20)
print('Analisador de Triângulos')
print('-=-'*20)
a = float ( input ('Valor de A: '))
b = float ( input ('Valor de B: '))
c = float ( input ('Valor de C: '))
print('-=-'*20)
if a < b + c and b < a + c and c < a + b:
    print('Os valores formam um triângulo')
else:
    print ('Os valores não formam um triângulo')
print('-=-'*20)

'''Desenvolva um programa que leia o comprimento de três retas e
diga ao usuário se elas podem ou não formar um triângulo.'''