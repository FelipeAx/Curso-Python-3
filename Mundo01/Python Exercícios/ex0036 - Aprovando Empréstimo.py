from time import sleep
print('-=-'*12)
casa = float ( input ('Digite o valor do imóvel: '))
salário = float ( input ('Digite o seu salário: '))
anos = int ( input ('Digite em quantos anos deseja pagar: '))
a = anos * 12
c = casa / a
s = salário *(30/100)
#prestação = casa / (anos *12)
print('-=-'*12)
print ('Seu salário é de \033[32mR$ {:.2f}\033[m e você deseja pagar um imóvel de \033[32mR$ {:.2f}\033[m em \033[34m{} anos\033[m.'.format(salário, casa, anos))
sleep(1)
print('\033[33mPROCESSANDO...\033[m')
sleep(4)
if c <= s:
        print('Parabéns, seu crédito foi \033[32mAPROVADO!\033[m')
        print('O valor da parcela será de: \033[32mR$ {:.2f}\033[m'.format(c))
else: 
        print('Crédito \033[31mNÃO APROVADO!\033[m')
        print('O valor da parcela é superior a \033[31m30%\033[m do seu salário.')
print('-=-'*12)

'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''