print('{:=^40}'.format('LOJAS MACHADO'))
v = float ( input ('Digite o Valor do Produto: '))
print('''Digite opções conforme seu Gênero:
            [1] À vista Dinheiro/Cheque (10% de Desconto)
            [2] À vista no Cartão de Crédito (5% de Desconto)
            [3] Em 2x no Cartão de Crédito (Sem Juros)
            [4] 3x ou mais no Cartão de Crédito (Juros da Maquininha''')
opção = int ( input ('Digite aqui sua opção: '))
print('-=-'*10)
if opção == 1:
    d1 = v - (v*10/100)
    print('\033[1;34;43m Você ganhou 10% de Desconto! \033[m')
    print('Valor a Pagar: \033[32mR$ {:.2f}\033[m'.format(d1))
elif opção == 2:
    d2 = v - (v*5/100)
    print('\033[1;34;43m Você ganhou 5% de Desconto! \033[m')
    print('Valor a Pagar: \033[32mR$ {:.2f}\033[m'.format(d2))
elif opção == 3:
    p = v/2
    print('Você parcelou o valor de \033[32mR$ {:.2f}\033[m em \033[33m2 vezes\033[m'.format(v))
    print('Valor da Parcela: \033[32mR$ {:.2f}\033[m e você vai pagar o total de  \033[32mR$ {:.2f}\033[m no final'.format(p,v))
elif opção == 4:
    p1 = int (input ('Digite a Quantidade de Parcelas: '))
    j = (v/p1)+(v*20/100)
    t = j * p1
    print('Você parcelou o valor de \033[32mR$ {:.2f}\033[m em \033[33m{} vezes\033[m'.format(v, p1))
    print('Valor da Parcela: \033[32mR$ {:.2f}\033[m e você vai pagar \033[32mR$ {:.2f}\033[m no final'.format(j,t))
else:
    print('\033[1;31mVocê Digitou errado, tente novamente!\033[m')



print('-=-'*10)

'''Elabore um programa que calcule o valor a ser pago por um produto, 
considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal 

– 3x ou mais no cartão: 20% de juros'''