'''
Enunciado:
O computador escolhe um número aleatório entre 1 e 100.
O jogador tenta adivinhar.
A cada tentativa, o jogo informa se o número é maior ou menor do que o chute do jogador.
O jogo só termina quando o jogador acerta, e o programa mostra quantas tentativas ele precisou.
'''

'''
import random  # Importa a biblioteca para gerar números aleatórios

print('🎯 Bem-vindo ao Jogo de Adivinhação! 🎯')
print('Estou pensando em um número entre 1 e 100...')

# Gerando o número aleatório
numero_secreto = random.randint(1, 100)

tentativas = 0

while True:
    chute = int(input('Digite seu palpite: '))
    tentativas += 1

    if chute < numero_secreto:
        print('🔺 Meu número é MAIOR que isso.')
    elif chute > numero_secreto:
        print('🔻 Meu número é MENOR que isso.')
    else:
        print(f'🎉 Parabéns! Você acertou o número {numero_secreto}!')
        print(f'Você precisou de {tentativas} tentativas.')
        break  # Sai do loop quando acerta
'''

'''
Melhorias que vamos adicionar:
🎚️ Níveis de dificuldade:
Fácil: Número entre 1 e 50
Médio: Número entre 1 e 100
Difícil: Número entre 1 e 200
🎯 Limitar o número de tentativas:
Fácil: 10 tentativas
Médio: 7 tentativas
Difícil: 5 tentativas
🏆 Sistema de pontuação:
Começa com 1000 pontos.
Perde pontos a cada erro (ex.: 50 pontos por erro).
🔁 Permitir jogar novamente após ganhar ou perder.
'''

import random

print('🎯 Bem-vindo ao Jogo de Adivinhação PRO! 🎯')

while True:
    print('\nEscolha a dificuldade:')
    print('1 - Fácil (número entre 1 e 50, 10 tentativas)')
    print('2 - Médio (número entre 1 e 100, 7 tentativas)')
    print('3 - Difícil (número entre 1 e 200, 5 tentativas)')

    dificuldade = input('Digite sua opção (1, 2 ou 3): ')

    if dificuldade == '1':
        limite_superior = 50
        tentativas_totais = 10
    elif dificuldade == '2':
        limite_superior = 100
        tentativas_totais = 7
    elif dificuldade == '3':
        limite_superior = 200
        tentativas_totais = 5
    else:
        print('❌ Opção inválida. Tente novamente.')
        continue  # Volta para escolher a dificuldade

    numero_secreto = random.randint(1, limite_superior)
    tentativas = 0
    pontos = 1000

    print(f'\n🎮 Estou pensando em um número entre 1 e {limite_superior}.')
    print(f'Você tem {tentativas_totais} tentativas para adivinhar.')

    while tentativas < tentativas_totais:
        try:
            chute = int(input(f'\nTentativa {tentativas + 1}: Digite seu palpite: '))
        except ValueError:
            print('❌ Digite um número válido!')
            continue

        if chute < 1 or chute > limite_superior:
            print(f'❌ Digite um número entre 1 e {limite_superior}.')
            continue

        tentativas += 1

        if chute == numero_secreto:
            print(f'\n🎉 Parabéns! Você acertou o número {numero_secreto}!')
            print(f'Você fez {pontos} pontos em {tentativas} tentativas.')
            break
        elif chute < numero_secreto:
            print('🔺 Meu número é MAIOR que isso.')
        else:
            print('🔻 Meu número é MENOR que isso.')

        pontos -= 50  # Perde 50 pontos a cada erro

    else:
        print(f'\n😢 Suas tentativas acabaram. O número era {numero_secreto}.')
        print(f'Você terminou com {pontos} pontos.')

    jogar_novamente = input('\n🔄 Quer jogar novamente? (s/n): ').lower()
    if jogar_novamente != 's':
        print('👋 Obrigado por jogar! Até a próxima.')
        break
