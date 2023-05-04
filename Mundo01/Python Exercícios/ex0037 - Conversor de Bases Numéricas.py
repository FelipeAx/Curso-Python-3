n = int ( input ('Digite um número: '))
print('''Escolha uma das bases para conversão:
            [1] Converter para Binário
            [2] Converter para Octal
            [3] Converter para Hexadecimal''')
opção = int ( input ('Dgite aqui a sua opção: '))
print('-=-'*15)
if opção == 1:
    print('\033[33m{}\033[m convertido para \033[34mBINÁRIO\033[m é \033[33m{}\033[m'.format(n,bin(n)[2:]))
elif opção == 2:
    print('\033[33m{}\033[m covnertido para \033[34mOCTA\033[m é \033[33m{}\033[m'.format(n,oct(n)[2:]))
elif opção == 3:
    print('\033[33m{}\033[m convertido para \033[34mHEXADECIMAL\033[m é \033[33m{}\033[m'.format(n,hex(n)[2:]))
else:
    print('\033[31mOpção inválida, tente novamente!\033[m')
print('-=-'*15)

''''Escreva um programa em Python que leia um número inteiro qualquer e 
peça para o usuário escolher qual será a base de conversão: 1 para binário, 
2 para octal e 3 para hexadecimal.'''