'''
Escreva um programa que imprima a tabuada de um número fornecido pelo usuário.
'''

numero = int(input('Digite o numero que deseja da tabuada: '))

for i in range(1, 11,):
    print(f'{numero}x{i}={i * numero}')