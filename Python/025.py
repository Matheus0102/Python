'''
Escreva um programa que peça ao usuário para adivinhar um número entre 1 e 10 e continue pedindo até que o usuário acerte o número. E no final, retorne também a quantidade de tentativas necessárias.
'''

import random

tentativas = 1
pc = random.randint(1, 10)
jogador = int(input('Digite um numero de 1 a 10: '))

while jogador != pc:
    tentativas += 1
    jogador = int(input('Tente outro número: '))

print('VITORIA! \n'
      f'Quantidade de tentativas: {tentativas}')

