'''
Escreva um programa que leia, o nome, idade, e cidade de nascimento e retorne para o usuário
Saída esperada:
Meu nome é Luis Tatin, tenho 22 anos e nasci em São Bernardo do campo
'''

print('Olá, Digite o seu nome, idade e cidade de nascimento a seguir: ')

nome = input('Nome: ')

idade = int(input('Idade: '))

cidadeDeNascimento = input('Cidade de nascimento: ')

print(f'Nome: {nome}, '
      f'Idade: {idade}, '
      f'Cidade de nascimento: {cidadeDeNascimento}')
