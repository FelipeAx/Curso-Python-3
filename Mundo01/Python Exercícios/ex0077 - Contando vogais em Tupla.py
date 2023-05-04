palavras = ('Cachorro', 'Celular', 'Gato')
print('-='*20)
for p in palavras:
    print(f'\nNa palava {p.upper()} temos as seguintes vogais: ', end = '')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end = ' ')
print('')
print('-='*20)

'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''