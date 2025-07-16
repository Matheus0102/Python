'''
Crie um programa para jogar JOKEMPO, usando a função random.randint
'''

import random

usuario = int(input('escolha 1 para papel, 2 para tesoura ou 3 para pedra: '))

pc = random.randint(1,3)

if usuario > pc or usuario > pc:
    print('Voce venceu!')
