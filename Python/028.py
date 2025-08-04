'''
Crie uma calculadora que após ler 3 valores, mostre e opere de acordo com as opções:
1.	Somar
2.	Multiplicar
3.	Maior
4.	Novos números
5.	Sair do programa
'''

i = 1

while i > 0 :
    i += 1

    n1 = int(input('Digite o primeiro valor: '))
    n2 = int(input('Digite o segundo valor: '))
    n3 = int(input('Digite o terceiro valor: '))

    soma = n1 + n2 + n3
    multiplicacao = n1 * n2 * n3

    if n1 > n2 and n1 > n3:
        maior = n1
    elif n2 > n1 and n2 > n3:
        maior = n2
    else:
        maior = n3

    print(f'A soma dos 3 valores é: {soma}\n'
          f'A multiplicação dos 3 valores são: {multiplicacao}\n'
          f'O maior numero entre os 3 valores é: {maior}')

    print('1. Digite 1 se deseja adicionar novos valores\n'
          '2. Digite 2 se deseja encerrar o programa')

    menu = int(input('Digite a escolha: '))

    if menu == 2:
        print('Obrigado por utilizar o programa!')
        break
    else:
        print('Então vamos lá adicionar novos valores...')
        continue
