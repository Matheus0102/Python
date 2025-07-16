#Operações Matematicas
'''
print('Olá Mundo!')
print(1515 + 15)
print(480 - 80)
print(5 * 5)
print(10 / 2)
print(2 ** 5)
print(8 % 2)

#Variáveis e print formatado
idade = 50
idade_2 = idade * 2
print(f'Sua idade é : {idade_2}')


#entrada de dados
nome = input('digite seu nome: ')
print(f'Seu nome é {nome}')

#Tipos de dados
idade_1 = int(input('Digite sua idade: '))
idade_2 = int(input('Digite sua idade: '))

soma = idade_1 + idade_2
print(f'A soma das idades é: {soma}')

#strings
nome = 'Luis Felipe Tatin Vlatkovic'

#Fatiamento
print(nome[3])
print(nome[3:7])

#Análise
print(len(nome)) # quantos caracteres existem
print(nome.count('i')) #quantas vezes aparece
print(nome.find('i')) #onde
print(nome.rfind('i')) #onde

#Transformação
nome = input('Digite o seu nome : ').strip()
print(nome)
nome.replace('i','p')
print(nome)
'''
'''
#condicionais
altura = float(input('Digite a sua altura(m): '))

if altura > 1.2:
    print('pode andar no brinquedo')
else:
    print('Quem sabe ano que vem! :) ')
'''
'''
if altura < 1.2:
    print('Quem sabe ano que vem')
elif altura > 2:
    print('Você vai bater a cabeça')
else:
    print('Pode andar no Brinquedo')
'''

# e - and

altura = float(input('Digite a sua altura(m): '))
peso = float(input('Digite o seu peso(kg): '))

if altura > 1.2 and altura < 2 and peso < 120:
    print('Pode andar no brinquedo')
else:
    print('Quem sabe ano que vem! ')

import random

pc = random.randint(1,10)
print(pc)

