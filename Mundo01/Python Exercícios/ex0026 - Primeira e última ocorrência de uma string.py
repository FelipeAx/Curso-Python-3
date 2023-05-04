frase = str (input('\nDigite uma Frase: ')).upper().strip()
print('\n{}'.format(frase))
print('Quantas vezes aparece a letra "A" na frase: {}'.format(frase.count('A')))
print('Em qual posição a letra "A" aparece pela primeira vez? {}'.format(frase.find('A')+1))
print('Em qual possição a letra "A" aparece pela última vez? {}\n'.format(frase.rfind('A')+1))



#Ou pode usar .upper() dentro do format como abaixo
#print('\nQuantas vezes aparece a letra "A" na frase: {}'.format(frase.upper().count('A')))
#print('Em qual posição a letra "A" aparece pela primeira vez? {}'.format(frase.find('A')))
#print('Em qual possição a letra "A" aparece pela última vez? {}\n'.format(frase.upper().rfind('A')))

#rfind = encontrar a direita"""

'''Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que 
posição ela aparece a primeira vez e em que posição ela aparece a última vez.'''