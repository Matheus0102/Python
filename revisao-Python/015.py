'''
Crie uma calculadora que após ler 3 valores, mostre e opere de acordo com as opções:
1.	Somar
2.	Multiplicar
3.	Maior
4.	Novos números
5.	Sair do programa
'''

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))

while True:

    escolha = int(input('1. Soma \n'
                        '2. Multiplicador \n'
                        '3. Maior \n'
                        '4. Novos números \n'
                        '5. Sair do Programa \n'
                        'Escolha: '))

    if escolha == 1:
        print(n1 + n2 + n3)
    elif escolha == 2:
        print(n1 * n2 * n3)
    elif escolha == 3:
        if n1 > n2 or n1 > n3:
            maior = n1
            print(f'{maior}')
        elif n2 > n1 or n2 > n3:
            maior = n2
            print(f'{maior}')
        else:
            maior = n3
            print(f'{maior}')
    elif escolha == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
        n3 = int(input('Digite o terceiro valor: '))
    elif escolha == 5:
        break
    else:
        print('Opção incorreta')

