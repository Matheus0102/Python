'''
Crie um programa para analisar o IMC de uma pessoa, e classifique se ela está entre a faixa ideal, acima ou abaixo do IMC ideal.
'''

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = peso / (altura ** 2)

if imc > 27 :
    print('Obeso')
elif imc > 22:
    print('Normal')
else:
    print('Abaixo do peso')