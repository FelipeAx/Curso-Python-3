from random import choice
n1 = input('\nPrimeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
List = [n1, n2, n3, n4]
a = choice(List)
print('\nO aluno escolhido foi: {}\n'.format(a))




