from random import shuffle
N1 = input('\nPrimeiro aluno: ')
N2 = input('Segundo aluno: ')
N3 = input('Terceiro aluno: ')
N4 = input('Quarto aluno: ')
lista = [N1,N2,N3,N4]
shuffle(lista)
print('\nA ordem de apresentação é: {}\n'.format(lista))

'''O mesmo professor do desafio 19 quer sortear a ordem 
de apresentação de trabalhos dos alunos. Faça um programa 
que leia o nome dos quatro alunos e mostre a ordem sorteada.'''