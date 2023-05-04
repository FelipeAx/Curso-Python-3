from time import sleep
print('-=-'*10)
print('Promoção de hoje!\n Viagem até 200km paga R$ 0.50 por km\n Viagem com mais de 200km paga R$ 0.45 por km')
d = float (input('Digite a Distância de sua Viagem: '))
p1 = d * 0.50
p2 = d * 0.45
print('-=-'*10)
print('Sua viagem é de {} Km'.format(d))
print('PROCESSANDO...')
sleep(4)
print('-=-'*10)
if d <= 200:
    print('O valor que você terá que pagar é: R$ {:.2f}'.format(p1))
else:
    print('O valor que você terá que pagar é: R$ {:.2f}'.format(p2))
print('Efetuando Pagamento...')
sleep(4)
print('-=-'*10)
print('Pagamento Realizado com Sucesso!')
sleep(1)
print('Tenha uma ótima viagem!')
print('-=-'*10)


'''Desenvolva um programa que pergunte a distância de uma viagem em Km. 
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45
para viagens mais longas.'''
