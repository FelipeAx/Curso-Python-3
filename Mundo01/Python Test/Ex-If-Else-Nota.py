n1 = float (input ('Digite sua primeira nota: '))
n2 = float (input ('Digite sua segunda nota: '))
n3 = float (input ('Digite sua terceira nota: '))
n4 = float (input ('Digite sua quarta nota: '))
média = (n1+n2+n3+n4)/4
print('\nSua média foi {:.1f}'.format(média))
if média < 6:
    print('Infelizmente você ficou de recuperação.')
else:
    print('Parabéns! Você foi aprovado.')
print('\nVocê precisava de no mínimo 6 na média para passar.\n')
