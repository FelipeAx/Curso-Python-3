print('\033[1;30;7mHello World!\033[m')

nome = 'Felipe'
print('Seja bem vindo, {}{}{}!!!'.format('\033[1;34m', nome, '\033[m'))

# Lista de cores
print('-=-'*20)

n = 'Felipe'
cores = {'limpa': '\033[m',
        'azul': '\033[1;34m',
        'amarelo': '\033[7;30m'}
    
print('Bem vindo, {}{}{}!!!'.format(cores['azul'], n, cores['limpa']))

'''style = 0,1,4,7
text = 30 ao 37
background = 40 ao 47'''