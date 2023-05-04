g = str ( input ('Digite seu Gênero: [M/F] ')).upper().strip() [0]
while g != 'F' and g != 'M':
    g = str ( input ('Você digitou errado! Por favor Digite novamente: [F/M]')).upper().strip() [0]
print('Você é do gênero {}'.format(g))
    

'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. 
Caso esteja errado, peça a digitação novamente até ter um valor correto.'''