'''
Escreva um programa que crie duas listas com 5 números cada uma e exiba a soma dos elementos correspondentes das duas
listas. Por exemplo, se as listas forem [1, 2, 3, 4, 5] e [5, 4, 3, 2, 1], o programa deve exibir [6, 6, 6, 6, 6].
'''

lista =[]
while True:
    try:
        n = int(input('N[negativo para sair]: '))
        if n < 0:
            break
        lista.append(n)
    except ValueError:
        print('Só aceitamos números')

print(f'A lista é {lista}')