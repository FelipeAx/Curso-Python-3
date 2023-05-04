from datetime import date
atual = date.today().year
TotMaior = 0
TotMenor = 0
for c in range(1,8):
    ano = int(input('DIGITE SEU ANO DE NASCIMENTO {}: '.format(c)))
    idade = atual - ano
    if idade >= 18:
       TotMaior += 1
    else:
        TotMenor = TotMenor + 1
print('Ao todo tivemos {} pessoas menores de idade'.format(TotMenor))
print('E também tivemos {} maiores de idade'.format(TotMaior))


'''Crie um programa que leia o ano de nascimento de sete pessoas. 
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''