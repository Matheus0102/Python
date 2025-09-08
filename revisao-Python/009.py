'''
Escreva um programa que imprima a tabuada de um número fornecido pelo usuário.
'''

n = int(input('Digite um numero: '))

for i in range(11):
    print(f'{n} x {i} = {n * i}')
