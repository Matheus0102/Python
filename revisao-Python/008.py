'''
Crie um programa para jogar JOKEMPO, usando a função random.randint
'''

import random

print('Bem vindo ao Jogo de jokempo!!')

usuario = int(input('Digite 1 para papel, 2 para pedra e 3 para tesoura: '))

pc = random.randint(1, 3)

print(f'Você escolheu: {usuario}')
print(f'Computador escolheu: {pc}')

if usuario == pc:
    print('Empate')
elif usuario == 1 and pc == 2 or usuario == 2 and pc == 3 or usuario == 3 and pc == 1:
    print('Voce Venceu!')
else:
    print('Computador venceu!')