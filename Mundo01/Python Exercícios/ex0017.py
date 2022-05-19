import math
#from math import sqrt
CO = float(input('\nDigite o valor do Cateto Oposto: '))
CA = float(input('Digite o valor do Cateto Adjacente: '))
#Hip = sqrt((CO**2)+(CA**2))
Hip = math.hypot(CO, CA)
print('O valor da Hipotenusa é: {:.2f}\n'.format(Hip))
