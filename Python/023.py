'''
Escreva um programa que leia o peso de 7 pessoas, e no final, mostre qual foi o maior e o menor peso lidos
'''

peso_maior = None
menor_peso = None

for i in range(1, 8):

    peso = float(input('Digite o seu peso: '))

    if peso_maior == None and menor_peso == None:
        peso_maior = peso
        menor_peso = peso

    if peso > peso_maior:
        peso_maior = peso

    if peso < menor_peso:
        menor_peso = peso

print(f'O maior peso é {peso_maior}\n'
      f'O menor peso é {menor_peso}')