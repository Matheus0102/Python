'''
Escreva um programa que leia o
Nome, idade e sexo de 4 pessoas. No final mostre:

1. A média de idade do grupo
2. Qual é o homem mais velho
3. Quantas mulheres têm menos de 20 anos
'''

soma_idades = 0
quantidade_mulheres = 0
homem_velho = 0
nome_homem_mais_velho = 0
for i in range(1, 5):

    nome = input('Digite o seu nome:').strip().capitalize()
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite o seu sexo[M/F]: ').strip().upper()[0]

    soma_idades = (soma_idades + idade) / 4

    if sexo == 'F' and idade < 20:
        quantidade_mulheres = quantidade_mulheres + 1

    if sexo == 'M' and idade > homem_velho:
        homem_velho = idade
        nome_homem_mais_velho = nome

print(f'A média de idade do grupo é: {soma_idades}\n'
          f'O homem mais velho é {nome_homem_mais_velho}\n'
          f'{quantidade_mulheres} mulher tem menos de 20 anos no grupo')



