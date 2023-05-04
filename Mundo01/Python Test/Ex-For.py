'''i = int ( input ('Digite início: '))
f = int ( input ('Digite Fim: '))
p = int ( input ('Digite Passo: '))
for c in range (i, f+1, p):
    print(c)
print('FIM')'''

s = 0
for c in range (0, 3):
    n = int ( input ('Digite um valor: '))
    s = s + n         # Ou s += n
print('A soma de todos os número é: {}'.format(s))