p = float (input ('Digite seu Peso (kg): '))
a = float (input ('Digite sua Altura (m): '))
imc = p / (a * a) # Ou p / (a ** 2)
print('-=-'*12)
print('\033[1mIMC:\033[m \033[1;33m{:.2f}\033[m'.format(imc))
if imc < 18.5:
    print('\033[1;41m Abaixo do Peso \033[m')
elif imc < 25:
    print('\033[1;42m Peso Ideal \033[m')
elif imc < 30:
    print('\033[1;34;43m Sobrepeso \033[m')
elif imc < 40:
    print('\033[1;41m Obesidade \033[m')
else:
    print('\033[1;41m Obesidade Mórbida \033[m')
print('-=-'*12)


'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida'''