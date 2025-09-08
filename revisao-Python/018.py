'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final mostre:
Qual é o total gasto na compra
Quantos produtos custam mais de R$1000,00
Qual é o produto mais barato
'''

soma = 0
quant_maior_1000 = 0
preco_mais_barato = None
nome_mais_barato = ''

while True:
    produto = input('Produto [0000 para sair]: ')

    if produto == '0000':
        break

    preco = float(input('Digite o Preço: '))

    #1
    soma += preco

    #2
    if preco > 1000:
        quant_maior_1000 += 1

    #3
    if preco_mais_barato == None:
        preco_mais_barato = preco
        nome_mais_barato = produto

    print(f'A soma é {soma}\n'
          f'Quantidade de produtos maior que 1000 é {quant_maior_1000}\n'
          f'O produto mais barato é: {nome_mais_barato}')
