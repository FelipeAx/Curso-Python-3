n=input('Qual seu Nickname: ')
print('Seu Nickaname é: ',n,
    '\n',type(n),
    '\n Tem só Letras? ',n.isalpha(),
    '\n Tem só números? ',n.isnumeric(),
    '\n Tem Letras ou números? ',n.isalnum(),
    '\n Tem só letra Maiúscula? ',n.isupper(),
    '\n Tem só Letras Minusculas? ',n.islower(),
    '\n Está capitalizada? ',n.istitle(),
    '\n Tem só espaços? ',n.isspace(),
    )
