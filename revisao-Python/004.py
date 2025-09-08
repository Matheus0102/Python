'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas
O nome com todas minúsculas
Quantas letras ao todo (sem considerar os espaços)
Quantas letras tem o primeiro nome
'''

nome = input('Digite o seu nome: ').strip()

print(nome.upper())
print(nome.lower())

nome.replace(' ', '')
nome = len(nome)

print(nome)

nome = nome.count(' ')
contarCaracteres = len(nome)

