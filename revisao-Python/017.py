'''
Crie um programa que retorne a tabuada de um número, e só pare quando o número digitado for 0000
'''

while True:
    n = input('N[0000 para sair]: ')

    if n == '0000':
        break

    for i in range(11):
        print(f'{n} X {i}')