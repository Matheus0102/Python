'''
Escreva um programa que leia o peso de 7 pessoas, e no final, mostre qual foi o maior e o menor peso lidos
'''

maior = None
menor = None

for i in range(7):
    peso = float(input('Peso: '))

    if menor == None and maior == None:
        maior == peso
        menor == peso

    if peso > maior:
        maior = peso
    if menor < peso:
        menor = peso