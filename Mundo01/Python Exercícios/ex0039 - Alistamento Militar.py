from datetime import date
atual = date.today().year
print('''Digite opções conforme seu Gênero:
            [1] Masculino
            [2] Feminino''')
gen = int ( input ('Digite aqui sua opção: '))
print('-=-'*20)
if gen == 2:
    print('\033[35mVocê não precisa fazer o alistamento militar obrigatório\033[m')
elif gen == 1:
    nasc = int ( input ('Digite o ano em que nasceu: '))
    idade = atual - nasc
    idadeP = idade - 18
    idadeA = 18 - idade
    a1 = atual - idadeP
    a2 = atual + idadeA
    print('-=-'*20)
    if idade == 19 and gen == 1:
        print('Você nasceu em \033[33m{}\033[m e sua idade é \033[33m{}\033[m era pra você ter se alistado a \033[36m{} ano\033[m'.format(nasc, idade, idadeP))
        print('Seu alistamento foi em \033[33m{}\033[m'.format(a1))
    elif idade > 19 and gen == 1:
        print('Você nasceu em \033[33m{}\033[m e sua idade é \033[33m{}\033[m era pra você ter se alistado a \033[36m{} anos\033[m'.format(nasc, idade, idadeP))
        print('Seu alistamento foi em \033[33m{}\033[m'.format(a1))
    elif idade == 17 and gen == 1:
        print('Você nasceu em \033[33m{}\033[m e sua idade é \033[33m{}\033[m e você deve se alistar daqui \033[36m{} ano\033[m'.format(nasc, idade, idadeA))
        print('Seu alistamento vai ser em \033[33m{}\033[m'.format(a2))
    elif idade < 17 and gen == 1:
        print('Você nasceu em \033[33m{}\033[m e sua idade é \033[33m{}\033[m e você deve se alistar daqui \033[36m{} anos\033[m'.format(nasc, idade, idadeA))
        print('Seu alistamento vai ser em \033[33m{}\033[m'.format(a2))
    elif idade == 18 and gen == 1: 
        print('Você nasceu em \033[33m{}\033[m e sua idade é \033[33m{} anos\033[m. Você deve se alistar \033[31mIMEDIATAMENTE!\033[m'.format(nasc, idade))
    else:
        print('\033[35mVocê não precisa fazer o alistamento militar obrigatório\033[m')
else:
    print('\033[31mOpção inválida, tente novamente!\033[m')
print('-=-'*20)


'''Faça um programa que leia o ano de nascimento de um jovem e informe, 
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''