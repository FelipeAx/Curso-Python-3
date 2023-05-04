lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    opção = str ( input ('Deseja continuar? [S/N] ')).upper().strip()[0]
    if opção in 'N':
        break
print('-='*20)
print(f'{len(lista)} números foram Digitados')
print(f'Lista de valores digitados: {lista}')
print(f'Lista Crescente: {sorted(lista)}')
print(f'Lista Descrescente: {sorted(lista, reverse = True)}')
if 5 in lista:
    print('O valor 5 está na lista? Sim')
else:
    print('O valor 5 está na lista? Não')
print('-='*20)



'''Crie um programa que vai ler vários números e colocar em uma lista.                  
Depois disso, mostre:                                                                                                                                                
A) Quantos números foram digitados.                                                                                                                    
B) A lista de valores, ordenada de forma decrescente.                                                                                          
C) Se o valor 5 foi digitado e está ou não na lista.'''