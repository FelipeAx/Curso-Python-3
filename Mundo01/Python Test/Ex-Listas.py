num = [2, 5, 4, 7] #Lista 
num [2] = 3 #Substitui o que ta na posição 2 (que é o 4) pelo novo valor
num.append(8) #Adiciona valor ao final da lista
num.insert(1, 0) #Insere 0 na posição 1 afasta pra frente o restante
num.pop() #Sem parametro Remove o último valor
num.pop(1) #Remove o valor da posição 1 print(num)
if 2 in num:
    num.remove(2) #Vai eliminar o primeiro valor 2 que aparecer na lista
else:
    print('Não achei o número')
print(num)

valores = []
for cont in range(0, 3):
    valores.append(int(input('Digite um valor: ')))
print('-='*20)
for v in valores:
    print(f'{v}...', end='')
print('')
print('-='*20)
for c, v in enumerate(valores):
    print(f'Na posição {c} achei o valor {v}')
print('Cheguei ao final da lista!')
print('-='*20)

a = valores
b = a [:] #Essas chaves cria umá cópia de a, onde agora pode alterar apenas o b. 
b [2] = 8
print(a)
print(b)