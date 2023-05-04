n1 = float ( input ('Digite a Primeira Nota: '))
n2 = float ( input ('Digite a Segunda Nota: '))
média = (n1 + n2)/2
print('-=-'*12)
if média < 5:
    print('\033[1mMédia:\033[m \033[1;36m{}\033[m\n\033[1;31mREPROVADO!\033[m'.format(média))
#elif média >= 5 and média < 7:
elif 7 > média >= 5:
    print('\033[1mMédia:\033[m \033[1;36m{}\033[m\n\033[1;33mRECUPERAÇÃO!\033[m'.format(média))
else:
    print('\033[1mMédia:\033[m \033[1;36m{}\033[m\n\033[1;32mAPROVADO!\033[m'.format(média))
print('-=-'*12)



'''Crie um programa que leia duas notas de um aluno e calcule sua média, 
mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO'''