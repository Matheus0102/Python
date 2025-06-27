'''
screva um programa que leia 6 notas diferentes e faça a média do aluno
Saída esperada:
A sua média final é : 5
'''

n1 = int(input('Digite a Primeira Nota: '))
n2 = int(input('Digite a Segunda Nota: '))
n3 = int(input('Digite a Terceira Nota: '))
n4 = int(input('Digite a Quarta Nota: '))
n5 = int(input('Digite a Quinta Nota: '))
n6 = int(input('Digite a Sexta Nota: '))

mediaAluno = (n1 + n2 + n3 + n4 + n5 + n6) / 6

print(f'A sua Média final é: {mediaAluno:.1f}')