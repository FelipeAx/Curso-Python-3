n = int (input ('Digite qual tabuada deseja saber: '))
print('-='*10)
for c in range(1,11):
    print('\033[1;33m {} x {:2} = {:2} \033[m'.format(n,c, n*c))
print('-='*10)

'''Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, 
só que agora utilizando um laço for.'''