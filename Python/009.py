'''
Crie um programa que leia um nome, e mostre o primeiro e o último nome
Saída esperada:
Luis Felipe Tatin Vlatkovic
Primeiro nome: Luis
Último nome: Vlatkovic
'''

nome = input('Digite o seu nome: ').strip()

print(f'O Primeiro Nome: {nome[0:nome.find(' ')]}\n'
      f'O Ultimo nome é: {nome[nome.rfind(' ') + 1:]}\n')