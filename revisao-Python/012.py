'''
Escreva um programa que peça ao usuário para adivinhar um número entre 1 e 10 e continue pedindo até que o usuário acerte o número. E no final, retorne também a quantidade de tentativas necessárias.
'''

import random

i = 1

while i > 0:

    usuario = int(input('Digite um numero de 1 a 10: '))
    i += 1

    pc = random.randint(1, 11)

    if usuario == pc:
        print(f'Você acertou!, você usou {i} tentativas.')
        break