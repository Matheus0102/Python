'''
Escreva um programa que leia o nome, depois o sobrenome, e retorne para o usuário
Saída esperada:
Seu nome completo é: Luis Tatin
'''

nome = input('Insira seu Nome:')
sobreNome = input('Insira seu sobrenome: ')
nomeCompleto = nome + '' + sobreNome

print(f'Seu nome completo é: {nomeCompleto}')