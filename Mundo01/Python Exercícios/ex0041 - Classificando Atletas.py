from datetime import date
n = int ( input ('\033[1mDigite Ano de Nascimento: \033[m'))
atual = date.today().year
idade = atual - n
print('\033[1mO atleta tem \033[33m{} anos\033[m\033[m'.format(idade))
print('-=-'*3)
print('\033[1;mCATEGORIA:\033[m')
if idade <= 9:
    print('\033[1;33mMIRIM\033[m')
elif 9 < idade <= 14: # pode ser assim também: elif idade<=14:
    print('\033[1;33mINFANTIL\033[m')
elif 14 < idade <= 19:
    print('\033[1;33mJÚNIOR\033[m')
elif 19 < idade <= 25:
    print('\033[1;33mSÊNIOR\033[m')
else:
    print('\033[1;33mMASTER\033[m')
print('-=-'*3)


'''A Confederação Nacional de Natação precisa de um programa 
que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER'''