print('-='*30)
for c in range(1,11):
    print(c)
print('FIM')
print('-='*30)
c = 1
while c < 11:
    print(c)
    c = c + 1
print('FIM')
print('-='*30)
# Ex condição de parada, só vai parar o loop se o valor que digitar for zero (0).
n = 1
while n != 0:
    n = int ( input ('Digite um número: '))
print('FIM')
print('-='*30)
# Enquanto a resposta for == a Sim o programa vai continuar
r = 'S'
while r == 'S':
    n = int ( input ('Digite um valor: '))
    r = str ( input ('Quer continuar [S/N]: ')).upper()
print('FIM')
print('-='*30)

# While até digitar zero e dizer quantos números Par e ímpar foi digitado
n = 1
par = impar = 0
while n != 0:
    n = int ( input ('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Foi digitado {} números Pares e {} números impares'.format(par, impar))