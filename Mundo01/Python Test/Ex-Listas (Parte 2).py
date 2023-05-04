teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:]) #Necessário colocar [:] pra criar uma cópia, se não vai printar só Maria, 22.
teste[0] = ('Maria')
teste[1] = (22)
galera.append(teste[:])
print(galera)

print('')
Family = [['Felipe', 29], ['Mirlene', 30], ['Marula', 1]]
print(Family[0][0]) #Nesse exemplo vai aparecer apenas Felipe, se colcoar [1][1] vai aparecer 30 idade da Mirlene.
for p in Family:
    print(p[0]) #Se der print no p[0] vai aparecer uma lista dos nomes, se colocar só o p printa todos em lista.
print('')

guys = list()
data = list()
totmaior = totmenor = 0
for c in range(0,3):
    data.append(str(input('Name: ')))
    data.append(int(input('Age: ')))
    guys.append(data[:])
    data.clear()
print(guys[0])

for p in guys:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmenor += 1
print(f'Total de maiores: {totmaior}')
print(f'Total de menores: {totmenor}') 
