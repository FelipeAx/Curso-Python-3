num = [[], []]
valor = 0
print('-='*20)
for c in range(1, 8):
    valor = int(input(f'Digite um valor {c}: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-='*20)
num.sort()
num[0].sort()
num[1].sort()
print(num)
print(f'Pares digitados: {num[0]}')
print(f'Impares digitados: {num[1]}')
print('-='*20)



'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os 
em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre 
os valores pares e ímpares em ordem crescente.'''