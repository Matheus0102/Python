'''
Crie um programa para jogar JOKEMPO, usando a função random.randint
'''

import random

pc = random.randint(1,3)

jogador = int(input('1. Pedra'
                    '\n2. Papel'
                    '\n3. Tesoura'
                    '\n--->  '))

if pc == jogador:
    print(f'Empate! - jogador - {jogador} x {pc} - PC')

elif (jogador == 1 and pc ==3) or (jogador == 2 and pc == 1) or (jogador == 3 and pc == 2):
    print(f'Vitoria! - jogador - {jogador} x {pc} - PC')
else:
    print(f'Perdeu! - jogador - {jogador} x {pc} - PC')
