from time import sleep
valor_inicial = float ( input ('Qual o valor inicial investido? '))
investimento_mensal = float ( input ('Qual valor mensal recorrente investido? '))
tempo = int ( input ('Quantos anos deseja investir? '))
juros = float (input ('Digite a taxa de juros anual: '))
juros_mês = (juros/100) / 12               
meses = tempo * 12
mês = 1
opção = -1
while opção != 0:
    print('''Digite a opção desejada:
            [ 1 ] Calcular
            [ 2 ] Add Novos Números
            [ 0 ] Sair do Programa''')
    print('-='*20)
    opção = int ( input ('Digite aqui sua opção: '))
    print('-='*20)
    if opção == 1:
        print('O valor do investimento no  1° mês é R$ {:.2f}'.format(valor_inicial))
        while mês < meses:
            valor_inicial = valor_inicial + (valor_inicial * juros_mês) + investimento_mensal
            mês = mês + 1
            print('O valor do investimento no {:2}° mês é R$ {:.2f}'.format(mês, valor_inicial))
        sleep(0.75)
    elif opção == 2:
        valor_inicial = float ( input ('Qual o valor inicial investido? '))
        investimento_mensal = float ( input ('Qual valor mensal recorrente investido? '))
        tempo = int ( input ('Quantos anos deseja investir? '))
        juros = float (input ('Digite a taxa de juros anual: '))
        juros_mês = (juros/100) / 12               
        meses = tempo * 12
        mês = 1
    elif opção == 0:
        print('Finalizando.',end='')
        sleep(0.75)
        print('.',end='')
        sleep(0.75)
        print('.')
        sleep(0.75)
        print('Programa Finalizado!')
        sleep(0.5)
        print('Volte sempre.')
        exit()
    else:
        print('Opção inválida, tente novamente...')
        sleep(1)
print('-='*20)



'Se eu investir x valor por x anos a um juros de x %, quanto terei no vencimento?'
