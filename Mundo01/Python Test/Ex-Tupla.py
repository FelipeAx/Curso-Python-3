# Primeiros passos em Tuplas
print('-='*20)
lanche = ('Burguer', 'Suco', 'Pudim', 'Bolo', 'Misto')
print(lanche[:5])
print('-='*20)

# Usando for com Tuplas
lanche = ('Hamburguer', 'Pizza', 'Pudim', 'Lazanha', 'Misto')
for cont in range(0, len(lanche)):
    print(lanche[cont])
print('-='*20)

for comida in lanche[-5:]:
    print(f'Gosto de comer {comida}')
print(f'Essas as são minhas {len(lanche)} principais comidas preferidas')
print('-='*20)

#Caso queira enumerar a Tupla
for posição, comida in enumerate(lanche):
    print(f'{posição} - Gosto de comer {comida}')
print(f'Essas as são minhas {len(lanche)} principais comidas preferidas')
print('-='*20)

#Caso queira organizar a Tupla em ordem é só usar o Sorted
print('-='*20)
lanche = ('Burguer', 'Suco', 'Pudim', 'Bolo', 'Misto')
print(sorted(lanche)) #Ele organiza por ordem alfabética
print('-='*20)

#Outro exmplo de Tuplas com números
a = (2,4,6)
b = (8, 2, 12)
c = a + b #Ele junta as duas tuplas mas não soma (2,4,6,8,10,12)
print(c) 
print(len(c)) # Conta quantos números tem ao todo
print(c.count(2)) # Mostra quantas vezes o número 2 aparece dentro de C
print(c.index(8)) # Mostra a posição de 8 em C, 0,1,2,3 (2,4,6,8)
print(c.index(2)) # Mostra a posição de 0 em C, 0 (2)
print(c.index(2, 1)) # Mostra a posição de 4 em C mas nesse caso se inicia da posição 1 a contagem 1,2,3,4 (4,6,8,2)

#Pode ter dados diferentes dentro das tuplas
pessoa = ('Felipe', 29, 'Casado', 78 )
print(pessoa)