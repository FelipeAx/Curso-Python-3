from random import shuffle
N1 = input('\nPrimeiro aluno: ')
N2 = input('Segundo aluno: ')
N3 = input('Terceiro aluno: ')
N4 = input('Quarto aluno: ')
lista = [N1,N2,N3,N4]
shuffle(lista)
print('\nA ordem de apresentação é: {}\n'.format(lista))
