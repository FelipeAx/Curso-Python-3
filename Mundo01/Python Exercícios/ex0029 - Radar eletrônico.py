print('-=-'*15)
v = float (input ('Digite a velocidade do veículo: '))
m = (v - 80)*7
print('-=-'*15)
print('Sua velocidade foi de {:.2f} Km/h'.format(v))
if v > 80:
    print('Você foi multado no valor de R$ {:.2f}'.format(m))
else:
    print('Tenha um bom dia e dirija com segurança.')
print('-=-'*15)





'''Escreva um programa que leia a velocidade de um carro. 
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
A multa vai custar R$7,00 por cada Km acima do limite.'''