'''
Crie um programa para jogar par ou ímpar com o usuário, e só pare quando perder.
Ao final deve mostrar a quantidade de vitórias
'''

import random

print('Bem Vindo ao Duelo de par ou ímpar!! \n'
      'Escolha entre par ou ímpar, e boa sorte!!')

vitorias = 0

while True:

    escolha = input('Par ou ímpar[P/I]: ').upper()[0]
    while escolha not in ('P', 'I'):
        escolha = input('Entrada inválida! Escolha par ou ímpar[P/I]: ').upper()[0]

    try:
        jogador_1 = int(input('Digite um numero(0-10): '))
        while jogador_1 < 0 or jogador_1 > 10:
            jogador_1 = int(input('Numero inválido! digite um numero(0-10): '))
    except:
        print('Entrada inválida, digite um número válido!')
        continue

    jogador_2 = random.randint(0, 10)

    soma = jogador_1 + jogador_2
    resultado = 'par' if soma % 2 == 0 else 'impar'

    print(f'Você escolheu {jogador_1} e o computador escolheu {jogador_2}, a soma foi: {soma}, e o resultado foi: {resultado}')

    if escolha == 'P' and resultado == 'par' or escolha == 'I' and resultado == 'impar':
        print('Você ganhou!')
        vitorias += 1
    else:
        print(f'Você perdeu! Total de vitorias: {vitorias}')
        tentativas = int(input('1. Digite 1 se deseja jogar novmente.\n'
                               '2. Digite 2 se não deseja mais jogar.\n'
                               '---> '))
        if tentativas == 1:
            continue
        else:
            print('Foi bom jogar com você, mais sorte na próxima!!')
            break

