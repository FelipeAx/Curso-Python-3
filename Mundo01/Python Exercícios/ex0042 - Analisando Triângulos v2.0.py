print('-=-'*20)
print('Analisador de Triângulos')
print('-=-'*20)
a = float ( input ('Valor de A: '))
b = float ( input ('Valor de B: '))
c = float ( input ('Valor de C: '))
print('-=-'*20)
if a < b + c and b < a + c and c < a + b:
    print('\033[1mOs valores formam um triângulo\033[m', end=' ')
    if a == b == c:
        print('\033[4;33mEQUILÁTERO\033[m') #EQUILÁTERO: todos os lados iguais
    elif a != b != c != a:
        print('\033[4;33mESCALENO\033[m') #ESCALENO: todos os lados diferentes
    else:
        print('\033[4;33mISÓSCELES\033[m') #ISÓSCELES: dois lados iguais, um diferente

else:
    print ('\033[1;31mOs valores não formam um triângulo\033[m')
print('-=-'*20)



'''Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes'''