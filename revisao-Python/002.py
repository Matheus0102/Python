'''
Escreva um programa que leia 6 notas diferentes e faça a média do aluno
Saída esperada:
A sua média final é : 5
'''

print('Digite 6 notas diferentes, e você irá ler a média do aluno!')

n1 = int(input('Nota 1: '))
n2 = int(input('Nota 2: '))
n3 = int(input('Nota 3: '))
n4 = int(input('Nota 4: '))
n5 = int(input('Nota 5: '))
n6 = int(input('Nota 6: '))

print(f' A média do aluno é: { (n1 + n2 + n3 + n4 + n5 + n6) / 6} ')