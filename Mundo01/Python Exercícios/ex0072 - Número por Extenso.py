n = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quartorze', 'Quinze', 'Desesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
c = ' '
while True:
    print('-='*20)
    print('\033[1;46m Aperte 0 para Sair \033[m')
    num = int (input ('\033[1;43m Digite um número de 1 a 20:\033[m '))
    print('-='*20)
    if 0 <= num <= 20: 
        print(f'Você digitou \033[1;44m {n[num]} \033[m')
        c = str (input ('Quer continuar? [S/N] ')).upper().strip() [0]
        if c =='N':
            break
    else:
        print('\033[1;41m Valor incorreto. Tente novamente! \033[m')
print('\033[1;42m Volte sempre! \033[m')
print('-='*20)


''''Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, 
de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''