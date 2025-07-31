'''
Escreva um programa que leia um número n inteiro qualquer e mostra na tela os n primeiros elementos de uma Sequência de Fibonacci
'''

numero = int(input('Digite um numero: '))
i = 0

a = 1
b = 1

while i < numero:

    if numero == 1 :
        c = 0
        print(c)
    elif numero == 2 :
        c = 0
        print(f'{c} {a}')
    elif numero == 3 :
        c = 0
        print(f'{c}, {a}, {a}')
    else:
        p = b + a
        b = a
        a = p
        print(p)

    i += 1

