'''
Escreva um programa que verifique se uma frase é um palíndromo.
'''

frase = input('Digite uma frase para ver se é um palíndromo: ').strip().upper()

pontos = 0

for i in range(0, len(frase)):
    if frase[i] == frase[-i -1]:
        pontos = pontos + 1

    if pontos == len(frase):
        print('É um Palindromo')
    else:
        print('Não é uma Palíndromo')


if frase == frase [::-1]:
    print('É um palindromo')
else:
    print('Não é')