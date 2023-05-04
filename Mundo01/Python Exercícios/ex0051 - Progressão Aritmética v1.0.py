primeiro = int ( input ('PRIMEIRO TERMO: '))
razão = int ( input ('RAZÃO: '))
décimo = primeiro + 10 * razão #Mostrar os 10 primeiros termos de uma PA
for c in range(primeiro,décimo,razão):
    print(c, end = ' → ')
print('ACABOU!')

'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, 
mostre os 10 primeiros termos dessa progressão.'''