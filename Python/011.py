'''
Escreva um programa que peça ao usuário um número e imprima se é positivo ou negativo.
'''

numero = float(input('Digite o seu numero para saber se é positivo ou negativo: '))

if numero > 0:
    print('positivo')
elif numero == 0:
    print('Neutro')
else:
    print('Negativo')
