s = ( float ( input ('Digite o seu salário atual: ')))
si = s + (s*0.15)
ss = s + (s*0.10)
print('-=-'*10)
if s <= 1250:
    print('Seu salário teve um aumento de 15%. Passou de R$ {:.2f} para R$ {:.2f}'.format(s,si))
else:
    print('Seu salário teve um aumento de 10%. Passou de R$ {:.2f} para {:.2f}'.format(s,ss))
print('-=-'*10)

# Outra maneira de se fazer

if s <= 1250:
    novo = s + (s * 15/100)
else:
    novo = s + (s * 10/100)

print('O seu salário passou de R$ {:.2f} para R$ {:.2f}'.format(s,novo))
print('-=-'*10)


'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
Para salários superiores a R$1250,00, calcule um aumento de 10%. 
Para os inferiores ou iguais, o aumento é de 15%.'''