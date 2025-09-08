'''
Crie um programa que pede ao usuário para digitar dois números e, em seguida, divide o primeiro número pelo segundo número. No entanto, o programa deve ser capaz de lidar com a possibilidade de o usuário digitar um valor inválido, como uma string ou o número zero.
ZeroDivisionError ; ValueError
'''

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

try:
    div = n1 / n2
except ZeroDivisionError:
    print('Valor inválido, não é possível divir por zero!')

