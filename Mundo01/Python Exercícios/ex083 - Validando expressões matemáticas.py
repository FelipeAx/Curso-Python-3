expressão = str (input ('Digite sua expressão: '))
pilha = []
for símbolo in expressão:
    if símbolo == '(':
        pilha.append('(')
    elif símbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão é válida!')
else:
    print('Expressão incorreta!')




'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e 
fechados na ordem correta.'''