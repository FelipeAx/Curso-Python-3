frase = str ( input ('DIGITE UMA FRASE: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
# COMENTADO OUTRA FORMA DE RESOLVER 
'''inverso = ''
for c in range(len(junto) -1, -1, -1):
    inverso = inverso + junto[c]'''
    
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('É um Palíndromo')
else:
    print('Não é um palíndromo')


'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, 
desconsiderando os espaços. Exemplos de palíndromos:

APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.'''