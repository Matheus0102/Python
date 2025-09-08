'''
Crie um programa para jogar par ou ímpar com o usuário, e só pare quando perder. Ao final deve mostrar a quantidade de vitórias
'''

import random

vitorias = 0

while True:

    pc = random.radient(1, 10)
    j = int(input('Digite um numero entre 1 a 10: '))
    escolha = input('Par ou Ímpar[P/Í]: ')

    if ((pc + j) % 2 == 0 and escolha == 'P') or ((pc + j) % 2 != 0 and escolha == 'Í'):
        print(f'Parábens você ganhou - {pc + j}')
        vitorias += 1
    else:
        print(f'Você Perdeu com {vitorias} vitorias')
        break