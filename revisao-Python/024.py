'''
Usando tuplas, leia um número de 0 a 15, e retorne esse número escrito por extenso
'''

'''
for cont in range(0, len(numeros)):
    print(numeros[cont])
'''

numeros_extensos = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze')

try:
    n = int(input('Digite um numero entre 0 a 15: '))
    while n < 0 or n > 15:
        n = int(input('Digite um numero entre 0 a 15: '))
        print(f'Seu numero por extenso é = {numeros_extensos[n]}')
except ValueError:
    print('Digite um numero válido!')

