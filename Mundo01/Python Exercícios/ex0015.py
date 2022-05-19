d=int(input('\nDigite quantos dias  o carro ficou alugado: '))
km=float(input('Digite a quantidade de km percorridos: '))
p=(km*0.15)+(d*60)
print('\nVocê ficou com o carro {} dias e percorreu {} km, o valor que terá que pagar é R$ {:.2f}\n'.format(d,km,p))
