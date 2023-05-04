from math import cos, sin, tan, radians
ângulo = float(input('\nDigite um ângulo: '))
cosseno = cos(radians(ângulo))
seno = sin(radians(ângulo))
tangente = tan(radians(ângulo))
print('\nO cosseno do ângulo {} é: {}\nO Seno do ângulo {} é: {}\nA tangente do ângulo {} é: {}\n'.format(ângulo, cosseno, ângulo, seno, ângulo, tangente ))

'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.'''