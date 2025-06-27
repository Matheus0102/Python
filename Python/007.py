'''
Crie um algoritmo que leia um salário e simule um reajuste positivo de 60%.
Saída esperada:
O salário de 6000 com o reajuste de 60% será de : 9600
'''

salario = int(input('Digite o seu salario: '))

reajuste = salario * 1.6

print(f'O Salario de {salario} com o ajuste de 60% será de: {reajuste:.1f}')