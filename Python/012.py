'''
Escreva um programa que peça ao usuário um número e imprima se é par ou ímpar
'''

numero = int(input('Digite o seu numero para saber se é par ou ímpar: '))

numero_ = numero % 2

if numero_ == 0:
    print('O número é par')
else:
    print('O número é ímpar')