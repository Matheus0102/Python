'''
Desafio 2 — Com for:
Peça um número ao usuário e exiba a tabuada desse número (de 1 a 10).
'''

'''
numero = int(input('Digite um número para ver a tabuada: '))

print(f'Tabuada do {numero}: ')

for i in range(1, 11):
    resultado = numero * i
    print(f'{numero} x {i} = {resultado}')
'''

'''
Enunciado bônus:
Peça ao usuário um número inicial e um número final.
Mostre a tabuada de todos os números dentro desse intervalo, de 1 a 10.
'''

'''
inicio = int(input('Digite o número inicial: '))
fim = int(input('Digite o número final: '))

print(f'\nTabuadas de {inicio} até {fim}:\n')

for numero in range(inicio, fim + 1):
    print(f'--- Tabuada do {numero} ---')
    for i in range(1, 11):
        resultado = numero * i
        print(f'{numero} x {i} = {resultado}')
    print()  # Linha em branco para separar as tabuadas
'''

'''
🚀 ✅ Enunciado mega-bônus:
Verificar se o número inicial é menor ou igual ao número final.
Se não for, mostrar um aviso e pedir os números novamente.

Permitir que o usuário escolha até qual número deseja ver a multiplicação (ex.: até 10, 20, 100…).
'''

# Verificando se o número inicial é menor ou igual ao final
while True:
    inicio = int(input('Digite o número inicial: '))
    fim = int(input('Digite o número final: '))

    if inicio <= fim:
        break
    else:
        print('❌ O número inicial deve ser MENOR ou IGUAL ao número final. Tente novamente.\n')

# Perguntar até qual multiplicador o usuário quer
limite = int(input('Digite até qual multiplicador você quer (ex.: 10, 20, 100...): '))

print(f'\nTabuadas de {inicio} até {fim}, até o multiplicador {limite}:\n')

# Gerando as tabuadas
for numero in range(inicio, fim + 1):
    print(f'--- Tabuada do {numero} ---')
    for i in range(1, limite + 1):
        resultado = numero * i
        print(f'{numero} x {i} = {resultado}')
    print()  # Linha em branco para separar as tabuadas
