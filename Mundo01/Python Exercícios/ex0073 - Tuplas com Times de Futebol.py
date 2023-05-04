times = ('none', 'Palmeiras', 'Athlético - PR', 'Atlético - MG', 'Corinthians', 'Internacional', 'Fluminense',
        'São Paulo', 'Flamengo', 'Botafogo', 'Santos', 'Avaí', 'Coritiba', 'América - MG', 'Bragantino', 
        'Ceará - SC', 'Atlético - GO', 'Goiás', 'Cuiabá', 'Juventude', 'Fortaleza')
print('-='*20)
print('Os 5 Primeiros Colocados:')
print('-='*20)
for posição, time in enumerate(times[:6]):
    if posição > 0:
        print(f'{posição} - {time}')
print('-='*20)
print('Últimos 4 colocados na Classificação:')
print('-='*20)
for time in times[-4:]:
        print(f'{time}')
print('-='*20)
print('Ordem Alfabética dos times:')
for t in sorted(times):
    if t != 'none':
        print(t)
print('-='*20)
print(f'O time da do Coritiba está na posição {times.index("Coritiba")}') 
print('-='*20)


'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, 
na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''