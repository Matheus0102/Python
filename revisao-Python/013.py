'''
Faça um programa que leia um número e retorne o fatorial !
4! = 4 x 3 x 2 x 1
'''

numero = int(input('Digite o numero que deseja o fatorial: '))
fat = 1

while numero > 0:
    fat = fat * numero
    print(f'Numero: {numero} - Fatorial - {fat}')
    numero -= 1